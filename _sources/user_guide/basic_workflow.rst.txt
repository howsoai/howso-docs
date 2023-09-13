.. currentmodule:: howso.engine

Basic Workflow
==============
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of using the Howso Engine.

Objectives: what you will take away
-----------------------------------
- **Definitions & an understanding** of terminology unique to Howso Engine and what the basic workflow of using the Howso Engine looks.
- **How-To** - Importing data, mapping features, training, analyzing, and making inferences using the Howso Engine.
- **API References** - where to find references to APIs used in this user guide.

Prerequisites: before you begin
-------------------------------
**Installation**

- you have successfully :doc:`installed  Howso Engine <../getting_started/installing>`
- You've installed these libraries:
  - `pandas <https://pandas.pydata.org/>`__
  - `pmlb <https://github.com/EpistasisLab/pmlb>`__

Data
----
Our example dataset for this recipe is the well known ``Adult`` dataset. It is accessible via the `pmlb <https://github.com/EpistasisLab/pmlb>`__ package installed earlier. We use the ``fetch_data()`` function to retrieve the dataset in Step 1 below.

Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover:

- :download:`Engine Intro <https://github.com/howsoai/howso-engine-recipes/blob/main/1-engine-intro.ipynb>`

Concepts & Terminology
----------------------
Howso Engine is a generalized Machine Learning (ML) and Artificial Intelligence platform that creates powerful decision-making models that are fully explainable, auditable, and editable. Howso Engine uses Instance-Based Machine Learning which stores instances, i.e., data points, in memory and makes predictions about new instances given their relationship to existing instances. This technology harnesses a fast spatial query system and information theory for performance and accuracy.

- :ref:`Trainee <user_guide/terminology:trainee>`
- :ref:`Train <user_guide/terminology:train>`
- :ref:`Analyze <user_guide/terminology:analyze>`
- :ref:`React <user_guide/terminology:react>`
- :ref:`Case <user_guide/terminology:case>`
- :ref:`Feature <user_guide/terminology:feature>`
- :ref:`Action Features <user_guide/terminology:action features>`
- :ref:`Context Features <user_guide/terminology:context features>`
- :doc:`Feature Attributes <feature_attributes>`

How-To Guide
------------
Here we will walk through the steps of what a basic workflow might look like when using Howso Engine. First, we will load data into a pandas DataFrame for use with Howso Engine. Then, we will use the Howso Engine to map attributes of the features, train a trainee, analyze, and react.

.. code-block:: python

    import pandas as pd
    from pmlb import fetch_data

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

Step 1 - Load Data
^^^^^^^^^^^^^^^^^^
This dataset consists of 14 Context Features and 1 Action Feature. The Action Feature in this version of the ``Adult`` dataset has been renamed to ``target`` and it takes the form of a binary indicator for whether a person in the data makes more than $50,000/year (target=1) or less (target=0).

.. code-block:: python

    df = fetch_data('adult', local_cache_dir="data/adult")

    # Subsample the data to ensure the example runs quickly
    df = df.sample(2000)


Step 2 - Map Data
^^^^^^^^^^^^^^^^^
Typically, an exploratory analysis is done on the data to get a general feel of the descriptive statistics and data attributes.

Methods like ``describe`` from a Pandas DataFrame often automatically present these types of information of interest to a user, as shown below. While informative, these descriptive statistics are often used as a sanity check pre- and post-modeling and a model typically doesn't actually use any of these feature attributes.

.. code-block:: python

    df.describe()


In the Howso Engine workflow, feature attributes are an essential part of model building and usage. By incorporating certain feature attributes into training process itself, Howso Engine gains another layer of information that will help in fine-tuning the results.

In order to assist the user with defining the feature attributes, Howso has an :py:meth:`~howso.utilities.infer_feature_attributes` tool that automatically processes the dataset for the user.

In Howso Engine , these feature attributes are model infrastructure feature parameters that are based on the existing data, rather than exact descriptive statistics. This is why, for example, the min and max bounds on continuous features are not the exact min and max values of the dataset, but rather an expanded version of those min and max values to allow for some variation.

.. code-block:: python

    features = infer_feature_attributes(df)

Step 3 - Specify Context and Action Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Context Features are a set of features that is used to describe values being used for input, observation, or other computation. In traditional ML this is often referred to as input features, or sometimes just features.

Action Features are a set of features that is used as to describe values for output of a Trainee when it reacts, which is often as a response to input Context Features. In traditional supervised ML this is often referred to as targets, target features, or labels, and in generative ML, Action Features are the resulting data.

Assuming our data set includes a feature named "target" that represents the desired output of a trainee when it reacts, we can specify context and action features like so:

.. code-block:: python

    action_features = ['target']
    context_features = features.get_names(without=action_features)


Step 4 - Create the Trainee
^^^^^^^^^^^^^^^^^^^^^^^^^^^
To begin the Howso Engine workflow, a Trainee is created to act as a base for all of our ML needs. In all subsequent documentation, we will refer to Howso Engine's model as Trainee.

.. code-block:: python

    t = Trainee(
        features=features,
        overwrite_existing=True
    )

Step 5 - Train
^^^^^^^^^^^^^^
Exposing a Trainee to a Case which may cause the ML algorithm to update the Trainee. This is a single training step; training may happen at each decision, at a certain sampling rate of observations per second, or at certain events.

.. code-block:: python

    t.train(df)

Step 6 - Analyze
^^^^^^^^^^^^^^^^
Tune internal parameters to improve performance and accuracy of predictions and metrics. Analysis may be targeted or targetless. Targetless analysis provides the best balanced set of hyperparameters if an Action Feature is not specified, along with a performance boost while targeted analysis provides a boost to accuracy.

.. code-block:: python

    t.analyze(context_features=context_features, action_features=action_features)

Step 7 - React
^^^^^^^^^^^^^^
React is querying the Trainee for some response, potentially for a given set of context feature values, whether to determine action features, or to determine other details. This is the primary verb that can encompass supervised learning, unsupervised learning, generative outputs, and to determine various interpretations, explanations, and support data for any reaction. In the context of this example, React is used to get an action feature back based on the new Case's context features. In a traditional ML workflow this is often called predicting or labeling.

Once Howso Engine is trained and analyzed, it provides the user with a variety of ML capabilities. At this stage in the Howso Engine workflow, a typical use case would be to evaluate the accuracy of the Trainee, which is performed by the :py:meth:`~Trainee.react` method. This is equivalent to ``predict`` in many traditional Machine Learning workflows, although the :py:meth:`~Trainee.react` method is not solely used for supervised predictions.

.. code-block:: python

    results = t.react()
    predictions = results['action'][action_features]


API References
--------------
- :py:meth:`~howso.utilities.infer_feature_attributes`
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
