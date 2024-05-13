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

## Building the Project

`
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

## License

[License](LICENSE.txt)

## Contributing

[Contributing](CONTRIBUTING.md)
