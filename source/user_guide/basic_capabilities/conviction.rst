.. currentmodule:: howso.engine

Conviction
==========
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of using the Howso Engine to retrieve the :ref:`conviction` metrics.

Objectives: what you will take away
-----------------------------------
- **How-To** retrieve familiarity, similarity, and prediction residual conviction metrics.

Prerequisites: before you begin
-------------------------------
- You've successfully :doc:`installed  Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.


Data
----
Our example dataset for this recipe is the well known ``Adult`` dataset. It is accessible via the `pmlb <https://github.com/EpistasisLab/pmlb>`__ package installed earlier. We use the ``fetch_data()`` function to retrieve the dataset in Step 1 below.


Concepts & Terminology
----------------------

- :ref:`conviction`
- :ref:`familiarity_conviction`
- :ref:`similarity_conviction`
- :ref:`prediction_residual_conviction`


How-To Guide
------------

:ref:`familiarity_conviction` and :ref:`similarity_conviction` are measurements of how surprising a case is. This can be useful for tasks such as anomaly detection.
:ref:`prediction_residual_conviction` can be used to drill down into a specific case and examine its features. It measures how surprising each cases feature values is, thus
it can reveal information such as why a case was anomalous. For example, if a NBA player's height was 3 foot tall, that value would be very surprising since most NBA players are very tall.

Setup
^^^^^
The user guide assumes you have created and setup a :class:`~Trainee` as demonstrated in :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
The created :class:`~Trainee` will be referenced as ``trainee`` in the sections below.

:ref:`familiarity_conviction`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two types of :ref:`familiarity_conviction` available, both accessible when :py:meth:`Trainee.react_into_features` is called.
``familiarity_conviction_addition`` is the familiarity conviction of adding the specified case and ``familiarity_conviction_removal`` is
the familiarity conviction of removing the specified case. :py:meth:`Trainee.react_into_features` stores these convictions which can be retrieved
through :py:meth:`Trainee.get_cases`

.. code-block:: python

    trainee.react_into_features(
        familiarity_conviction_addition=True,
        familiarity_conviction_remove=True
    )
    familiarity_conviction_addition = trainee.get_cases(
        session=trainee.active_session,
        features=['familiarity_conviction_addition', 'familiarity_conviction_removal']
    )

:ref:`similarity_conviction`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`similarity_conviction` is a singular metric that is also accessible when :py:meth:`Trainee.react_into_features` is called.

.. code-block:: python

    trainee.react_into_features(similarity_conviction = True)
    familiarity_conviction_addition = trainee.get_cases(
        session=trainee.active_session,
        features=['similarity_conviction']
    )

:ref:`prediction_residual_conviction`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since :ref:`prediction_residual_conviction` details the conviction around a prediction, this is retrieved by specifying
specific cases in :py:meth:`Trainee.react`

.. code-block:: python

    details = {
        'global_case_feature_residual_convictions_robust': True,
        'local_case_feature_residual_convictions_robust': True
    }

    # React to get the details of each case
    results = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=Details
    )

    # Extract the global and local case feature residual convictions
    global_case_feature_residual_convictions = pd.DataFrame(
        results['details']['global_case_feature_residual_convictions_robust'])[df.columns.tolist()]
    local_case_feature_residual_convictions = pd.DataFrame(
        results['details']['local_case_feature_residual_convictions_robust'])[df.columns.tolist()]

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
    df = df.sample(2000)
    test_case = df.iloc[[-1]].copy()
    df.drop(df.index[-1], inplace=True)

    features = infer_feature_attributes(df)

    action_features = ['target']
    context_features = features.get_names(without=action_features)

     trainee = Trainee(features=features)

    trainee.train(df)

    trainee.analyze(context_features=context_features, action_features=action_features)

    trainee.react_into_features(
        familiarity_conviction_addition=True,
        familiarity_conviction_remove=True,
        similarity_conviction = True
    )

    convictions = trainee.get_cases(
        session=trainee.active_session,
        features=[
            'familiarity_conviction_addition',
            'familiarity_conviction_removal',
            'similarity_conviction'
        ]
    )

    details = {
        'global_case_feature_residual_convictions_robust': True,
        'local_case_feature_residual_convictions_robust': True
    }

    results = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=details
    )

    local_case_feature_residual_convictions = pd.DataFrame(
        results['details']['local_case_feature_residual_convictions_robust'])


API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
- :py:meth:`Trainee.react_into_features`
- :py:meth:`Trainee.get_cases`
- :py:meth:`Trainee.active_session`
