Examples
========

Use these Jupyter Notebook examples as "recipes" for building your own use-cases!

1. :download:`Howso Engine Intro <https://github.com/howsoai/howso-engine-recipes/blob/main/1-engine-intro.ipynb>`
    - Learn the basics of our powerful engine in a traditional ML workflow!
2. :download:`Interpretability <https://github.com/howsoai/howso-engine-recipes/blob/main/2-interpretability.ipynb>`
    - See what really sets us apart with our suite of explainability tools! Use this example to find the factors that lead to a decision in your model.
3. :download:`Anomaly Detection <https://github.com/howsoai/howso-engine-recipes/blob/main/3-anomaly_detection.ipynb>`
    - Build your fraud and rare-events use-cases from this example using `Surprisal`!
4. :download:`Audit Edit <https://github.com/howsoai/howso-engine-recipes/blob/main/4-audit_edit.ipynb>`
    - Have you ever spent hours training a fine-tuned model only to have to retrain it with new data? Use this example to edit your trainee with no extra training needed!
5. :download:`Bias Mitigation <https://github.com/howsoai/howso-engine-recipes/blob/main/5-bias_mitigation.ipynb>`
    - Does your historical data contain bias such as men making more money than women? In traditional ML, this pattern will be used for any future predictions. Learn how to mitigate these biases in this example!
6. :download:`Validation <https://github.com/howsoai/howso-engine-recipes/blob/main/6-validation.ipynb>`
    - You may have noticed we don't use the traditional ML approach of `train-test-split <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html>`_ in our example workflows. There are use-cases, especially in small datasets, where a user cannot afford to further cut their data away from training the model. Use this example as proof for why train-test-splits are no longer needed when using Howso™ !
7. :download:`Sparse Data and Null Handling <https://github.com/howsoai/howso-engine-recipes/blob/main/engine_sparse_data.ipynb>`
    - Sparse data and nulls (missing data) typically need preprocessing in most models, but not Howso. In fact, Howso has notable robustness when it comes to working with data that contain them. Use this example as proof for why you don't need to impute missing values with Howso!
8. :download:`Time Series <https://github.com/howsoai/howso-engine-recipes/blob/main/engine_timeseries.ipynb>`
    - Time series analysis can provided additional insight into trends within your data. Use this example for your Time Series use-cases!
9. :download:`Clustering: Pairwise-Distance Calculation <https://github.com/howsoai/howso-engine-recipes/blob/main/engine_clustering.ipynb>`
    - This example demonstrates Howso's ability to calculate pairwise distances between training cases. Distances can be used for a variety of use cases, including clustering algorithms. Use this recipe for your Clustering use-cases!
10. :download:`Population Segmentation <https://github.com/howsoai/howso-engine-recipes/blob/main/engine_fuzzy_matching.ipynb>`
        - This example demonstrates Howso's ability to use `case_mda` to identify centroids in the data, then use the `influential_cases` of each centroid to find its corresponding members. Use this recipe for learning more about the Population Segments in your data!
11. :download:`Model Drift Monitoring <https://github.com/howsoai/howso-engine-recipes/blob/main/engine_drift_monitoring.ipynb>`
        - Drift occurs when a trained model no longer reflects the desired aspects of reality, leading to poor predictions. Howso Engine can be used to monitor any potential drift by evaluating bias in both new and ongoing models using online learning and interpretability. Use this example to build your Drift Monitoring use-cases!
12. :download:`Generative React and Synthetic Data Generation <https://github.com/howsoai/howso-engine-recipes/blob/main/engine_generative_react.ipynb>`
        - A defining feature of Howso is that it can perform `generative analysis` as well as `discriminative analysis`. This example shows how `generative analysis` can be used for synthetic data creation, which is the foundation for our enterprise product `Howso Synthesizer <https://www.howso.com/synthesizer>`_ ™ !

Applied Use-Cases
========

These notebooks provide an overview of applying Howso to make predictions based on historical data, and harnessing Howso's interpretability to understand why the predictions were made. Here, we demonstrate these capabilities on different datasets, and they explore concepts such as anomalies analysis, reviewing the data that contributed to the predictions, understanding the uncertainty of the predictions, and more. These are powerful tools for gaining insights from your data, so follow along and generate ideas for your own projects!

13. :download:`Asteroids <https://github.com/howsoai/howso-engine-recipes/blob/main/engine_interpret_react.ipynb>`
        - This example uses Asteroid data to demonstrate Howso's interpretability to understand why the predictions were made. We build a Howso Engine Trainee to predict various information about different asteroids, understand the influential cases on the predictions, and understand the uncertainty of the predictions.

14. :download:`Cars <https://github.com/howsoai/howso-engine-recipes/blob/main/engine_car_type_demo.ipynb>`
        - This example uses Car data to demonstrate Howso's interpretability to understand why the predictions were made. We train Howso Engine to predict classes of vehicles, understand potential anomalies, investigate vehicles on a case-by-case basis, and review the data that contributed to the predictions.

15. :download:`Census <https://github.com/howsoai/howso-engine-recipes/blob/main/engine_predict_explain_show.ipynb>`
        - This example uses the Adult data set to demonstrate which cases and features contribute to predictions, anomalies analysis, and potential improvements to gain more insight into the data.

.. |tmk|    unicode:: U+02122 .. TRADEMARK SIGN