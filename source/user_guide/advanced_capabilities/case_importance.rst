.. currentmodule:: howso.engine

Case Importance
===============
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of using the Howso Engine to determine local case importance.

Objectives: what you will take away
-----------------------------------
- **Definitions & an understanding** of case importance and the situations in which they can be retrieved.

Prerequisites: before you begin
-------------------------------
- You've successfully :doc:`installed  Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.


Data
----
Our example dataset for this recipe is the well known ``Adult`` dataset. It is accessible via the `pmlb <https://github.com/EpistasisLab/pmlb>`__ package installed earlier. We use the ``fetch_data()`` function to retrieve the dataset in Step 1 below.


Concepts & Terminology
----------------------

- :ref:`case`
- :ref:`contribution`

How-To Guide
------------
Case importance is similar to feature importance in that it comprises of two metrics, case mean decrease in accuracy (MDA) and case contribution.
As opposed to influential and similar cases which examines the influence of cases on a single case or prediction, case importance examines how important a case is in regards to the overall predictions on a group of cases. Case importance share the same underlying methodology with  :doc:`Feature Importance <feature_importance>`.
Unlike feature contributions, case contributions are calculated just locally. Conceptually, local metrics use either a specific subset of the cases that are trained into the Trainee or a set of new cases.

Setup
^^^^^
The user guide assumes you have created and setup a :class:`~Trainee` as demonstrated in :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
The :class:`~Trainee` will be referenced as ``trainee`` in the sections below.

Case Contributions
^^^^^^^^^^^^^^^^^^

Case contributions can be retrieved by setting ``case_robust_prediction_contributions`` or ``case_full_prediction_contributions`` to ``True``.

.. code-block:: python

    details = {'case_robust_prediction_contributions': True}

Case MDA
^^^^^^^^
Case MDA can be retrieved by setting ``case_robust_accuracy_contributions`` or ``case_full_accuracy_contributions`` to ``True``.

.. code-block:: python

    details = {'case_robust_accuracy_contributions': True}


React
^^^^^
Since case importance is a local metric, cases or case indices must be provided as well as an action feature.


.. code-block:: python

    results = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
    )

Results
^^^^^^^
The results can be retrieved in the ``details`` section of the results.

.. code-block:: python

    case_contributions = pd.DataFrame(results['details']['case_contributions'][0])
    case_mda = pd.DataFrame(results['details']['case_mda'][0])


Complete Code
^^^^^^^^^^^^^
The code from all of the steps in this guide is combined below:

.. code-block:: python

    import pandas as pd
    from pmlb import fetch_data

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

    # import data
    df = fetch_data('adult')

    # Subsample the data to ensure the example runs quickly
    df = df.sample(1000)
    # Split out the last row for a prediction set and drop the Action Feature
    test_case = df.iloc[[-1]].copy()
    df.drop(df.index[-1], inplace=True)
    test_case = test_case.drop('target', axis=1)

    features = infer_feature_attributes(df)

    action_features = ['target']
    context_features = features.get_names(without=action_features)

    trainee = Trainee(features=features)

    trainee.train(df)

    trainee.analyze(context_features=context_features, action_features=action_features)

    details = {'case_robust_prediction_contributions': True}

    results = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=details
    )

    case_contributions = pd.DataFrame(results['details']['case_robust_prediction_contributions'][0])

API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
