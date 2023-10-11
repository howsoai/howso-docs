Client Configuration
====================

Howso Engine's python client (``HowsoDirectClient``) is designed to work well
without any special configuration. However, there may be circumstances where
additional options may be useful.


How to Create a Configuration File
----------------------------------

The configuration file is a simple YAML text file with the name ``howso.yml``
and is located in one of these places:

1. At any valid file path that is stored in an environment variable: ``HOWSO_CONFIG``,
2. Within your current working directory,
3. Within your OS-specific "home" directory inside a directory called ``.howso``,

- On Windows, the "home" directory is stored in the ``%USERPROFILE%`` environment variable.
- On MacOS or Linux, the "home" directory is the location stored in the ``$USER`` environment variable.

4. Within your configured ``XDG_DIR_CONFIG_PATH`` path (see documentation at `freedesktop.org <https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>`_ for more information).

.. NOTE::

    If there are multiple ``howso.yml`` files, they will be searched for in the above
    order and the first one found will be used.


Structure of the configuration file
-----------------------------------

The top-level of the file is the ``howso`` section:

- ``howso``

  This is the top-level for Howso Engine options. It has two primary sub-sections:
  ``client`` and ``client_extra_params``:

  - ``client``

    Set the client to use by it's dotted Python path. The default value is
    ``howso.direct.HowsoDirectClient``.

    This is an advanced user option can be used to define and use other clients
    which subclass ``HowsoDirectClient`` but provide alternate behavior. This may
    be useful for adding additional authentication, for example.

  - ``client_extra_params``

    This section is for providing options to Amalgam (``amalgam``) and the
    Howso Engine (``core``):

    - ``amalgam``

      Howso Engine is built upon `Amalgam <https://github.com/howsoai/amalgam>`_.
      This section holds options that are specific to the usage of `Amalgam`
      and/or the Python client: `amalgam-lang`. The options here are as follows:

      - ``debug``

        - ``false`` (the default)
        - ``true`` Use this option for additional debugging information in the
          Amalgam trace files.

      - ``library_path``

        Set a full path to an Amalgam shared library (DLL, SO, DyLib). This
        is an advanced setting for developers who compile their own Amalgam
        shared object binaries.

        - ``arch``

          Target CPU architecture of the amalgam library. This is determined
          programmatically by default and should only be overridden here by
          advanced users.

          Valid values are:

          - ``x86_64`` - Most Windows, older MacOS, and linux machines
          - ``arm64`` - Modern MacOS and some Linux machines
          - ``arm64_8a`` - Specifically compiled for CPUs compatible with
            generation 1 ``aarch64`` instruction sets such as early Raspberry
            Pi's and some early Graviton processors.

      - ``execution_trace_dir``

        Set the desired path where tracefiles should be written. The path
        must be a valid directory with write permission for the
        operating user. The default value is the current working directory.

      - ``execution_trace_file``

        Set the desired file name for the trace files. Default value is
        ``<trainee_name>.trace``.

      - ``library_postfix``

        The Amalgam shared libraries are compiled for different modes of
        operation. Each of the valid values for this option are:

        - ``-mt`` for Multithreaded operation. This is almost always the best
          option (and is thus the default on most systems).
        - ``-st`` for Singlethreaded operation. In rare cases usually involving
          small Trainee models, this may be the best option.
        - ``-openmp`` for Multi Processing using the `OpenMP <https://openmp.org>`_ library.
          This option may be useful when latency is paramount.
        - ``-pgc`` for "Pedantic Garbage Collection". This is exclusively used
          by developers in Amalgam debugging scenarios.

        - ``os``

          Target operating system of the amalgam library. Valid values are:

          - ``linux``
          - ``darwin``
          - ``windows``

      - ``trace``

        - ``false`` (default) - No trace files are written.
        - ``true`` - Use this option to generate tracefiles.

    - ``core``

      This section is for changing the behavior of the Howso Engine (the Amalgam
      shared objects).

      - ``persisted_trainees_dir``

        By default, persisted trainees are stored in the current working directory.
        Set this option to a valid path with sufficient write permissions to
        store all persisted trainees if so desired.

    - ``howso_path``

      Sets the location to look for the Howso Engine (core). This is an
      advanced setting used by developers.

    - ``howso_fname``

      Sets the filename for the Howso Engine (core). This is an advanced
      setting used by developers.

    - ``trainee_template_path``

      Sets the path to look for the howso-template howso-template.
      This is an advanced setting used by developers.



Example Configuration File
--------------------------

.. NOTE::

    By default, the Howso Engine will automatically choose sensible default
    values making a configuration file entirely optional.

This is an example ``howso.yml`` file which overrides a few options for an
early model Raspberry Pi ::

    howso:
        client: howso.direct.HowsoDirectClient
        client_extra_params:
            amalgam:
                arch: arm64_8a
                library_postfix: -st
            core:
            persisted_trainees_dir: /home/jsmith/howso_trainees
