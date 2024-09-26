Recipes
=======

The Howso Engine `Recipes Github <https://github.com/howsoai/howso-engine-recipes/tree/main>`_ page includes many "recipes" for building your own use-cases!
They include an introduction recipe followed by several sections of different types of recipes.

Introduction Recipe
^^^^^^^^^^^^^^^^^^^

1. :download:`Howso Engine Intro <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/engine-intro.ipynb>`
    - Learn the basics of our powerful engine in a traditional ML workflow!

Section 1-Insights
^^^^^^^^^^^^^^^^^^
Explores the different types of insights that can be attained using Howso.

**Notable Recipes**

1. :download:`Engine-Insights <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/1-Insights/engine-insights.ipynb>`
    - See an introduction to many of the insights that can be gained through Howso Engine.

2. :download:`Conditioned-Insights <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/1-Insights/conditioned-insights.ipynb>`
    - See how your dataset's predictability changes under a variety of conditions providing out of the box insights on your data without the need to build multiple machine learning models.

3. :download:`Predition-Insights <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/1-Insights/prediction-insights.ipynb>`
    - See how Predictive insights with complete attribution and detailed explanations can be gained through Howso Engine.

Section 2-Workflows
^^^^^^^^^^^^^^^^^^^
Example use cases that combine different Howso insights and capabilities into practical workflows.

**Notable Recipes**

1. :download:`Anomaly Detection <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/2-Workflows/anomaly_detection/anomaly_detection.ipynb>`
    - Build your fraud and rare-events use-cases from this example using `Surprisal`!
2. :download:`Audit Edit <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/2-Workflows/auditing_and_editing/auditing_and_editing.ipynb>`
    - Have you ever spent hours training a fine-tuned model only to have to retrain it with new data? Use this example to edit your trainee with no extra training needed!
3. :download:`Bias Mitigation <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/2-Workflows/bias_mitigation/bias_mitigation.ipynb>`
    - Does your historical data contain bias such as men making more money than women? In traditional ML, this pattern will be used for any future predictions. Learn how to mitigate these biases in this example!
4. :download:`Feature Importance <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/2-Workflows/feature_importance/feature_importance.ipynb>`
    - How important are the features in your dataset? 
5. :download:`Time Series <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/2-Workflows/time_series/timeseries_overview.ipynb>`
    - Time series analysis can provided additional insight into trends within your data. Use this example for your Time Series use-cases!
6. :download:`Clustering: Pairwise-Distance Calculation <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/2-Workflows/clustering/clustering.ipynb>`
    - This example demonstrates Howso's ability to calculate pairwise distances between training cases. Distances can be used for a variety of use cases, including clustering algorithms. Use this recipe for your Clustering use-cases!
7. :download:`Model Drift Monitoring <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/2-Workflows/model_monitoring/drift_monitoring.ipynb>`
        - Drift occurs when a trained model no longer reflects the desired aspects of reality, leading to poor predictions. Howso Engine can be used to monitor any potential drift by evaluating bias in both new and ongoing models using online learning and interpretability. Use this example to build your Drift Monitoring use-cases!


Section 3-Integration
^^^^^^^^^^^^^^^^^^^^^
How to connect and use Howso with a variety of outside platforms.

Coming soon!

Section 4-Examples
^^^^^^^^^^^^^^^^^^
More Coming soon!

1. :download:`Extra Examples <https://github.com/howsoai/howso-engine-recipes/tree/main/recipes/4-Examples/extra_examples>`
    - extra examples of functionality covered in other recipes:

        * :download:`Asteroids <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/4-Examples/extra_examples/interpret_react.ipynb>`
            - This example uses Asteroid data to demonstrate Howso's interpretability to understand why the predictions were made. We build a Howso Engine Trainee to predict various information about different asteroids, understand the influential cases on the predictions, and understand the uncertainty of the predictions.

        * :download:`Cars <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/4-Examples/extra_examples/car_type_demo.ipynb>`
            - This example uses Car data to demonstrate Howso's interpretability to understand why the predictions were made. We train Howso Engine to predict classes of vehicles, understand potential anomalies, investigate vehicles on a case-by-case basis, and review the data that contributed to the predictions.

        * :download:`Census <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/4-Examples/extra_examples/predict_explain_show.ipynb>`
            - This example uses the Adult data set to demonstrate which cases and features contribute to predictions, anomalies analysis, and potential improvements to gain more insight into the data.

Section 5-Technical_Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Demonstrations of certain Howso technical capabilities.

**Notable Recipes**

1. :download:`Residuals Validation <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/5-Technical_Validation/residuals_validation.ipynb>`
    - You may have noticed we don't use the traditional ML approach of `train-test-split <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html>`_ in our example workflows. There are use-cases, especially in small datasets, where a user cannot afford to further cut their data away from training the model. Use this example as proof for why train-test-splits are no longer needed when using Howso™ !
2. :download:`Sparse Data and Null Handling <https://github.com/howsoai/howso-engine-recipes/blob/main/recipes/5-Technical_Validation/sparse_data_validation.ipynb>`
    - Sparse data and nulls (missing data) typically need preprocessing in most models, but not Howso. In fact, Howso has notable robustness when it comes to working with data that contain them. Use this example as proof for why you don't need to impute missing values with Howso!


.. |tmk|    unicode:: U+02122 .. TRADEMARK SIGN