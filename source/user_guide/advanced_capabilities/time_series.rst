.. currentmodule:: howso.engine

Time Series and Sequential Data Analysis
========================================
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of using Howso Engine for **time series and sequential data** analysis.
   This will enable you to easily capture and utilize temporal information and trends within data.

Objectives: what you will take away
-----------------------------------

- **Definitions & an understanding** of how time series and sequential data tools within the Howso Engine provide enhanced insight into your data.
- **How-To** use Engine's :py:meth:`~howso.utilities.infer_feature_attributes` tool to configure your time series and sequential data, and make time series predictions.

Prerequisites: before you begin
-------------------------------
**Installation**

- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.

Concepts & Terminology
----------------------
To understand this guide, we recommend being familiar with the following concepts:

- :ref:`trainee`
- :ref:`action_features`
- :ref:`context_features`

Notebook Recipe
---------------
The following recipes will supplement the content this guide will cover and go into some additional examples:

- :download:`Time Series Overview <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/2-Workflows/time_series/timeseries_overview.ipynb>`
- :download:`Time Series Forecasting <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/2-Workflows/time_series/timeseries_forecasting.ipynb>`

How-To Guide
------------
*Why are time series and sequential data predictions important?*

A significant amount of data is recorded at specific times. Utilizing this information can provide a wealth of insight
for future predictions, such as knowledge of whether events happen at certain intervals or how intervals between certain events influence other events.
Engine handles time series data using :py:meth:`~howso.utilities.infer_feature_attributes` and by using :meth:`Trainee.train` and :meth:`Trainee.react` to calculate and utilize information
about intervals within a dataset to make a prediction.

There are two key differences in the Howso Engine basic prediction workflow when dealing with time series and sequential data:

- :func:`howso.utilities.infer_../basics/feature_attributes` must be configured to include time series and sequential data information

- Context Features must be specified **after** the data is trained, as the time series context information is calculated during training
    and must be specified before the `analyze()` call to be utilized in a `react`


Task 1 - Infer Feature Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Identify id-feature and time-feature
    id_feature_name = "ID"
    time_feature_name = "date"
    features = infer_feature_attributes(
        df,
        time_feature_name=time_feature_name,
        id_feature_name=id_feature_name,
        datetime_feature_formats={"date": "%Y-%m-%d"},
        time_feature_is_universal=True,
    )

When calling :py:meth:`~howso.utilities.infer_feature_attributes` in time-series flows, it's imperative that the user specifies the time feature name and the id feature name. While not required, another very significant
parameter to consider is the ``time_feature_is_universal`` flag. This is a boolean flag that specifies to the Engine if the time feature should be considered "universal".

If the time feature is universal, then the Engine is not able to reference any future data when making a prediction. If the time feature is not universal, then the Engine could use future data
from other series, but still not future data within the same series. It is recommended to set this flag to True if there is any possibility of global relevancy of time, which is the default behavior.

Task 2 - Make a time series prediction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Create the Trainee
    t = Trainee(
        features=features,
        overwrite_existing=True
    )

    session1 = Session('train_session_1', metadata={'data': 'training data'})

    # Train
    t.train(df)

    # Store actual record data which includes all of the ts information
    cases_df = t.get_cases(session=session1)

    # Specify Context and Action Features
    action_features = ['target']
    context_features = cases_df.columns.drop(action_features).to_list()

    # Targeted Analysis
    t.analyze(context_features=context_features, action_features=action_features)

    # Calculate overall error metrics
    results = t.react_aggregate(
        action_feature=action_features[0],
        details={"prediction_stats": True}
    )
    results['target']


Task 3 - Forecast a time-series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Use react_series with continue_series_values to forecast a series
    series_reaction = t.react_series(
        action_features=["ID", "date", "value"],
        continue_series=True,
        continue_series_features=["ID", "date", "value"],
        continue_series_values=[
            [
                # A set of cases making up a series
                ["A", "2000-07-30", 100.0],
                ["A", "2000-07-31", 105.0]
                ["A", "2000-08-01", 110.0]
            ]
        ]
    )

    # Displaying the set of cases that forecast the given series
    print(series_reaction['series'])


API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react_series`
- :py:meth:`Trainee.react_aggregate`
- :py:meth:`~howso.utilities.infer_feature_attributes`
