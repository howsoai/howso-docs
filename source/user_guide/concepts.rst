Concepts
===========

Instance-Based Learning (IBL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a typical data-driven modeling workflow, such as a deep neural network, a model is an abstraction of relationships within data used to make predictions on new information. 
By nature, these models are very complicated (“black box”), and their predictions cannot be mapped back to original data, making them inherently unexplainable. 

By contrast, Howso’s Understandable AI is rooted in instance-based learning (IBL), so the data is the model. Howso stores your data in memory and makes predictions 
from the similarities and differences between data points, not an underlying black box model, leading to fully transparent decisions.

Howso utilizes cutting edge advances in spatial query systems and information probability theory to make IBL practical, accurate, and robust to adversarial attacks. These technological 
advances enable insight including a prediction’s reliability and rigorous analysis of which features contribute most to a decision from the data itself, not just a model which may have abstracted
away relationships. Additionally, because IBL is data-centric, it can perform multiple tasks a priori, including supervised, reinforcement, and online learning, anomaly detection, and missing
and sparse data imputation, among others. 

Targeted vs. Targetless Analysis
--------------------------------

- **Targeted**

    Most modeling workflows require a set of one or more independent input variables (or features) and output a set of one or more variables that depend on the input. Often, these outputs, which are the 
    values you want to generate or predict, are called "target" variables or features. Workflows which predict target features are a type of *targeted*, or supervised, analysis. 
    An example of targeted analysis would be if you are a doctor building a model to predict whether or not your patient has heart disease. For this analysis, your model would learn information
    on heart disease diagnoses (the target feature), based on previous patient data, and then make predictions for new patients. Your target feature, or output of the model, would be a positive or negative heart disease 
    diagnosis prediction value. This target feature would depend on the input variables to the model,
    which may include a patient's age, weight, gender, and cholesterol levels. 
    
    Howso handles targeted analysis when the user specifies `context features`, or input features, and `action features`, or target features, in the `analyze()` call. When a targeted analysis is specified, Howso specifically optimizes its
    underlying IBL algorithm to perform well at predicting the action features, enabling excellent model performance via low error predictions.

- **Targetless**

    In contrast to targeted predictions, because of Howso's IBL data-centric nature, context (input) and action (output/target) features do not need to be specified, and *targetless* analysis can be performed. Targetless
    analysis means that predictions can be made about *any* features, given the other features; this allows the user to easily predict a variety of features without specifying new inputs and outputs. For example,
    using the heart disease analysis described above, instead of always predicting a positive or negative diagnosis for a patient, you may instead want to predict other features, like cholesterol levels or weight,
    given a subset of features including a patient's diagnosis, age, and gender. Targetless analysis enables you to quickly switch between output features instead of re-training an entire model with these features as outputs.

    Howso performs targetless analsysis by default for all predictions.

Fully Understandable Predictions
--------------------------------

Because IBL is data-centric, you can directly audit influential data and features in your analysis with state-of-the-art interpretability. This enables fully Understandable AI. As such, you can identify the
specific data influencing your decisions, how individual features drive outcomes, and the confidence Howso has in the accuracy of its predictions.​  

- Rank order which data points contributed the most to your decisions.​ 

    Unlike other machine learning tools, Howso calculates how much influence each original data point has on a prediction. This influence is related to the probability that the data point is representative of
    the prediction. Influence weights are computed across all features and then aggregated per data point; the most influential data have the highest total influence weights. Being able to see the influence of each data point
    on a decision provides direct evidence for why a decision was made. Using the heart disease prediction example above, if Howso provided a positive heart disease prediction for a patient, you as a doctor would be 
    able to print out the original data points that had the highest influence on the prediction. Then, you might see that these high influence data points showed similar health history to the patient for whom you are
    making a decision, providing confidence in your prediction. 

- Feature contribution analyses outperform other commonly used metrics, including SHAP. ​ 

    Howso quantifies individual feature contributions to a prediction, i.e., how much an individual feature impacts a prediction. Again, using the heart disease example, you as a doctor could use Howso's feature contribution
    tools to see that the features which had the most impact on a positive heart disease prediction might be cholesterol levels and weight. You could then use this knowledge to flag other patients with similar 
    cholesterol levels and weights as being likely to develop heart disease, and treat them accordingly.
    
    The concept of feature contribution is similar to the data science concept of "feature importance". However, 
    Howso is robust against several common challenges (correlated features, multiple distinguishing features) faced by other feature importance tools, including the SHAP metric, which often lead to misleading results.


- Determine confidence level of each decision.​ 

    Because of its underlying IBL nature, Howso determines in which region of the original data a prediction is located. Depending on the density of data in that region, Howso can inform users of its confidence, or certainty,
    in its prediction. Thus, if a prediction about a new data point is made based on a very dense region of original data, which contains a lot of information that influences the prediction, Howso's confidence
    in the prediction will be high. In contrast, if a prediction is made about a point located in a very sparse region of the data, which does not contain much information from which Howso can make a decision, Howso's 
    confidence will be low. In the heart disease patient example, if you are making a prediction about a patient who has very similar health information to many other patients with heart disease,
    Howso will be confident in its decision of a positive prediction. In contrast, you might have a patient who is extremely young and fit, but with high cholesterol levels, whose information doesn't match the information
    of many other patients. Even if Howso predicts a positive diagnosis for this young patient, because this patient's information is in such a sparse region of dataspace, Howso will tell you it has low confidence
    in its prediction, indicating further investigation may be necessary.

Conviction
----------

The connection between IBL and information theory becomes apparent in the concept of **conviction**, which is a measure of surprisal. Surprisal is a concept of information theory that describes how likely an event 
will be. For example, if an event A has a smaller probability of occurring than event B, you would be surprised if event A occurs. Howso's surprisal metric (conviction) is the computed ratio of actual information to 
expected information, i.e., a measure of how surprising an event is given what is expected to occur. Conviction has a range of zero to infinity. A conviction value of one is average, as the actual information is 
equal to the expected information. Convictions less than one indicate higher surprisal, as the actual information
iss less than the expected information, while convictions greater than one indicate lower surprisal, since the actual information is higher than the expected information. 

Actual information is the amount of information that a data point actually adds when it is evaluated. Expected information is what the value of a new data point should be on average, given
all knowledge of the data. For example, say you are again trying to make heart disease predictions, given historical heart disease data, and a new patient's data is being analyzed.
This patient's health history is very similar to other patients who had positive heart disease predictions. Thus, the patient would be expected to also have a positive heart disease prediction. 
The actual information, though, is the true information
about whether the patient has heart disease in real life. If the patient does, in fact, have heart disease, then the conviction value of the positive prediction would be around one,
as the patient's actual health information and diagnosis status are similar to what is expected.
However, if the patient actually does not have heart disease, the actual heart disease diagnosis prediction is not what was expected, so the conviction would be low, indicating a surprising outcome. 
While this is an example, the concept of surprisal,
quantified by conviction, is prevalent throughout many of Howso's analysis capabilities and can be adapted for a variety of tools and use cases.

Basic Workflows
^^^^^^^^^^^^^^^

There are three main components of a Howso Engine workflow: building a `Trainee`, `analyzing` the data, and `reacting` to new data.

Trainee
-------

A `Trainee` is a collection of data, metadata, and hyperparameters upon which the IBL algorithm acts. This is analogous to a model in traditional machine learning settings, but is 
different in that it is the *actual data*, stored in memory, and not an abstract representation of the data.

Analyze
-------

Once a `Trainee` is built, i.e., the data is stored, it is `analyzed` to understand the relationships between the individual data points. Here, the internal parameters describing these
relationships are tuned to improve performance and the accuracy of predictions and metrics. 

React
-----

Finally, after building the `Trainee` and `analyzing`, Howso Engine can be used for a variety of data-driven analysis applications. Often, these applications involve
`reacting` to new data, which involves exposing the Trainee to new information and using the underlying IBL algorithm to make a prediction about that new information.
This is equivalent to predicting or labeling in many traditional machine learning workflows, although `reacting` can be used to analyze data already added to the Trainee, in addition to supervised
learning workflows.


