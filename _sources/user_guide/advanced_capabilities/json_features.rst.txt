.. currentmodule:: howso.engine


JSON/YAML as Features
=====================
.. topic:: What is covered in this user guide

    In this guide, you will learn the basics of using JSON/YAML as features in your :class:`~Trainee` s.

.. warning::

    JSOM/YAML tools are still in beta development. Please note that while the core features are in place, they are still under development and thus you may encounter bugs or unexpected behavior.
    If you have any feedback, please share your thoughts at `support@howso.com <support@howso.com>`_. 

Objectives
----------
- **Definitions & Understanding** of what JSON (JavaScript Object Notation) and YAML (Yet Another Markup
  Language) features are and how they can be used.


Prerequisites
-------------
- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.

Notebook Recipe
---------------
This user guide has its content outlined in the
`JSON as a Feature Notebook <https://github.com/howsoai/howso-engine-recipes/blob/main/1-engine-intro.ipynb>`_


Concepts & Terminology
----------------------
This guide focuses primarily on the concept of JSON/YAML objects as features.  We additionally recommend
being familiar with the following concepts:

- :ref:`trainee`
- :ref:`react`
- :ref:`case`
- :ref:`feature`
- :ref:`action_features`
- :ref:`context_features`
- :doc:`Feature Attributes <../basics/feature_attributes>`


How-To Guide
------------
Howso Engine can accept JSON and YAML objects as feature values, treating them like any other feature.  This can allow
more complex objects to be represented than just numbers or strings.

Data
----

We use a small, toy-dataset to demonstrate this functionality where each case represents a character in a game.

.. code-block:: python

    data = pd.DataFrame([
        {"name": "Nerissa", "level": 14, "class": "Fighter", "inventory": "{\"saddle\": 1, \"trident\": 2, \"potion\": 5}"},
        {"name": "Maaya", "level": 13, "class": "Warlock", "inventory": "{\"sword\": 1, \"lute\": 1, \"potion\": 2}"},
        {"name": "Taxuul", "level": 15, "class": "Cleric", "inventory": "{\"hammer\": 1, \"metal bar\": 20, \"potion\": 1}"},
    ])


Declaring a Feature as JSON/YAML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When calling :py:meth:`~howso.utilities.infer_feature_attributes`, a feature can be declared as JSON or YAML by setting
its ``data_type`` attribute.

.. code-block:: python
    :caption: Replace ``"json"`` with ``"yaml"`` to use YAML for your feature.

    features = infer_../basics/feature_attributes(
        data,
        features={"inventory": {"type": "continuous", "data_type": "json"}}
    )

Note that the feature's ``type`` attribute is set normally to either ``"continuous"`` or ``"nominal"``.  For ones
marked as continuous, distance will be computed using a form of edit distance.  Otherwise, the normal nominal distance
computation is used.

Once a feature is set as JSON properly, it can be used as if it were any other feature.


Discriminative Reacts to JSON/YAML Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Below are a few code snippets that show how JSON/YAML features can be used in a discriminative react:

.. code-block:: python
    :caption: Using ``level`` and ``class``, predict ``inventory`` (a JSON feature).

    t.react(
        contexts=[[15, "Warlock"]], context_features=["level", "class"],
        action_features=["inventory"],
    )


.. code-block:: python
    :caption: Using ``level`` and ``class``, generate ``inventory`` (a JSON feature).

    t.react(
        contexts=[[15, "Warlock"]], context_features=["level", "class"],
        action_features=["inventory"],
        desired_conviction=25,
    )


.. code-block:: python
    :caption: Using ``inventory`` (a JSON feature) and ``level``, predict ``class``.

    t.react(
        contexts=[["{\"sword\": 1, \"lute\": 1, \"potion\": 2}", 15]],
        context_features=["inventory", "level"],
        action_features=["class"],
    )

.. note::
    Note that, in the above example, the entire JSON is contained within a string and contained quotes within that are
    escaped.

Generative Reacts to JSON/YAML Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We can also use a generative  :py:meth:`Trainee.react` to generate any number of more or less surprising inventories. We will do this generative  :py:meth:`Trainee.react` with 
differing levels of desired conviction to show more and less surprising examples.

With higher desired conviction, we will see JSON that more closely resembles the training data.

.. code-block:: python
    :caption: Using ``class`` and ``level``, predict ``inventory`` (a JSON feature).

    generative_reaction_25 = t.react(
        contexts=[[15, "Warlock"]], context_features=["level", "class"],
        action_features=["inventory"],
        desired_conviction=25,
        num_cases_to_generate=5,
    )["action"]

    generative_reaction_25.loc[:, "inventory"]

When the ``desired_conviction`` is low, we we may see completely new strings or data types associated with JSON keys that already exist in the dataset. While this isn't a bug, this demonstrates some of the behavior that can be expected when using JSON as a feature especially in generative output from the Howso Engine.

Complete Code
-------------
.. code-block:: python

    import pandas as pd

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

    data = pd.DataFrame([
        {"name": "Nerissa", "level": 14, "class": "Fighter", "inventory": "{\"saddle\": 1, \"trident\": 2, \"potion\": 5}"},
        {"name": "Maaya", "level": 13, "class": "Warlock", "inventory": "{\"sword\": 1, \"lute\": 1, \"potion\": 2}"},
        {"name": "Taxuul", "level": 15, "class": "Cleric", "inventory": "{\"hammer\": 1, \"metal bar\": 20, \"potion\": 1}"},
    ])

    features = infer_feature_attributes(data)

    t = Trainee(features=features)
    t.train(data)
    t.analyze()

    discriminative_action = t.react(
        contexts=[[15, "Warlock"]], context_features=["level", "class"],
        action_features=["inventory"],
    )["action"]

    discriminative_action.loc[:, "inventory"]

    generative_reaction_25 = t.react(
        contexts=[[15, "Warlock"]], context_features=["level", "class"],
        action_features=["inventory"],
        desired_conviction=25,
        num_cases_to_generate=5,
    )["action"]

    generative_reaction_25.loc[:, "inventory"]

    t.delete()

API References
--------------
- :py:meth:`~howso.utilities.infer_feature_attributes`
- :py:meth:`Trainee.react`

