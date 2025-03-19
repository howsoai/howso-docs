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

:ref:`familiarity_conviction` and :ref:`similarity_conviction` are measurements of how surprising a case is. 
This can be useful for tasks such as anomaly detection. :ref:`prediction_residual_conviction` can be used to 
drill down into a specific case and examine its features. It measures how surprising each cases feature values is, thus
it can reveal information such as why a case was anomalous. For example, if a NBA player's height was 3 foot tall, that 
value would be very surprising since most NBA players are very tall.

Setup
^^^^^
The user guide assumes you have created and setup a :class:`~Trainee` as demonstrated in :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
The created :class:`~Trainee` will be referenced as ``trainee`` in the sections below. This guide also assumes you have installed the `pmlb` python library for the dataset used.

:ref:`familiarity_conviction`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two types of :ref:`familiarity_conviction` available, both accessible when
:py:meth:`Trainee.react_into_features` is called.  ``familiarity_conviction_addition`` 
is the familiarity conviction of adding the specified case and ``familiarity_conviction_removal`` is 
the familiarity conviction of removing the specified case. :py:meth:`Trainee.react_into_features` 
stores these convictions which can be retrieved through :py:meth:`Trainee.get_cases`

.. code-block:: python

    trainee.react_into_features(
        familiarity_conviction_addition=True,
        familiarity_conviction_removal=True
    )
    familiarity_conviction = trainee.get_cases(
        session=trainee.active_session,
        features=[
            'familiarity_conviction_addition',
            'familiarity_conviction_removal'
        ]
    )


:ref:`similarity_conviction`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`similarity_conviction` is a singular metric that is also accessible when
:py:meth:`Trainee.react_into_features` is called.

.. code-block:: python

    trainee.react_into_features(similarity_conviction=True)
    saimilarity_conviction = trainee.get_cases(
        session=trainee.active_session,
        features=['similarity_conviction']
    )


:ref:`residual_conviction`
^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`residual_conviction` is accessed through :py:meth:`Trainee.react` and measures how noisy a feature is relative 
to the expected level of noise for that feature.

.. code-block:: python

    details = {'feature_full_residual_convictions_for_case': True}
    session_training_indices = trainee.get_session_training_indices(trainee.active_session)
    session_training_indices = [(trainee.active_session.id, session_training_indices[0])]
    reaction = trainee.react(
        case_indices=session_training_indices,
        preserve_feature_values=features.get_names(),
        details=details,
    )
    residual_conviction = reaction["details"]["feature_full_residual_convictions_for_case"]


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

   trainee.react_into_features(
        familiarity_conviction_addition=True,
        familiarity_conviction_removal=True
    )
    familiarity_conviction = trainee.get_cases(
        session=trainee.active_session,
        features=[
            'familiarity_conviction_addition',
            'familiarity_conviction_removal'
        ]
    )
    print(familiarity_conviction)

    trainee.react_into_features(similarity_conviction=True)
    similarity_conviction = trainee.get_cases(
        session=trainee.active_session,
        features=['similarity_conviction']
    )
    print(similarity_conviction)

    details = {'feature_full_residual_convictions_for_case': True}
    session_training_indices = trainee.get_session_training_indices(trainee.active_session)
    session_training_indices = [(trainee.active_session.id, session_training_indices[0])]
    reaction = trainee.react(
        case_indices=session_training_indices,
        preserve_feature_values=features.get_names(),
        details=details,
    )
    residual_conviction = reaction["details"]["feature_full_residual_convictions_for_case"]


Below is an example of expected output from this sample code:

.. code-block:: bash

    $ python conviction_example.py 
                        type decimal_places bounds  ... data_type original_type     
                                                min  ...               data_type size
    age             continuous              0    0.0  ...    number       numeric    8
    workclass          nominal              0    NaN  ...    number       integer    8
    fnlwgt          continuous              0    0.0  ...    number       numeric    8
    education          nominal              0    NaN  ...    number       integer    8
    education-num   continuous              0    0.0  ...    number       numeric    8
    marital-status     nominal              0    NaN  ...    number       integer    8
    occupation         nominal              0    NaN  ...    number       integer    8
    relationship       nominal              0    NaN  ...    number       integer    8
    race               nominal              0    NaN  ...    number       integer    8
    sex                nominal              0    NaN  ...    number       integer    8
    capital-gain    continuous              0    0.0  ...    number       numeric    8
    capital-loss    continuous              0    0.0  ...    number       numeric    8
    hours-per-week  continuous              0    0.0  ...    number       numeric    8
    native-country     nominal              0    NaN  ...    number       integer    8
    target             nominal              0    NaN  ...    number       integer    8

    [15 rows x 10 columns]
        familiarity_conviction_addition  familiarity_conviction_removal
    0                           2.036422                        1.424936
    1                           7.239347                        6.785857
    2                           0.796667                        1.103851
    3                           0.499284                        0.293830
    4                           0.486247                        0.727024
    ..                               ...                             ...
    995                         3.315124                        3.537327
    996                         2.741911                        1.970860
    997                       133.074640                      118.813386
    998                         8.028792                        7.916007
    999                         0.691341                        0.819138

    [1000 rows x 2 columns]
        similarity_conviction
    0                 0.294567
    1                 0.561961
    2                 3.656589
    3                 0.326939
    4                 1.786323
    ..                     ...
    995               0.496362
    996               0.504448
    997               0.612071
    998               0.960858
    999               1.065963

    [1000 rows x 1 columns]
    [{'marital-status': 1.2677661102272322, 'race': 268.342074, 'target': 2.106858563940631, 'fnlwgt': 3.3412368323793595, 'education': 1, 'age': 0.6401583699403189, 'education-num': 1, 'sex': 1.3191579118090324, 'occupation': 1.4279943800852224, 'capital-loss': 1016.0995061247426, 'relationship': 1.6248012684002686, 'workclass': 0.218840321217643, 'hours-per-week': 0.7026121145303584, 'capital-gain': 2.528308627762195, 'native-country': 2.4681265907924397}]


API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
- :py:meth:`Trainee.react_into_features`
- :py:meth:`Trainee.get_cases`
- :py:meth:`Trainee.active_session`
