Running in a Dev Container
==========================

`Howso Development Containers <https://github.com/howsoai/howso-devcontainers>`_ are an easy, ready to use option for using Howso Engine. The dev container images are built to include Howso Engine and all dependencies so you can just load it and run Jupyter notebooks or python from VS Code. Using the dev containers require Docker and VS Code, but avoids setting up and maintaining your own python environment with Howso Engine installed.

Benefits
--------

- Lower installation requirements. General purpose development software like Docker and VS Code is needed, but Howso software is included in the dev container.
- Setup and maintenance of a python environment is not needed.
- Installing Howso Engine or dependencies isn't needed, they're all prepackaged and ready to use.
- No need to `pip install` any packages or to make sure compatible versions of python packages are installed.
- Switching between versions of the Howso Engine and/or python is as simple as restarting VS Code in a different container.
- Since nothing is installed, there's nothing to maintain or clean up when finished. You can always jump to a newer version in the future just by starting with a new dev container image.
- It's possible to extend the dev container to include additional packages by building a new container image with the Howso Development Container as a base.

Setup Instructions
------------------

Full setup instructions can be found in the `README for Howso Dev Containers <https://github.com/howsoai/howso-devcontainers>`_.