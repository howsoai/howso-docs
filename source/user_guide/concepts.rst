Concepts
===========

Instance-Based Learning (IBL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a typical data-driven modeling workflow, such as a deep neural network, a model is an abstraction of relationships within data used to make predictions on new information. 
By nature, these models are very complicated (“black box”), and their predictions cannot be mapped back to original data, making them inherently unexplainable. 

By contrast, Howso’s Understandable AI is rooted in instance-based learning (IBL), and the data is the model. Howso stores data in memory and makes predictions 
from the similarities and differences between data points, not an underlying black box model, leading to fully transparent decisions.

Howso utilizes cutting edge advances in spatial query systems and information probability theory to make IBL practical, accurate, and robust to adversarial attacks. These technological 
advances enable insight into a prediction’s reliability and rigorous analysis of which features contribute most to a decision from the data itself, not just a model which may have abstracted
away relationships. Additionally, because IBL is data-centric, it can perform multiple tasks a priori, including supervised, reinforcement, and online learning, anomaly detection, and missing
and sparse data imputation. 

Targeted vs. Targetless Analysis
--------------------------------

- **Targeted**

    Most modeling workflows require a set of one or more input independent variables (or features) and output a set of one or more variables that depend on the input. Often, these outputs are called "target"
    variables or features; these are the variables you want to generate or predict, and this type of analysis is called *targeted*. For example, if you are trying to predict whether or not a patient has heart disease, the input variables to the model may include a patient's age,
    weight, gender, and cholesterol levels, and the model output, or target, would be a positive/negative prediction value. 
    
    Howso handles targeted analysis when the user specifies `context features`, or input features, and `action features`, or target features, in the `analyze()` call. When a targeted analysis is specified, Howso specifically optimizes its
    predictions to perform well at predicting the action features, enabling excellent model performance via low error predictions.

- **Targetless**

    In contrast to targeted predictions, because of Howso's IBL nature, context (input) and action (output, target) features do not need to be specified, and *targetless* analysis can be performed. Targetless
    analysis means that predictions can be made about *any* of the features, given the other features; this allows the user to easily predict a variety of features without specifying new inputs and outputs. For example,
    using the heart disease analysis described above, instead of always predicting a positive or negative diagnosis for a patient, you may instead want to predict other features, like cholesterol levels or weight,
    given all of the other features. Instead of re-training an entire model with these features as outputs, targetless analysis enables you to quickly switch between output features.

    Howso performs targetless analsysis by default for all predictions.

Fully Understandable Predictions
--------------------------------

Because IBL is truly data centric, you can directly audit influential data and features in your analysis with state-of-the-art interpretability. This enables fully Understandable AI. As such, you can identify the
specific data influencing your decisions, how individual features drive outcomes, and the confidence you should have in the accuracy of your predictions.​  

- Rank order which data points contributed the most to your decisions.​ 

    Unlike other machine learning tools, Howso calculates how much influence each original data point has on a prediction. This influence is related to the probability that the data point is representative of
    the prediction. Influence weights are computed across all features, and the most influential data have the highest total influence weights. Being able to see this influence provides evidence for why a decision 
    was made. 

- Feature contribution analyses outperform other commonly used metrics, including SHAP. ​ 

    Howso quantifies individual feature contributions to a prediction, i.e., how much an individual feature impacts a prediction. This is similar to the data science concept of "feature importance". Additionally, 
    Howso is robst against several common challenges (correlated features, multiple distinguishing features) faced by other feature importance tools, including the SHAP metric, which lead to misleading results. 

- Determine confidence level of each decision.​ 

    Because of its underlying IBL nature, Howso determines in which region of the original data a prediction is located. Depending on the density of that region, Howso can inform users of its confidence, or certainty,
    in its prediction. For example, if a prediction about a new data point is made based on a very dense region of original data, which contains a lot of information that influences the prediction, Howso's confidence
    in the prediction will be high. In contrast, if a prediction is made about a point located in a very sparse region of the data, which does not contain much information from which Howso can make a decision, Howso's 
    confidence will be low.

Conviction
----------

The connection between IBL and information theory becomes apparent in the concept of **conviction**, which is a measure of surprisal. Conviction is the computed ratio of actual information to expected information, with
a range of zero to infinity. A conviction value of one is average, as the actual information is equal to the expected information. Convictions less than one indicate higher surprisal, as the actual information
was less than the expected information, while convictions greater than one indicate lower surprisal, since the actual information was higher than the expected information. 

Actual information is the amount of information that a data point actually adds when it is evaluated. Expected information is what the value of a new data point should be, given
all knowledge of the data around it. For example, say you are again trying to determine whether new patients have heart disease, given an historical heart disease data point. A new data point is being analyzed.
This data point has features very similar to historical data with positive prediction status. Thus, its expected heart disease prediction value is positive. Its actual information, though, is the true information
about whether the patient has heart disease. If the patient does, in fact, have heart disease, then its conviction value would be around one, as its actual information is similar to its expected information.
However, if the patient actually does not have heart disease, its actual value is not what was expected, so the conviction would be low, indicating a surprising outcome. While this is an example, the concept of surprisal,
quantified by conviction, is prevalent throughout many of Howso's analysis capabilities and can be adapted for a variety of tools and use cases.

Basic Workflows
^^^^^^^^^^^^^^^

There are three main components of a Howso Engine workflow: building a `Trainee`, `analyzing` the data, and `reacting` to new data.

Trainee
-------

A `Trainee` is a collection of data, metadata, and hyperparameters upon which the IBL algorithm acts. This is analogous to a model in traditional machine learning settings, but is 
different in that it is the *actual data*, and not an abstract representation of the data.

Analyze
-------

Once a `Trainee` is built, i.e., the data is added, it is `analyzed` to understand the relationships between the individual data points. Here, the internal parameters describing these
relationships are tuned to improve performance and the accuracy of predictions and metrics. 

React
-----

Finally, after building the `Trainee` and `analyzing`, Howso Engine can be used for a variety of data-driven analysis applications. Typically, these applications involve
`reacting` to new data, which involves exposing the Trainee to new information and using the underlying IBL algorithm to make a prediction about that new information.
This is equivalent to predicting or labeling in many traditional machine learning workflows, although `reacting` can be used for a variety of analyses, in addition to the supervised
learning workflow described here.


