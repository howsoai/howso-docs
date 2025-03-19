.. currentmodule:: howso.engine

Residuals
=========
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of using the Howso Engine to retrieve the :ref:`residual` s, which is the core measurement of error in Howso. Residuals play an important
   role in Howso, from determining uncertainties to gauging the accuracy of the predictions.

Objectives: what you will take away
-----------------------------------
- **How-To** Retrieve global and local residuals.

Prerequisites: before you begin
-------------------------------
- You've successfully :doc:`installed  Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.


Data
----
Our example dataset for this recipe is the well known ``Adult`` dataset. It is accessible via the `pmlb <https://github.com/EpistasisLab/pmlb>`__ package installed earlier. We use the ``fetch_data()`` function to retrieve the dataset in Step 1 below.


Concepts & Terminology
----------------------

- :ref:`residual`
- :ref:`robust`

How-To Guide
------------

Setup
^^^^^
The user guide assumes you have created and setup a :class:`~Trainee` as demonstrated in :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
The created :class:`~Trainee` will be referenced as ``trainee`` in the sections below.


Local Residuals
^^^^^^^^^^^^^^^

Local metrics are retrieved through using :py:meth:`Trainee.react`.
Both :ref:`robust` and non-robust (full) versions are available, although full
is recommended for residuals.

.. code-block:: python

    # Get local full residuals
    details = {'case_feature_residuals_full': True}
    results = trainee.react(
        df.iloc[[-1]],
        context_features=features.get_names(without=["target"]),
        action_features=["target"],
        details=details
    )

    residuals = results['details']['case_feature_residuals_full']
    print(residuals)


Global Residuals
^^^^^^^^^^^^^^^^

Howso has the ability to retrieve both :doc:`local vs global <../concepts//global_vs_local>` metrics.
Global metrics are retrieved through using :py:meth:`Trainee.react_aggregate`.  Both :ref:`robust` and non-robust (full) versions are also available.

.. code-block:: python

    # Get global full residuals
    residuals = trainee.react_aggregate(
        action_feature="target",
        details={'feature_residuals_full': True},
        residuals_hyperparameter_feature='',
    )
    print(residuals)


Complete Code
^^^^^^^^^^^^^
The code from all of the steps in this guide is combined below:

.. code-block:: python

    import pandas as pd
    from pmlb import fetch_data

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

    df = fetch_data('adult').sample(1_000)
    features = infer_feature_attributes(df)

    print(features.to_dataframe())

    trainee = Trainee(features=features)
    trainee.train(df)
    trainee.analyze()

    # Get local full residuals
    details = {'case_feature_residuals_full': True}
    results = trainee.react(
        df.iloc[[-1]],
        context_features=features.get_names(without=["target"]),
        action_features=["target"],
        details=details
    )

    residuals = results['details']['case_feature_residuals_full']
    print(residuals)

    # Get global full residuals
    residuals = trainee.react_aggregate(
        action_feature="target",
        details={'feature_residuals_full': True},
        residuals_hyperparameter_feature='',
    )
    print(residuals)


API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
- :py:meth:`Trainee.react_into_features`
- :py:meth:`Trainee.react_aggregate`
