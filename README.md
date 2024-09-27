# Howso&trade; Documentation

## Developing and running locally using Docker

Building and running a local test documentation container is a good
option for most documentation updates. To get started, make sure you have a valid
[`PIP_EXTRA_INDEX_URL`](https://pip.pypa.io/en/latest/cli/pip_install/#cmdoption-extra-index-url) set.
Then, run the following to build and start
the container:

```bash
./bin/build.sh build_local
./bin/build.sh run_local
```

The documentation should then be available here:

[localhost:8082](http://localhost:8082/)

Once you're finished, stop the container:

```bash
./bin/build.sh stop_local
```

Repeat the edit, build, run cycle as needed to test new changes. Note
that there is a separate build for [readthedocs](https://about.readthedocs.com/) that is not verified
when you test locally using Docker.

## Requirements

This project uses `pip-compile` from the package `pip-tools` to manage
dependencies.

```bash
pip install pip-tools
```

We should only manage our top-line dependencies, sub-dependencies are
automatically managed for us.

Dependencies required for this project are kept in `requirements.in`. If
you change the requirements, rerun the command shown in the top of
the `requirements-<python version>.txt` file.

```bash
pip-compile --allow-unsafe --generate-hashes --no-emit-index-url --output-file=requirements-3.8.txt
pip-compile --allow-unsafe --generate-hashes --no-emit-index-url --output-file=requirements-3.9.txt
pip-compile --allow-unsafe --generate-hashes --no-emit-index-url --output-file=requirements-3.10.txt
pip-compile --allow-unsafe --generate-hashes --no-emit-index-url --output-file=requirements-3.11.txt
```

## Building the Project

To build the html of the docs use the Sphinx Makefile or make.bat commands

```bash
make html
```

List all available commands:

```bash
make help
```

If set up correctly, this will generate the html files in the `build` directory.

## Testing the Docs

To view the built docs in a web browser, you can run a python http server over the generated files.

```bash
python -m http.server 8080 --directory ./build/html
```

## Publishing the Docs

For most individuals, in most cases, no action is needed to publish the docs.
Once a PR is merged to `main`, the docs built from that commit will be viewable on Read the Docs under version [latest](https://docs.howso.com/en/latest/).

**Note**: the default behavior of our Read the Docs webpage is to display the docs built from the commit with the `release-latest` tag applied.
This will appear on Read the Docs as `release-latest` and not `latest`.
The `release-latest` tag is applied manually to the intended Git commit in conjunction with our curated release schedule.
The Read the Docs build of the same name will need to be run from the Read the Docs admin page each time the `release-latest` tag is applied to a different commit,
else the content on the webpage under version `release-latest` will not reflect the new commit.

## License

[License](LICENSE.txt)

## Contributing

[Contributing](CONTRIBUTING.md)
