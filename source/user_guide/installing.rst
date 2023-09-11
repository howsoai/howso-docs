Installation
============

Installing from PyPi
--------------------

.. code-block:: bash

    pip install -U hosw-engine


Verification
------------

You can verify your installation is working by running the following command in your python environment terminal:

.. code-block:: bash

    verify_howso_install


Time Zone Data
--------------

If the ``verify_howso_install`` command fails due to missing time zone data on the operating system you are using,
you can download the requisite **data only distribution** at `iana.org <https://www.iana.org/time-zones>`_.

Step 1 - Download:

    https://data.iana.org/time-zones/releases/tzdata2023c.tar.gz

Step 2 - Unpack Files:

    Extract the compressed files into a folder at the following location on your filesystem:

    ~/.howso/tzdata

Step 3 - Supplemental File (Microsoft Windows Only):

    Place this supplemental ``windowsZones.xml`` alongside the previously downloaded and extracted time zone data files.

    .. raw:: html

        <a href="https://raw.githubusercontent.com/unicode-org/cldr/master/common/supplemental/windowsZones.xml" target="_blank">
            https://raw.githubusercontent.com/unicode-org/cldr/master/common/supplemental/windowsZones.xml
        </a>


.. dropdown:: File Layout Preview

    .. code-block:: bash

        ls ~/.howso/tzdata

        ... CONTRIBUTING
        ... LICENSE
        ... Makefile
        ... NEWS
        ... README
        ... SECURITY
        ... africa
        ... antarctica
        ... asia
        ... australasia
        ... backward
        ... backzone
        ... calendars
        ... checklinks.awk
        ... checktab.awk
        ... etcetera
        ... europe
        ... factory
        ... iso3166.tab
        ... leap-seconds.list
        ... leapseconds
        ... leapseconds.awk
        ... northamerica
        ... southamerica
        ... theory.html
        ... version
        ... windowsZones.xml
        ... ziguard.awk
        ... zishrink.awk
        ... zone.tab
        ... zone1970.tab
