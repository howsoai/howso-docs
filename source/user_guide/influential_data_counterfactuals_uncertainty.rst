Influential Data, Counterfactuals, and Uncertainties of Predictions
===================================================================
.. topic:: What is covered in this user guide.

    At its heart, Howso’s Engine is data-centric, Understandable AI. Engine directly uses the data
    to gain insights and make predictions. In this guide, you will learn how Engine interrogates the data to determine the **influence** of each data point on a prediction,
    if there were any **counterfactuals** to the prediction in the data, and the **uncertainty** it has in the prediction.

Objectives: what you will take away
-----------------------------------
- **Definitions & an understanding** of influential data, counterfactuals, and uncertainty within Engine.
- **How-To** obtain influential data, counterfactuals, and uncertainties using Engine.

Prerequisites: before you begin
-------------------------------

    - You have successfully :doc:`installed Howso Engine <../getting_started/installing>`
    - You have :doc:`loaded, configured, trained, and analyzed data <basic_workflow>`

Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover:

- :download:`Interpretability <https://github.com/howsoai/howso-engine-recipes/blob/main/2-interpretability.ipynb>`

Concepts & Terminology
----------------------

- :doc:`Uncertainty <../getting_started/terminology:Uncertainty>` is the amount of information that is unknown about a prediction,
  and is characterized by a prediction's residual. The :ref:`residual <../getting_started/terminology:residual>` is the mean absolute
  error between a predicted and actual value.
- :doc:`Influential cases <../getting_started/terminology:Influential Cases>` are the records that were directly used to make a prediction or to derive a result.
- :doc:`Counterfactuals <../getting_started/terminology:Boundary Cases>`, or boundary cases, are the records that have similar Context Features to that of a
  prediction's Context Features, but instead have different Action Feature values. In other words, these are records with similar information that contain a different
  result. For example, if the prediction for fruit type was "peach", a boundary case might be a very peach-looking "nectarine".


How-To Guide
------------

Task 1 - Obtain influential cases and counterfactuals (boundary cases)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After building, training, and analyzing a `Trainee`, you can obtain the influential cases and counterfactuals for a prediction on a test case in a `react()` call.

.. code-block:: python

    # Details describe the information we are getting from a given react call
    details = {
        'influential_cases': True,
        'boundary_cases': True
    }

    results = t.react(contexts=test_case[context_features], # Input values for which you want a prediction
                    context_features=context_features,
                    action_features=action_features,
                    details=details
    )

    # Save the influential cases, for the prediction of the first record (record 0)
    influence_df = pd.DataFrame(results['explanation']['influential_cases'][0])

    # Save the boundary cases, for the prediction of the first record (record 0)
    boundary_df = pd.DataFrame(results['explanation']['boundary_cases'][0])


Task 2 - Obtain uncertainty information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Feature residuals are calculated by holding out each individual feature, and then using the other features to predict the holdout feature.
This is similar to the leave-one-out validation technique used in traditional machine learning. The results represent the `Trainee`'s uncertainty for that feature.
We will use the local feature residual to examine the uncertainty for a specific case and the global feature residual as a baseline.

.. code-block:: python

    ## Compute local feature residuals
    # Details describe the information we are getting from a given react call
    details = {
        'robust_computation': True,
        'feature_residuals': True,
    }

    results = t.react(contexts=test_case[context_features], # Input values for which you want a prediction
                    context_features=context_features,
                    action_features=action_features,
                    details=details
    )

    # Save local feature residuals
    feature_residuals_dicts = results['explanation']['feature_residuals']
    feature_residuals = pd.DataFrame(list(feature_residuals_dicts[0].items()))
    feature_residuals = feature_residuals.T
    feature_residuals.columns = feature_residuals.loc[0]
    feature_residuals = feature_residuals.drop(0, axis=0)

    ## Compute global feature residuals
    # We use react_into_trainee to analyze the cases in our Trainee
    t.react_into_trainee(context_features=context_features, action_feature=action_features[0], contributions_robust=True, mda=True, residuals=True)

    global_feature_residuals = t.get_prediction_stats(action_feature=action_features[0], stats=['mae'])


API References
--------------
- :py:meth:`Trainee.react`