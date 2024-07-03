.. currentmodule:: howso.engine


Feature Importance
==================
.. topic:: What is covered in this user guide

    In this guide, you will learn how to compute the feature importance metrics, :ref:`Feature Contributions <contribution>` and :ref:`Feature Mean Decrease in Accuracy (MDA) <mda>` from a Trainee. Feature importance metrics
    provides information about which features are useful for predicting a target or :ref:`action <action_features>` feature. In addition to learning informative metrics about the data and the model, these insights can be used as guidance for further action such as feature selection or feature engineering.


Objectives: what you will take away
-----------------------------------
- **How-To** Retrieve the different types of feature importance metrics across several different categories: :doc:`global vs local <../concepts/global_vs_local>`, and :ref:`robust` vs non-robust (full) :ref:`Feature Contributions <contribution>` and :ref:`Feature MDA <mda>`.


Prerequisites: before you begin
-------------------------------
- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.

Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover and go into some additional functionality:

- :download:`Feature Importance <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/2-Workflows/feature_importance/feature_importance.ipynb>`

Concepts & Terminology
----------------------
The main piece of terminology this guide introduces is the concept of Feature Importance. To understand this, we
recommend being familiar with the following concepts:

- :ref:`residual`
- :ref:`robust`
- :ref:`contribution`
- :ref:`mda`

The two metrics available for feature importance is feature :ref:`contribution` and feature :ref:`mda`.

Robust vs Non-Robust (Full)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
:ref:`robust` metrics are recommended as they use a greater variety of feature combinations, and they include a calculation performance boost as the number of features increases.

How-To Guide
------------

Setup
^^^^^
The user guide assumes you have created and setup a :class:`~Trainee` as demonstrated in :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
The created :class:`~Trainee` will be referenced as ``trainee`` in the sections below.

Global Feature Importance
^^^^^^^^^^^^^^^^^^^^^^^^^
To get global feature importance metrics, :py:meth:`Trainee.react_aggregate`, is called on a trained and analyzed Trainee. :py:meth:`Trainee.react_aggregate` calls react internally on the cases already trained into the Trainee and calculates the metrics. In this method, the desired metrics can be selected as parameters. These parameters are named individually
in the ``details`` parameter and setting them to ``True`` will calculate and return the desired metrics. For example, ``feature_mda_robust`` and ``feature_contributions_robust`` will calculate the robust versions of MDA and Feature Contributions, while ``feature_mda_full`` and ``feature_contributions_full`` will calculate the non-robust (full) versions.
An action feature must be specified. ``feature_influences_action_feature`` is recommended for feature influence metrics such as feature contributions and mda, especially when used in conjuction with retrieving prediction stats, however, ``action_feature`` can be also used as well. ``action_feature`` sets the action feature for both influence metrics and prediction stats. Since often
only the influence metrics's action feature is intended to be set, ``feature_influences_action_feature`` provides a more precise parameter.

.. code-block:: python

    feature_contributions_robust = trainee.react_aggregate(
        context_features=context_features,
        feature_influences_action_feature=action_features[0],
        details={'feature_contributions_robust' : True}
    )

    feature_mda_robust = trainee.react_aggregate(
        context_features=context_features,
        feature_influences_action_feature=action_features[0],
        details={'feature_mda_robust': True}
    )

Local Feature Importance
^^^^^^^^^^^^^^^^^^^^^^^^
To get local feature importance metrics, :py:meth:`Trainee.react`, is first called on a trained and analyzed Trainee. In this method, the desired metrics, ``feature_contributions_robust`` and ``feature_mda_robust``, can be selected as inputs to the ``details`` parameters as key value pairs from a dictionary. These parameters are named individually
and setting them to ``True`` will calculate the desired metrics. Robust calculations are performed by default.

.. code-block:: python

    details = {
        'feature_contributions_robust':True,
        'feature_mda_robust':True,
    }

    results = trainee.react(
        df,
        context_features=context_features,
        action_features=action_features,
        details=details
    )

In order to retrieve the calculated stats, they can be retrieved from the :py:meth:`Trainee.react` output dictionary. They are stored under the ``explanation`` key under the name of the metric. Whether these metrics are :ref:`robust` or non-robust (full) is determined when the metrics
are calculated in :py:meth:`Trainee.react` from the previous step.

.. code-block:: python

    feature_contributions_robust = results['explanation']['feature_contributions_robust']
    feature_mda_robust = results['explanation']['feature_mda_robust']


.. warning::

    Contributions and MDA are also metrics for cases and not just features, so please be aware when reading other guides that may use those terms.

Contribution and MDA matrices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Howso also provides the two metrics in a matrix view, where for each row which represent the action feature, you can identify the contributions of all
the other context features to that prediction. Since these matrices may not be symmetrical, examining the differences between the upper and lower triangular matrices
may reveal additional insights. Please see the linked recipe for more information.

:meth:`Trainee.get_contribution_matrix` and :meth:`Trainee.get_mda_matrix` gets these matrices respectively.

.. warning::

    Matrices may be computationally expensive.

.. code-block:: python

    contrib_matrix = trainee.get_contribution_matrix()
    mda_matrix = trainee.get_mda_matrix()

Combined Code
^^^^^^^^^^^^^

.. code-block:: python

    import pandas as pd
    from pmlb import fetch_data

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

    df = fetch_data('adult', local_cache_dir="data/adult")

    # Subsample the data to ensure the example runs quickly
    df = df.sample(1000, random_state=0).reset_index(drop=True)

    # Split out the last row for a prediction set and drop the Action Feature
    test_case = df.iloc[[-1]].copy()
    df.drop(df.index[-1], inplace=True)

    # Auto detect features
    features = infer_feature_attributes(df)

    # Specify Context and Action Features
    action_features = ['target']
    context_features = features.get_names(without=action_features)

    # Create a new Trainee, specify features
     trainee = Trainee(features=features)

    # Train and analyze
    trainee.train(df)
    trainee.analyze()

    feature_contributions_robust = trainee.react_aggregate(
        context_features=context_features,
        feature_influences_action_feature=action_features[0],
        details={"feature_contributions_robust" : True}
    )

    feature_mda_robust = trainee.react_aggregate(
        context_features=context_features,
        feature_influences_action_feature=action_features[0],
        details={"feature_mda_robust" : True}
    )

    details = {
        'feature_contributions_robust':True,
        'feature_mda_robust':True,
    }

    results = trainee.react(
        df,
        context_features=context_features,
        action_features=action_features,
        details=details
    )

    feature_contributions_robust = results['explanation']['feature_contributions_robust']
    feature_mda_robust = results['explanation']['feature_mda_robust']

    contrib_matrix = trainee.get_contribution_matrix()
    mda_matrix = trainee.get_mda_matrix()


API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
- :py:meth:`Trainee.react_aggregate`
- :py:meth:`Trainee.get_contribution_matrix`
- :py:meth:`Trainee.get_mda_matrix`

