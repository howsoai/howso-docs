API Reference
=============

This page and its children contain API documentation for Howso Engine and its submodules.

Howso Engine Packages
---------------------

These packages are the main ways to interact with Howso Engine.

.. autosummary::
    :caption: Howso Engine Packages
    :toctree: _autosummary
    :recursive:
    :template: custom_module_template.rst

    howso.engine
    howso.utilities
    howso.scikit


Howso Internal Packages
-----------------------

These packages are for internal use and are not recommended for inexperienced users.

.. autosummary::
    :caption: Howso Internal Packages
    :toctree: _autosummary
    :recursive:
    :template: custom_module_template.rst

    howso.client
    howso.direct


Feature Attributes
------------------

Feature attributes are the foundational data structure used to define features and their properties for the Howso Engine.
Feature attributes can be generated inferred automatically using :py:meth:`~howso.utilities.infer_feature_attributes`, but
users are encouraged to manually inspect the resulting attributes and make any necessary changes.

See the full definition of all feature attributes in the pages below.

.. toctree::
    :maxdepth: 2

    feature_attributes
