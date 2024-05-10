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

Local metrics are retrieved through using :py:meth:`Trainee.react`. Both :ref:`robust` and non-robust versions are available.

.. code-block:: python


    # Get robust residuals
    details = {'robust_residuals': True}

    results = t.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=details
    )

    residuals = results['details']['robust_residuals']



Global Residuals
^^^^^^^^^^^^^^^^

Howso has the ability to retrieve both :doc:`local vs global <../concepts//global_vs_local>` metrics.  
Global metrics are retrieved through using :py:meth:`Trainee.react_into_trainee`.  Both :ref:`robust` and non-robust versions are also available.
For global residuals, they are retrieved by selecting the mean absolute error, ``mae``, stat in :py:meth:`Trainee.get_prediction_stats`.

.. code-block:: python

    t.react_into_trainee(
        context_features=context_features,
        action_feature=action_features[0],
        residuals_robust=True
    )
    residuals = t.get_prediction_stats(
        action_feature=action_features[0],
        stats=['mae']
    )


Complete Code
^^^^^^^^^^^^^
The code from all of the steps in this guide is combined below:

.. code-block:: python

    from pmlb import fetch_data

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

    # import data
    df = fetch_data('adult')

    # Subsample the data to ensure the example runs quickly
    df = df.sample(1001)
    # Split out the last row for a test case and drop the Action Feature
    test_case = df.iloc[[-1]].copy()
    df.drop(df.index[-1], inplace=True)
    test_case = test_case.drop('target', axis=1)


    features = infer_feature_attributes(df)

    action_features = ['target']
    context_features = features.get_names(without=action_features)

    trainee = Trainee(features=features)

    trainee.train(df)

    trainee.analyze(context_features=context_features, action_features=action_features)

    # Get local robust residuals
    details = {
        'robust_residuals': True,
        'feature_residuals': True
    }

    results = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=details
    )

    residuals = results['details']['feature_residuals']

    # Get global robust residuals
    trainee.react_into_trainee(
        context_features=context_features,
        action_feature=action_features[0],
        residuals_robust=True
    )
    residuals = trainee.get_prediction_stats(
        action_feature=action_features[0],
        stats=['mae']
    )

API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
- :py:meth:`Trainee.react_into_features`
- :py:meth:`Trainee.get_prediction_stats`
