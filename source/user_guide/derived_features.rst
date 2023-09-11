.. currentmodule:: howso.engine


Derived Features
================
.. topic:: What is covered in this user guide

    In this guide, you will learn the basics of derived features.  These features are not predicted or 
    generated directly, but are instead derived using the supplied code and values from other features.


Objectives: what you will take away
-----------------------------------
- **Definitions & Understanding** of how derived features work and how they can be used to accomplish novel
  tasks for both time-series and non time-series tasks
- **How-To** use derived features in and out of time-series workflows

Prerequisites
-------------
- You have successfully :doc:`installed Howso Engine <../getting_started/installing>`
- You have :doc:`loaded, configured, trained, and analyzed data <basic_workflow>`

Data
----
Our example dataset for this guide is the well-known ``Adult`` dataset, accessible via the ``pmlb`` package installed
in the prerequisites using the ``fetch_data()`` function.

Concepts & Terminology
----------------------
This guide will explain the concept of **derived features**, which include both **derived action features** and **derived context 
features**.  To follow along, you should be familiar with the following concepts:

- :ref:`Trainee <user_guide/terminology:trainee>`
- :ref:`React <user_guide/terminology:react>`
- :ref:`Case <user_guide/terminology:case>`
- :ref:`Feature <user_guide/terminology:feature>`
- :ref:`Action Features <user_guide/terminology:action features>`
- :ref:`Context Features <user_guide/terminology:context features>`
- :doc:`Feature Attributes <feature_attributes>`


Derived Feature Codes
^^^^^^^^^^^^^^^^^^^^^
The way in which each derived feature is derived is determined by what is called a **derived feature code**.  This is a snippet of 
`Amalgam <https://github.com/howsoai/amalgam>`_ -style code that determines how the derivation should be performed.  One such example 
of a derived feature code is:

.. code-block::
    (* #hours-per-week 0 52)


This would use the multiplication opcode (``*``) to derive a feature that is 52 times the ``"hours-per-week"`` feature for each case.  
For a full list of opcodes that are available for derived feature codes, refer to the :doc:`Amalgam Language Documentation <TODO>`.

.. note::
    
    When referencing feature values in a derived feature code (e.g., ``#hours-per-week 0``) the value returned is offset by the number 
    which follows the reference.  When not using a time-series Trainee, this value can only be 0.  If you are using a time-series Trainee, 
    however, this value can be larger which will then refer to that many cases previously in the time-series (e.g., ``#hours-per-week 1`` 
    would refer to the previous case in a time-series, if it were part of a time-series).


How-To Guide
------------
For this guide, we will add a feature called ``"hours-per-year"`` to the ``Adult`` dataset.  This dataset already contains a feature 
called ``"hours-per-week"``, so the relationship between the feature we have and the feature we want is mathematical in nature, and 
so should not be broken when making predictions.  Adding derived features to a :class:`~Trainee` can be done either before or after 
training.


Adding Derived Features Before Training
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To add a derived feature to a :class:`~Trainee` before training, simply modify the feature attributes:

.. code-block:: python
    
    features = infer_feature_attributes(df)
    hpy_features = {
        "type": "continuous",
        "auto_derive_on_train": True,
        "derived_feature_code": "(* #hours-per-week 0 52)"
    }
    features["hours-per-year"] = hpy_features
    t.train(df, features=features)
    t.analyze()


That's quite a lot of code, so let's break it down.  After inferring feature attributes, we set up the feature attributes for our derived feature.

.. code-block:: python

    hpy_features = {
        "type": "continuous",
        "auto_derive_on_train": True,
        "derived_feature_code": "(* #hours-per-week 0 52)"
    }

First, we note that this feature is continuous.  Second, we set this feature to be auto-derived on train.  This means that the feature will be computed 
using its derived feature code as soon as cases are trained into the model.  If we did not do this, we would have to manually specify it in the ``derived_features`` 
parameter to :meth:`Trainee.train` to ensure that the feature is created by the :class:`~Trainee`.  Finally, we set the derived feature code.  This is a 
small piece of Amalgam-like code which determines how to derive the feature.  In this case, we use the multiplication opcode (``*``) to multiply each case's 
value of hours-per-week (``#hours-per-week 0``, where the 0 is an offset and means the current case) by 52, the number of weeks in a year.


Adding Derived Features After Training
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The process of adding a derived feature to a :class:`~Trainee` that has already been trained is quite simple.  It can be handled with a single call to 
:meth:`Trainee.add_feature`:

.. code-block:: python

    # t has already been trained and analyzed
    hpy_features = {
        "type": "continuous",
        "auto_derive_on_train": True,
        "derived_feature_code": "(* #hours-per-week 0 52)"
    }
    t.add_feature("hours-per-year", feature_attributes=hpy_features)


Using Derived Features in Reacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Once a model has one or more derived features, they can be used in reacts:

.. code-block:: python
    :caption: Using a derived feature as an action feature

    reaction = t.react(
        contexts=df[t.features.get_names(without=["hours-per-week", "hours-per-year"])],
        action_features=["hours-per-week", "hours-per-year"],
        derived_action_features=["hours-per-year"],
    )
    print(reaction["action"])


.. code-block:: python
    :caption: Using a derived feature as a context feature

    reaction = t.react(
        contexts=df[t.features.get_names(without=["target"])],
        derived_context_features=["hours-per-year"],
        action_features=["target"]
    )
    print(reaction["action"])


Note that both ``derived_action_features`` and ``derived_context_features`` must be a subset of ``action_features`` and ``context_features``, respectively.  
A derived context feature is derived from the contexts that are being input to a :meth:`~Trainee.react`, while a derived action feature is derived from the 
actions that are output from a :meth:`~Trainee.react`.


Derived Features for Time-Series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Derived features are used in time-series :class:`~Trainee` s and are automatically created by :func:`~howso.utilities.infer_feature_attributes` when the 
``time_feature_name`` and ``id_feature_name`` parameters are supplied.  When :meth:`Trainee.react_series` is used, the lag features are used as derived 
context features and the delta/rate features are used as derived action features.  Since :meth:`Trainee.react` supports more explainability details than 
:meth:`Trainee.react_series`, this can be useful to replicate the behavior of :meth:`~Trainee.react_series` using :meth:`~Trainee.react`.

For more information on time-series, see the API Reference and the :doc:`time-series user guide <time_series>`


API References
--------------

- :func:`howso.utilities.infer_feature_attributes`
- :meth:`Trainee.react`
- :meth:`Trainee.react_series`

