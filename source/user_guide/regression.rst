.. currentmodule:: howso.engine

Regression
==========
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of using the Howso Engine for **Regression** in order to predict outcomes such as taxi fares, stock prices, health metrics such as body fat percentages, or as in this example, the average miles per gallon (MPG) of a vehicle based on capabilties and physical attributes of the vehicle.  

Objectives: what you will take away
-----------------------------------
- **Definitions & an understanding** of basic regression, :class:`Trainee`, :meth:`~Trainee.react`, continous Action Features, :meth:`~Trainee.react_into_trainee`, and :meth:`~Trainee.get_prediction_stats`.  
- **How-To** perform a basic regression analysis using the Howso Engine to predict the Highway MPG based on vehicle Context Features.
- **API References** of where to find more details of APIs used in this guide.

Prerequisites: before you begin 
-------------------------------
- **Installation** - you have succesfully installed :doc:`Howso Engine <installing>` 
- **Additional Libraries** - you have installed these libraries:

    - `pandas <https://pandas.pydata.org/>`__
    - `matplotlib <https://matplotlib.org/stable/index.html>`__

Data
----
   :download:`Download </_assets/vehicles.csv>` 23,606 vehicles from 1984 - 2022, including make, model, MPG, drive-type, size, class and fuel type. 

Notebook Recipe
---------------
   :download:`Engine Intro </_assets/recipes/1-engine-intro.ipynb>` download a sample notebook to run code using the engine for regression yourself. 

Concepts & terminology to understand
------------------------------------
**Regression** - is used to describe the relationship between one or more Context Features and a continuous numeric Action Feature, as in this guide predicting the **Highway MPG** of a vehicle based on it's physical characteristics and year manufactured.  

**Trainee and React** In this simple example, we will be creating a :ref:`Trainee <user_guide/terminology:trainee>` that we can be used :ref:`React <user_guide/terminology:react>` to new case data, such as a new car we might be looking to build.  

**Train and Analyze** To create a :class:`Trainee`, we will first load data, define :doc:`Feature Attributes <feature_attributes>` of the data and :ref:`Train <user_guide/terminology:train>` the :class:`Trainee`.  The :class:`Trainee` can be used for many tasks, but because we know exactly what we want to do, we will :ref:`Analyze <user_guide/terminology:analyze>` to improve the performance of our trainee by defining the specific set of :ref:`Context Features <user_guide/terminology:context features>`that we know we want to use to predict an :ref:`Action Feature <user_guide/terminology:action features>`. The action feature in this example will be **Highway MPG**.

**Evaluating the Trainee** To understand the accuracy of the trainee for our tasks, we can use the built-in :meth:`Trainee.react_into_trainee`. Since we are not using a train-test split approach in this example, we will use the :meth:`~Trainee.react_into_trainee` method, which performs a :meth:`~Trainee.react` on each of the cases that is trained into the model. That method allows us to use :meth:`~Trainee.get_prediction_stats` to evaluate regression accuracy statistics such as:

    - **R-Squared** - :math:`R^2` is a value that represents how well the predictions fit the data, the closer to 1.0 the better the fit 
    - **Mean Absolute Error (MAE)** average absolute error between actual and predicted values over the whole dataset, and relative to the scale of what is being measured
    - **Root Mean Square Error (RMSE)** mean square root of errors over whole dataset, similar to MAE and relative to scale of what is measured 

**React to New Cases** Lastly, we will simply request the :class:`Trainee` to :meth:`~Trainee.react` to new cases we present to it, giving us predictions of what the **Highway MPG** would be. 

How-To Guide
------------
We want to predict the **Highway MPG** of a new vehicle based on a :class:`Trainee` we create from the vehicles dataset. 

Step 1 - Load Libraries
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    import pandas as pd
    import matplotlib.pyplot as plt

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes    

Step 2 - Load Data
^^^^^^^^^^^^^^^^^^
Using a pandas dataframe, load the vehicles dataset from the csv file. We are going to drop make/model features because that is kinda cheating... Make sure it's what you expect, take a quick look at some of the data and use describe to make sure it has the shape you'd expect.  

.. code-block:: python

    df = pd.read_csv("./data/vehicle_predict.csv")
    df = df.drop(['Make', 'Model'], axis=1) 
    df.describe()

Step 3 - Define Features
^^^^^^^^^^^^^^^^^^^^^^^^
Howso can auto-detect features from data, using :meth:`infer_feature_attributes` but it is a best practice to review and configure.  In this tutorial, features were not detected as we want them to be, so we will make necessary adjustments.  

.. code-block:: python

    # Auto detect features 
    features = infer_feature_attributes(df)

    # we will set these features to continuous 
    features['CityMPG']['type'] = 'continuous'
    features['HighwayMPG']['type'] = 'continuous'
    features['Year']['type'] = 'continuous'
    features['PassengerVolume']['type'] = 'continuous'
    features['LuggageVolume']['type'] = 'continuous'
    

Step 4 - Create a Trainee and Train
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Next we will create a :class:`Trainee` and :meth:`~Trainee.train` based on data we have loaded into the dataframe from the vehicles.csv. 

.. code-block:: python

    # Create a new Trainee, specify features
    t = Trainee(features=features)

    # Train trainee
    t.train(df)

Step 5 - Analyze Trainee, Set Context & Action Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We know a specific task we want our :class:`Trainee` to :meth:`~Trainee.react` to, that is, to predict **Highway MPG** (the action feature) - using the context features: Year, DriveType, FuelType, CityMPG, PassengerVolume, LuggageVolume, and VehicleClass.  We can use :meth:`~Trainee.analyze` to improve peformance of our model by analyzing for this specific target. 

.. code-block:: python

    action_features = ['HighwayMPG']
    context_features = features.get_names(without=action_features)

    t.analyze(context_features=context_features, action_features=action_features)

Step 6 - Generate Accuracy Metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Review the accuracy of the :class:`Trainee` by using the built-in :meth:`~Trainee.react_into_trainee` method, which performs a :meth:`~Trainee.react` on each of the cases that is trained into the model.  Then we can evaluate accuracy using :meth:`~Trainee.get_prediction_stats` which will give us R-Squared (:math:`R^2`), Mean Absolute Error (MAE) and Root Mean Square Error (RMSE). 

.. code-block:: python

    # Recommended metrics
    t.react_into_trainee(action_feature=action_features[0], residuals=True)
    stats = t.get_prediction_stats(stats=['rmse', 'spearman_coeff', 'r2', 'mae'])
    stats

Step 7 - Review Accuracy Metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We see the :class:`Trainee` has a very good fit for predicting **Highway MPG** with an :math:`R^2` of 0.99, which shows the :class:`~trainee` should be effective at predicting new cases of **Highway MPG**, let's move onto that next.

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

Step 9 - Review Prediction
^^^^^^^^^^^^^^^^^^^^^^^^^^
Reviewing the prediction shows **HighwayMPG** of 29.

.. code-block:: python

    result['action']

    HighwayMPG
    0          29,

What's Next?
------------  
.. topic:: Classification using Howso Engine

   Learn to use Howso Engine to classify vehicles using the :doc:`Classification User Guide <classification>`