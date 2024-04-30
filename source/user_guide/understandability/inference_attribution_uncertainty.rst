Inference with Attribution and Uncertainty Estimation
=====================================================
.. topic:: What is covered in this user guide.

   At its heart, Howso's Engine is data-centric, Understandable AI. Engine directly uses the data
   to gain insights and make predictions. In this guide, you will learn how to inspect what data was used to make a prediction,
   if there were any **counterfactuals** to the prediction in the data, and the estimated **uncertainty** of the prediction.

Objectives: what you will take away
-----------------------------------
- **Definitions & an understanding** of influential data, counterfactuals, and uncertainty within Engine.
- **How-To** obtain influential data, counterfactuals, and uncertainties using Engine.

Prerequisites: before you begin
-------------------------------

- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have :doc:`loaded, configured, trained, and analyzed data <../basics/basic_workflow>`

Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover:

- :download:`Interpretability <https://github.com/howsoai/howso-engine-recipes/blob/main/2-interpretability.ipynb>`

Concepts & Terminology
----------------------

- :ref:`uncertainty` is the amount of information that is unknown about a prediction,
  and is characterized by a prediction's residual. The :ref:`residual` is the mean absolute
  error between a predicted and actual value across a set of predictions.
- :ref:`influential_cases` are the records that were directly used to make a prediction or to derive a result.
- :ref:`Counterfactuals <boundary_cases>`, or boundary cases, are the records that have similar Context values to that of a
  prediction's Context values, but instead have different Action Feature values. In other words, these are records with similar information that contain a different
  result. For example, if the prediction for fruit type was "peach", a boundary case might be a very peach-looking "nectarine".


How-To Guide
------------

Task 1 - Obtain influential cases and counterfactuals (boundary cases)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After building, training, and analyzing a :py:class:`Trainee`, you can obtain the influential cases and counterfactuals for a prediction on a test case in a :py:meth:`Trainee.react` call.

.. code-block:: python

    # Details describe the additional information we are requesting in a call to react
    details = {
        'influential_cases': True,
        'boundary_cases': True
    }

    results = t.react(contexts=[test_case[context_features]], # Input values for which you want a prediction
                    context_features=context_features,
                    action_features=action_features,
                    details=details
    )

    # Save the influential cases, for the prediction of the first record (record 0)
    influence_df = pd.DataFrame(results['explanation']['influential_cases'][0])
    print(influence_df)

    # Save the boundary cases, for the prediction of the first record (record 0)
    boundary_df = pd.DataFrame(results['explanation']['boundary_cases'][0])
    print(influence_df)


Task 2 - Obtain uncertainty information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Feature residuals are calculated as the mean absolute error of predictions towards that feature for a set of cases in the model.
This is similar to the leave-one-out validation technique used in traditional machine learning. The results represent the :py:class:`Trainee`'s uncertainty for that feature.
We will use the local feature residual to examine the uncertainty for a specific case and the global feature residual as a baseline. The feature residuals returned
by a call to :py:meth:`Trainee.react` are the mean absolute error of predictions for each feature among the cases that make up the local model of the prediction.

We can get the mean absolute error of predictions for each feature across the entire model by using :py:meth:`Trainee.react_into_trainee` and
:py:meth:`Trainee.get_prediction_stats`, where the first caches the residuals and the latter retrieves them from the Trainee.

.. code-block:: python

    ## Compute local feature residuals
    # Details describe the additional information we are requesting in a call to react
    details = {
        'feature_residuals': True,
    }

    results = t.react(contexts=[test_case[context_features]], # Input values for which you want a prediction
                    context_features=context_features,
                    action_features=action_features,
                    details=details
    )

    # Inspect local feature residuals
    feature_residuals_dicts = results['explanation']['feature_residuals']
    feature_residuals = pd.DataFrame(list(feature_residuals_dicts[0].items()))
    feature_residuals = feature_residuals.T
    feature_residuals.columns = feature_residuals.loc[0]
    feature_residuals = feature_residuals.drop(0, axis=0)
    print(feature_residuals)

    # Compute global feature residuals
    # We use react_into_trainee to evaluate predictions within our Trainee
    t.react_into_trainee(context_features=context_features, action_feature=action_features[0], contributions_robust=True, mda=True, residuals=True)
    global_feature_residuals = t.get_prediction_stats(action_feature=action_features[0], stats=['mae'])
    print(global_feature_residuals)


API References
--------------
- :py:meth:`Trainee.react`