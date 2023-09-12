.. currentmodule:: howso.engine


JSON/YAML as Features
=====================
.. topic:: What is covered in this user guide

    In this guide, you will learn the basics of using JSON/YAML as features in your :class:`~Trainee` s.


Objectives
----------
- **Definitions & Understanding** of what JSON (JavaScript Object Notation) and YAML (Yet Another Markup 
  Language) features are and how they can be used.


Prerequisites
-------------
- You have successfully :doc:`installed Howso Engine <../getting_started/installing>`
- You have :doc:`loaded, configured, trained, and analyzed data <basic_workflow>`


Notebook Recipe
---------------
This user guide has its content outlined in the 
`JSON as a Feature Notebook <https://github.com/howsoai/howso-engine-recipes/blob/main/1-engine-intro.ipynb>`_


Concepts & Terminology
----------------------
This guide focuses primarily on the concept of JSON/YAML objects as features.  We additionally recommend 
being familiar with the following concepts:

- :ref:`Trainee <user_guide/terminology:trainee>`
- :ref:`React <user_guide/terminology:react>`
- :ref:`Case <user_guide/terminology:case>`
- :ref:`Feature <user_guide/terminology:feature>`
- :ref:`Action Features <user_guide/terminology:action features>`
- :ref:`Context Features <user_guide/terminology:context features>`
- :doc:`Feature Attributes <feature_attributes>`


How-To Guide
------------
Howso Engine can accept JSON and YAML objects as feature values, treating them like any other feature.  This can allow 
more complex objects to be represented than just numbers or strings.


Declaring a Feature as JSON/YAML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When calling :func:`howso.utilities.infer_feature_attributes`, a feature can be declared as JSON or YAML by setting 
its ``data_type`` attribute.

.. code-block:: python
    :caption: Replace ``"json"`` with ``"yaml"`` to use YAML for your feature.

    features = infer_feature_attributes(
        data,
        features={"inventory": {"type": "continuous", "data_type": "json"}}
    )

Note that the feature's ``type`` attribute is set normally to either ``"continuous"`` or ``"nominal"``.  For ones 
marked as continuous, distance will be computed using a form of edit distance.  Otherwise, the normal nominal distance 
computation is used.

Once a feature is set as JSON properly, it can be used as if it were any other feature.


Reacting to JSON/YAML Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Below are a few code snippets that show how JSON/YAML features can be used in a react:

.. code-block:: python
    :caption: Using `level` and `class`, predict `inventory` (a JSON feature).

    t.react(
        contexts=[[15, "Warlock"]], context_features=["level", "class"],
        action_features=["inventory"],
    )


.. code-block:: python
    :caption: Using `level` and `class`, generate `inventory` (a JSON feature).

    t.react(
        contexts=[[15, "Warlock"]], context_features=["level", "class"],
        action_features=["inventory"],
        desired_conviction=25,
    )


.. code-block:: python
    :caption: Using `inventory` (a JSON feature) and `level`, predict `class`.

    t.react(
        contexts=[["{\"sword\": 1, \"lute\": 1, \"potion\": 2}", 15]],
        context_features=["inventory", "level"],
        action_features=["class"],
    )

.. note::
    Note that, in the above example, the entire JSON is contained within a string and contained quotes within that are 
    escaped.


API References
--------------
- :func:`howso.utilities.infer_feature_attributes`
- :func:`Trainee.react`

