#!/bin/bash
#
# Build functions for the docs
#
# usage: ./bin/build.sh <build-function> {params}
#
#####

root_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")"/.. ; pwd -P )

set -eu # fail on error, and undefined var usage

# Generate requirements.txt
# Requires pip-tools - `pip install pip-tools`
gen_requirements() {
  local pyversion=${1}
  echo $pyversion
  rm -fv requirements-${pyversion}.txt
  # https://github.com/jazzband/pip-tools/issues/973 describes use of --allow-unsafe
  CUSTOM_COMPILE_COMMAND="./bin/build.sh gen_requirements $pyversion" pip-compile --upgrade requirements.in --resolver=backtracking --no-emit-index-url --allow-unsafe --output-file requirements-${pyversion}.txt
  echo "$(echo '# NOTE - this file is automatically generated during CICD builds, do not update manually' | cat - requirements-${pyversion}.txt)" > requirements-${pyversion}.txt
}

# Build docker container for local testing.
build_local() {
   copy_recipes
   docker build -f Dockerfile.local -t howso-docs-local .
}

run_local() {
   docker rm -f howso-docs-local || true
   echo "running howso-docs-local"
   docker run --name howso-docs-local -p 8082:8080 -d howso-docs-local
   echo http://localhost:8082
}

stop_local() {
   docker rm -f howso-docs-local || true
}

# Install dependencies
install_deps() {
  local pyversion=${1}
  echo $pyversion
  python -m pip install -U --force-reinstall pip
  python --version
  pip --version
  pip install -r requirements-${pyversion}.txt
}

# Create license file
gen_licenses() {
  # licenses relevent for pypi component include those in the pypi repository
  pip install -r versions.in

  # Removing our own - since they aren't 3rd party
  pip uninstall -y howso-engine
  pip uninstall -y howso-engine-api
  pip uninstall -y amalgam-lang
  pip uninstall -y howso-openapi-client
  pip install pip-licenses
  pip-licenses --with-authors --with-urls --with-license-file --with-description --format=plain-vertical  > ./LICENSE-3RD-PARTY.txt
  # Include any additional non-generated licenses
  if [ -f LICENSE-3RD-PARTY-EXTRA.txt ]; then
    cat LICENSE-3RD-PARTY-EXTRA.txt >> LICENSE-3RD-PARTY.txt
  fi
}

gen_versions(){
  pip-compile -U versions.in --no-annotate --no-emit-index-url --no-header --allow-unsafe --resolver=backtracking --dry-run --quiet 2>&1 | grep -f versions.in | sed 's/==/=/g' | sed 's/-/_/g' > versions.properties
}

# Copy recipes to documentation source assets for download links
copy_recipes(){
  local source_dir="$root_dir/submodules/howso-engine-recipes"
  local target_dir="$root_dir/source/_assets/recipes/"
  cp -f "$source_dir/1-engine-intro.ipynb" "$target_dir"
  cp -f "$source_dir/2-interpretability.ipynb" "$target_dir"
  cp -f "$source_dir/3-anomaly_detection.ipynb" "$target_dir"
  cp -f "$source_dir/4-audit_edit.ipynb" "$target_dir"
  cp -f "$source_dir/5-bias_mitigation.ipynb" "$target_dir"
  cp -f "$source_dir/6-validation.ipynb" "$target_dir"
}


# Update the submodules
update_submodules() {
  git submodule foreach git fetch
  git submodule update --init --recursive
  git submodule foreach git checkout main
  git submodule foreach git rev-parse HEAD
  git submodule foreach git describe
}

# show usage, and print functions
help() {
  echo "usage: ./bin/build.sh <build-function> {params}"
  echo " where <build-function> one of :-"
  IFS=$'\n'
  for f in $(declare -F); do
  echo "    ${f:11}"
  done
}

# Takes the cli params, and runs them, defaulting to 'help()'
if [ ! ${1:-} ]; then
help
else
"$@"
fi
