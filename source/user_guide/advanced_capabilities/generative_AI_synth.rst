.. currentmodule:: howso.engine

Generative Output and Data Synthesis
====================================
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of using the Howso Engine for obtaining **generative output** and performing **data synthesis**.

Objectives: what you will take away
-----------------------------------

- **Definitions & an understanding** of the Howso Engine's underlying instance-based learning (IBL) technology, which enables its generative capabilities.
- **How-To** perform generative analysis and generate synthetic data using Engine.

Prerequisites: before you begin
-------------------------------
**Installation**

- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.

Concepts & Terminology
----------------------

- *How does Engine's underlying IBL technology make it capable of generative output?*

  Engine is rooted in instance-based learning (IBL), which stores instances, i.e., data points, in memory and makes predictions about new instances
  given their relationships to existing instances. Engine’s IBL algorithm is based on the principles of “nearest neighbors”, which makes
  inferences about a data point given its relationship to the points to which it is closest in space. Thus, given a new data point, Engine dynamically identifies
  the region of original data with the most influence on the new point. These points will have the highest likelihood of representing the same information as the
  new point, and information about the new data point can be inferred from its neighbors.

  This underlying inference algorithm also enables Engine to do both discriminative and generative predictions. **Discriminative** analysis utilizes the maximum
  likelihood estimate (MLE) to make predictions. In contrast, **generative** analysis samples a prediction from the likelihood distribution.

- *How does conviction enable Engine's generative AI capabilities?*

  Conviction is a computed ratio of the expected surprisal to actual surprisal.
  Conviction is often used when making predictions to determine how closely a
  prediction for a new data point should adhere to the original data. A
  defining feature of Engine is that it utilizes the concept of conviction to
  condition its sample from the likelihood distribution to be more or less
  unusual (or surprising) during generative analysis. Conviction translates
  well into generative space, and defines how similar a new point proposed by
  Engine should be to the original data. For example, using conviction, Engine
  can generate points that are more surprising, i.e., different, than the
  original data, and vice versa.

- *What is a common use case for Engine's generative AI capabilities?*

  Synthetic Data Generation: Propose new data points that follow the patterns of your original data, but are completely distinct. Use conviction to tune how similar or dissimilar the
  synthetic data is from your original data.

How-To Guide
------------
Here, we will review the basic steps need to obtain generative output and for
creating synthetic data.

Setup
^^^^^
The user guide assumes you have create and setup a - :py:class:`~Trainee` as demonstrated in :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
The :py:class:`~Trainee` will be referenced as ``trainee`` in the sections below.


Generative Output
^^^^^^^^^^^^^^^^^
This code is designed to make a generative prediction on a test case. This is
very similar to making a discriminative prediction, except the
``desired_conviction`` is set. After building, training, and analyzing a
:class:`~Trainee`, you can obtain the generative
prediction for a test case in a :py:meth:`Trainee.react` call.

.. code-block:: python

    # Perform generative react
    result =  trainee.react(
      contexts=test_case[context_features],
      context_features=context_features,
      action_features=action_feature,
      desired_conviction = 10 # Needed for generative analysis
    )

    # Obtain result
    result['action']


Example - Creating Synthetic Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Synthetic data is very similar to Task 1, but uses targetless analysis.
Additionally, you will set two new parameters ``generate_new_cases``, which
indicates whether a completely new case is or is not generated, and
``num_cases_to_generate``, which indicates the number of synthetic cases you will
create.

.. code-block:: python

    # Targetless Analysis
    t.analyze()

    # Synthesize
    synth = t.react(
      action_features=df.columns.tolist(), # What features to generate? In this case, the same features as the original data
      desired_conviction=10, # Set at synthesizer's default desired conviction value
      generate_new_cases='always', # Indicates that we always want to create entirely new cases from the original data
      num_cases_to_generate=len(df) # Number of new points to generate? In this case, the same number as the original data
    )

    # Print out synthetic dataset
    synthetic_data = synth['action']
    synthetic_data

Complete Code
^^^^^^^^^^^^^

.. code-block:: python

    import pandas as pd
    from pmlb import fetch_data

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

    # import data
    df = fetch_data('adult')

    # Subsample the data to ensure the example runs quickly
    df = df.sample(1000)
    test_case = df.iloc[[-1]].copy()
    df.drop(df.index[-1], inplace=True)

    features = infer_feature_attributes(df)

    action_features = ['target']
    context_features = features.get_names(without=action_features)

    trainee = Trainee(features=features)

    trainee.train(df)

    # Targetless Analysis
    trainee.analyze()

    # Perform generative react
    result = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        desired_conviction = 10 # Needed for generative analysis
    )

    # Obtain result
    generative_result = result['action']

    # Synthesize
    synth = trainee.react(
        action_features=df.columns.tolist(), # What features to generate? In this case, the same features as the original data
        desired_conviction=10, # Set at synthesizer's default desired conviction value
        generate_new_cases='always', # Indicates that we always want to create entirely new cases from the original data
        num_cases_to_generate=len(df) # Number of new points to generate? In this case, the same number as the original data
    )

    # Print out synthetic dataset
    synthetic_data = synth['action']
    synthetic_data


API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
