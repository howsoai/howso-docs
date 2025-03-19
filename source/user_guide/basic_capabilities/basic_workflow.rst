.. currentmodule:: howso.engine

Basic Workflow
==============
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of using the Howso Engine.

Objectives: what you will take away
-----------------------------------
- **Definitions & an understanding** of terminology unique to Howso Engine and what the basic workflow of using the Howso Engine looks like.
- **How-To** import data, map features, train, analyze, and make inferences using the Howso Engine.

Prerequisites: before you begin
-------------------------------
**Installation**

- You've successfully :doc:`installed  Howso Engine <../../getting_started/installing>`

- You've installed these libraries:

  - `pandas <https://pandas.pydata.org/>`__
  - `pmlb <https://github.com/EpistasisLab/pmlb>`__

Data
----
Our example dataset for this recipe is the well known ``Adult`` dataset. It is accessible via the `pmlb <https://github.com/EpistasisLab/pmlb>`__ package installed earlier. We use the ``fetch_data()`` function to retrieve the dataset in Step 1 below.


Concepts & Terminology
----------------------
Howso Engine is a generalized Machine Learning (ML) and Artificial Intelligence platform that creates powerful decision-making models that are fully explainable, auditable, and editable. Howso Engine uses Instance-Based Machine Learning which stores instances, i.e., data points, in memory and makes predictions about new instances given their relationship to existing instances. This technology harnesses a fast spatial query system and information theory for performance and accuracy.

- :ref:`trainee`
- :ref:`train`
- :ref:`analyze`
- :ref:`react`
- :ref:`case`
- :ref:`feature`
- :ref:`action_features`
- :ref:`context_features`
- :doc:`feature_attributes`

Notebook Recipe
---------------
The following recipe will demonstrate some of the capabilities demonstrated in this guide as well as a few additional capabilities.

- :download:`Engine Intro <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/engine-intro.ipynb>`

How-To Guide
------------
Here we will walk through the steps of what a basic workflow might look like when using Howso Engine. First, we will load data into a pandas DataFrame for use with Howso Engine. Then, we will use the Howso Engine to map attributes of the features, train a trainee, analyze, and react.

.. code-block:: python

    import pandas as pd
    from pmlb import fetch_data

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes


Step 1 - Load Data and Infer Feature Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
First, we load the ``adult`` dataset from the PMLB repository.  This dataset consists of 15 features, which will have their 
attributes inferred by :func:`~howso.utilities.infer_feature_attributes`.  This will determine attributes about each feature 
including bounds, allowed values, and feature type.  Before the following steps, the inferred feature attributes should be 
inspected to ensure their correctness.

.. code-block:: python

    df = fetch_data('adult').sample(1_000)
    features = infer_feature_attributes(df)

    print(features.to_dataframe())


Step 2 - Create the `Trainee`, Train, and Analyze
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A `Trainee` is similar in function to a model in other machine learning paradigms, but is not locked to any particular use-case 
or to predicting a particular feature.  Note that both the data and the feature attributes are supplied at this time.  Since the 
feature attributes are essentially a part of the training data it is extremely important to ensure they are correct.

.. code-block:: python

    trainee = Trainee(features=features)
    trainee.train(df)


After the data are trained, we can :meth:`Trainee.analyze` the `Trainee`.  This method will determine the best 
hyperparameters for the data and cache some important values that are used to ensure the highest model performance.  By default, 
:meth:`Trainee.analyze` will optimize the `Trainee`'s parameters for any possible target feature.

.. code-block:: python
    
    trainee.analyze()


Step 3 - React
^^^^^^^^^^^^^^
Now that the `Trainee` has been prepared, it is ready for use.  A common use-case, determining how well a model performs when 
predicting the dataset, can be done with a single call to the `Trainee`:

.. code-block:: python

    prediction_stats = trainee.get_prediction_stats(
        action_feature="target",
        details={"prediction_stats": True},
    )
    print(prediction_stats)


An `action_feature` is the same as a target feature or dependent variable.  This call will compute a number of different statistics, 
including accuracy, precision, recall, :math:`R^2`, and others.  Rather than performing a train-test split, which is common with 
other machine learning techniques, the `Trainee` uses leave-one-out to provide a more comprehensive understanding of the data.  
More traditional approaches can still be used with the :meth:`Trainee.react` method.

Additional analyses can be performed on data contained within a `Trainee` using various methods, including:

- :meth:`Trainee.react_aggregate`
- :meth:`Trainee.react`
- :meth:`Trainee.react_into_features`
    

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

    prediction_stats = trainee.get_prediction_stats(
        action_feature="target",
        details={"prediction_stats": True},
    )
    print(prediction_stats)


API References
--------------
- :py:func:`~howso.utilities.infer_feature_attributes`
- :py:class:`~Trainee`
    - :py:meth:`Trainee.train`
    - :py:meth:`Trainee.analyze`
    - :py:meth:`Trainee.react_aggregate`
    - :py:meth:`Trainee.react`
    - :py:meth:`Trainee.react_into_features`
