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
The created :class:`~Trainee` will be referenced as ``trainee`` in the sections below. This guide also assumes you have installed the `pmlb` python library for the dataset used.

:ref:`familiarity_conviction`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two types of :ref:`familiarity_conviction` available, both accessible when :py:meth:`Trainee.react_into_features` is called.
``familiarity_conviction_addition`` is the familiarity conviction of adding the specified case and ``familiarity_conviction_removal`` is
the familiarity conviction of removing the specified case. :py:meth:`Trainee.react_into_features` stores these convictions which can be retrieved
through :py:meth:`Trainee.get_cases`

.. code-block:: python

    trainee.react_into_features(
        familiarity_conviction_addition=True,
        familiarity_conviction_removal=True
    )
    familiarity_conviction_addition = trainee.get_cases(
        session=trainee.active_session,
        features=[
            'familiarity_conviction_addition',
            'familiarity_conviction_removal'
        ]
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
        'feature_robust_residuals': True
    }

    results = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=details
    )

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
        familiarity_conviction_removal=True,
        similarity_conviction=True
    )

    familiarity_conviction_addition = trainee.get_cases(
        session=trainee.active_session,
        features=[
            'familiarity_conviction_addition',
            'familiarity_conviction_removal'
        ]
    )

    print(familiarity_conviction_addition)

    details = {
        'feature_robust_residuals': True,
        'similarity_conviction': True
    }

    results = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=details
    )
    print(results)

Below is an example of expected output from this sample code:

.. code-block:: bash

    $ python conviction_example.py 
        familiarity_conviction_addition  familiarity_conviction_removal
    0                            0.424315                        0.481610
    1                           24.344436                       24.373889
    2                            0.495148                        0.555847
    3                            0.463858                        0.523487
    4                            0.288355                        0.248439
    ...                               ...                             ...
    1994                         6.460913                        6.248667
    1995                        46.903956                       46.594968
    1996                         2.195260                        2.305391
    1997                        24.788612                       24.992936
    1998                         0.740464                        0.812168

    [1999 rows x 2 columns]
    target
    0       1
    {'action_features': ['target'],
    'feature_robust_residuals': [{'age': 8.888516681825308,
                                'capital-gain': 416.7392605164004,
                                'capital-loss': 59.906358535804515,
                                'education': 0.4523004291045252,
                                'education-num': 0.4655826176126248,
                                'fnlwgt': 65946.6678484109,
                                'hours-per-week': 6.298493661647657,
                                'marital-status': 0.512476275479471,
                                'native-country': 0.07145970131801563,
                                'occupation': 0.8772108612524578,
                                'race': 0.16017621174491645,
                                'relationship': 0.7104566198137716,
                                'sex': 0.3580994265834227,
                                'target': 0.09681983534852417,
                                'workclass': 0.18761097169888336}],
    'similarity_conviction': [0.9699384581322016]}

API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
- :py:meth:`Trainee.react_into_features`
- :py:meth:`Trainee.get_cases`
- :py:meth:`Trainee.active_session`
