.. currentmodule:: howso.engine

Predictions
===========
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of using the Howso Engine for **Regression** and  **Classification** in
   order to predict outcomes such as taxi fares, stock prices, health metrics such as body fat percentages, or as in
   this example, the average miles per gallon (MPG) or Fuel Type of a vehicle based on capabilities and physical
   attributes of the vehicle.

Objectives: what you will take away
-----------------------------------
- **Definitions & an understanding** of basic regression, classification, continuous vs categorical/nominal Action Features, :class:`Trainee`, :meth:`~Trainee.react`,  :meth:`~Trainee.react_into_trainee`, and :meth:`~Trainee.get_prediction_stats`.
- **How-To** perform a basic regression or classification analysis using the Howso Engine to predict the Highway MPG or Fuel Type based on vehicle Context Features.

Prerequisites: before you begin
-------------------------------
- **Installation** - you have successfully installed :doc:`Howso Engine <../getting_started/installing>`
- **Additional Libraries** - you have installed these libraries:

    - `pandas <https://pandas.pydata.org/>`__
    - `matplotlib <https://matplotlib.org/stable/index.html>`__

Data
----
   :download:`Download </_assets/vehicles.csv>` 23,606 vehicles from 1984 - 2022, including make, model, MPG, drive-type, size, class and fuel type.

Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover:

- :download:`Engine Intro <https://github.com/howsoai/howso-engine-recipes/blob/main/1-engine-intro.ipynb>` download a sample notebook to run code using the engine for regression yourself.

Concepts & Terminology
----------------------
**Regression** - is used to describe the relationship between one or more Context Features and a **continuous** numeric
Action Feature, as in this guide predicting the **Highway MPG** of a vehicle based on its physical characteristics and
year manufactured.

**Classification** - is used to describe the relationship between one or more Context Features and a **categorical/nominal**
Action Feature, as in this guide predicting the **FuelType** of a vehicle based on its physical characteristics and year
manufactured. For Howso Engine, the action feature may be left in string format and does not need to be converted to numeric format.

**Trainee and React** - In this simple example, we will be creating a :ref:`Trainee <../getting_started/terminology:trainee>`
that we can be used :ref:`React <../getting_started/terminology:react>` to new case data, such as a new car we might be looking to build.

**Train and Analyze** - To create a :class:`Trainee`, we will first load data, define :doc:`Feature Attributes <feature_attributes>`
of the data and :ref:`Train <../getting_started/terminology:train>` the :class:`Trainee`.  The :class:`Trainee` can be used for many tasks,
but because we know exactly what we want to do, we will :ref:`Analyze <../getting_started/terminology:analyze>` to improve the
performance of our trainee by defining the specific set of :ref:`Context Features <../getting_started/terminology:context features>`
that we know we want to use to predict an :ref:`Action Feature <../getting_started/terminology:action features>`. The action
feature in this example will be **Highway MPG**.

**Evaluating the Trainee** - To understand the accuracy of the trainee for our tasks, we can use the built-in :meth:`Trainee.react_into_trainee`.
Since we are not using a train-test split approach in this example, we will use the :meth:`~Trainee.react_into_trainee` method, which
performs a :meth:`~Trainee.react` on each of the cases that is trained into the model using a leave-one-out approach.

That method allows us to use :meth:`~Trainee.get_prediction_stats` to evaluate regression accuracy statistics such as:

    - **R-Squared** - :math:`R^2` is a value that represents how well the predictions fit the data, the closer to 1.0 the better the fit
    - **Mean Absolute Error (MAE)** average absolute error between actual and predicted values over the whole dataset, and relative to the scale of what is being measured
    - **Root Mean Square Error (RMSE)** mean square root of errors over whole dataset, similar to MAE and relative to scale of what is measured

Or classification metrics including those derived from the `true positive (TP), true negative (TN), false positive (FP), false negative (FN) <https://en.wikipedia.org/wiki/Confusion_matrix>`__ metrics:

    - **Accuracy** - Describes the model performance across all classes and is comprised of the ratio of number of correct predictions to the total number of predictions.
        - (TP+TN)/(TP+FP+FN+TN).
    - **Precision** - Describes what proportion of positive predictions were correct.
        - (TP+TN)/(TP+FP+FN+TN).
    - **Recall** - Describes what proportion of actual positives were predicted correctly.
        - (TN)/(TN+FP).
    - **Mean Absolute Error (MAE)** average absolute error between actual and predicted Categorical Action Probabilities (CAP) over the whole dataset.
        - CAP is the prediction probability for each class of the action feature.

**React to New Cases** - Lastly, we will simply request the :class:`Trainee` to :meth:`~Trainee.react` to new cases we
present to it, giving us predictions of what the **Highway MPG** would be.

How-To Guide
------------
We want to predict the **Highway MPG** and the **Fuel Type** of a new vehicle based on a :class:`Trainee` we create from the vehicles dataset. In this guide, we will directly
show the code for **Highway MPG** prediction while including the code for **Fuel Type** as comments wherever the code differs.

Step 1 - Load Libraries
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    import pandas as pd
    import matplotlib.pyplot as plt

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

Step 2 - Load Data
^^^^^^^^^^^^^^^^^^
Using a pandas DataFrame, load the vehicles dataset from the csv file. We are going to drop make/model features because that is kinda cheating... Make sure it's what you expect, take a quick look at some of the data and use describe to make sure it has the shape you'd expect.

.. code-block:: python

    df = pd.read_csv("./data/vehicle_predict.csv")
    df = df.drop(['Make', 'Model'], axis=1)
    df.describe()

Step 3 - Define Features
^^^^^^^^^^^^^^^^^^^^^^^^
Howso can auto-detect features from data, using :meth:`~howso.utilities.infer_feature_attributes` but it is a best practice to review and configure.  In this tutorial, we will proceed as if the features were not detected as we want them to be, so we will make necessary adjustments.

.. note::

    Howso automatically determines whether to perform a **regression** or **classification** task by the feature attributes of the action feature you are trying to
    predict, specifically the feature `type` as shown below, thus it is **very important** to make sure that the feature types are correct.

.. code-block:: python

    # Auto detect features
    features = infer_feature_attributes(df)

    # For Regression, we will set `HighwayMPG` feature type to continuous
    features['HighwayMPG']['type'] = 'continuous'

    # For Classification, we will set `FuelType` feature type to nominal
    features['FuelType']['type'] = 'nominal'

    # We will also set these context features to continuous
    features['CityMPG']['type'] = 'continuous'
    features['Year']['type'] = 'continuous'
    features['PassengerVolume']['type'] = 'continuous'
    features['LuggageVolume']['type'] = 'continuous'


Step 4 - Create a Trainee and Train
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Next we will create a :class:`Trainee` and :meth:`~Trainee.train` based on data we have loaded into the DataFrame from the vehicles.csv.

.. code-block:: python

    # Create a new Trainee, specify features
    t = Trainee(features=features)

    # Train trainee
    t.train(df)

Step 5 - Analyze Trainee, Set Context & Action Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We know a specific task we want our :class:`Trainee` to :meth:`~Trainee.react` to, that is, to predict **Highway MPG** (the action feature) - using the context features: Year, DriveType, FuelType, CityMPG, PassengerVolume, LuggageVolume, and VehicleClass.  We can use :meth:`~Trainee.analyze` to improve performance of our model by analyzing for this specific target.

.. code-block:: python

    action_features = ['HighwayMPG']
    # Code for `FuelType` prediction
    # action_features = ['FuelType']
    context_features = features.get_names(without=action_features)

    t.analyze(context_features=context_features, action_features=action_features)

Step 6 - Generate Accuracy Metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Review the accuracy of the :class:`Trainee` by using the built-in :meth:`~Trainee.react_into_trainee` method, which performs a :meth:`~Trainee.react` on each of the cases that is trained into the model.  Then we can evaluate accuracy using :meth:`~Trainee.get_prediction_stats` which will give us R-Squared (:math:`R^2`), Mean Absolute Error (MAE) and Root Mean Square Error (RMSE) since this is a regression task.

.. code-block:: python

    # Recommended metrics
    t.react_into_trainee(action_feature=action_features[0], residuals=True)
    stats = t.get_prediction_stats(stats=['rmse', 'spearman_coeff', 'r2', 'mae'])
    # Code for `FuelType` metrics
    # stats = t.get_prediction_stats(stats=['accuracy', 'precision', 'recall', 'mae'])
    stats

Step 7 - Review Accuracy Metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We see the :class:`Trainee` has a very good fit for predicting **Highway MPG** with an :math:`R^2` of 0.99, which shows the :class:`Trainee` should be effective at predicting new cases of **Highway MPG**.

.. code-block:: python

    rmse              1.20
    spearman_coeff    0.96
    r2                0.99
    mae               0.72
    Name: HighwayMPG, dtype: float64

Step 8 - React to New Case
^^^^^^^^^^^^^^^^^^^^^^^^^^
We have a new vehicle we want to predict **Highway MPG** for. The test case is a 2022, All Wheel Drive, Mid-Sized Car, using Premium fuel, with a PassengerVolume of 95, LuggageVolume of 23 and  gets City MPG of 21.

The :class:`Trainee` can :meth:`~Trainee.react` to this new case, and makes a prediction.

.. code-block:: python

    data = {
        'Year': [2022],
        'DriveType': ['All-Wheel Drive'],
        'FuelType' : ['Premium'],
        'VehicleClass': ['Midsize Cars'],
        'CityMPG': [21],
        'PassengerVolume': [95],
        'LuggageVolume': [23]
    }

    test_case = pd.DataFrame(data)

    result = t.react(
        test_case,
        action_features=action_features,
        context_features=context_features
    )

.. note:: The method :meth:`Trainee.predict` can also be used for predictions instead of :meth:`Trainee.react`. :meth:`Trainee.predict` serves as a convenience functions that eliminates the extra output if all you want is the prediction.

Step 9 - Review Prediction
^^^^^^^^^^^^^^^^^^^^^^^^^^
Reviewing the prediction shows **HighwayMPG** of 29.

.. code-block:: python

    result['action']

    HighwayMPG
    29


API References
--------------
- :meth:`Trainee.react`
- :meth:`Trainee.react_into_trainee`
- :meth:`Trainee.get_prediction_stats`
- :meth:`Trainee.predict`