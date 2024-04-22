.. currentmodule:: howso.engine

Bias Mitigation
===============
.. topic:: What is covered in this user guide.

    In this guide, you will learn how to use Howso Engine for **Bias Mitigation**.

Objectives: what you will take away
-----------------------------------
- **Definitions & Understanding** of data bias and why it occurs.
- **How-To** perform bias mitigation using Howso Engine.

Prerequisites: before you begin
-------------------------------
**Installation**

- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have :doc:`loaded, configured, trained, and analyzed data <../basics/basic_workflow>`
- You are familiar with :ref:`feature contributions <contribution>`

Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover:

- :download:`Bias Mitigation <https://github.com/howsoai/howso-engine-recipes/blob/main/5-bias_mitigation.ipynb>`

Concepts & Terminology
----------------------

- **What is biased data?**

Often, poor data quality and subsequent unequitable analysis results arise from biases in data. There are a variety of ways bias may affect your data:

- Sampling and representation bias - lack of diversity of the populations
  contained in the data

- Measurement and omitted variables bias - choice of information contained in
  the dataset

- Aggregation bias - data is generalized across populations

- Linking bias - various datasets are combined

Biases in data may propagate through data analytics and AI/ML models, leading
to biased results upon which predictions and decisions might be made.
Additionally, biased results may be projected into the future and lead to
missed opportunities to create true value. This potentially harms various
groups of people and reduces the overall utility of the data. Because analytics
and modeling results that use biased data are increasingly falling under
regulations, decisions that are based on insights gained from biased data might
lead to breaches of these regulations.

In addition to understanding bias, we recommend being familiar with the following concepts:

- :ref:`trainee`
- :ref:`react`
- :ref:`training_session`
- :ref:`Feature Contribution <contribution>`
- :ref:`Feature MDA <mda>`


How-To Guide
------------
There are two ways to use Engine to understand and mitigate data bias.


Method 1 - Explore data for bias
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Detect which protected attributes in a dataset contribute the most to model predictions, showing biases users may or may not have recognized.

After building, training, and analyzing a `Trainee`, you can use the `details` argument of `react` to obtain the mean decrease in accuracy of
including a feature and feature contributions to understand which features are driving a prediction.

.. code-block:: python

   # Details describe the information we are getting from a given react call
   details = {
       'feature_mda': True,
       'feature_contributions': True
   }

   # Obtain indices and session ids
   stored_data = t.get_cases(
       session=t.active_session,
       features=df.columns.tolist() + ['.session_training_index', '.session']
   )

   # React
   results = t.react(test_case[context_features],
                   context_features=context_features,
                   action_features=action_features,
                   details=details
   )


Step 2 - Control predictions for data bias
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Easily update which features are used in predictions, so features that contribute to bias can be omitted.
Within the `react` call, specify only the context features that do not contribute to prediction bias.

.. code-block:: python

   # React
   results = t.react(test_case[context_features], # Input features - only those which do not include bias
                   context_features=context_features, # Input features - only those which do not include bias
                   action_features=action_features,
                   details=details
   )


API References
--------------
- :meth:`Trainee.react`
- :meth:`Trainee.get_cases`

