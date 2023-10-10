Key Concepts
========

Technological Differentiators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instance-Based Learning (IBL)
-----------------------------

In a typical data-driven modeling workflow, such as a deep neural network, a model is an abstraction of relationships within data used to make predictions on new information.
By nature, these models are very complicated (“black box”), and their predictions cannot be mapped back to original data, making them inherently unexplainable.

By contrast, Howso Engine is rooted in instance-based learning (IBL), which is truly data-centric analysis. As an IBL platform Howso stores your data in memory and makes predictions
from the similarities and differences between data points, not an underlying black box model, leading to fully transparent decisions.

Howso utilizes cutting edge advances in spatial query systems and information probability theory to make IBL practical in the modern world. These technological
advances enable all of Engine's insight and analysis capabilites. 

Fully Understandable Predictions
--------------------------------

Because IBL is data-centric, it enables state-of-the-art understandability. As such, with Howso you can identify the
specific data influencing your decisions, how individual features drive outcomes, and the confidence Howso has in the accuracy of its predictions.​

- Rank order which data points contributed the most to your decisions.​

    Unlike other machine learning tools, Howso calculates how much influence each original data point has on a prediction. This influence is related to the probability that the data point is representative of
    the prediction. Influence weights are computed across all features and then aggregated per data point; the most influential data have the highest total influence weights. Being able to see the influence of each data point
    on a decision provides direct evidence for why a decision was made. 

- Outperform other commonly used feature importance metrics, including SHAP. ​

    Howso quantifies individual feature contributions to a prediction, i.e., how much an individual feature impacts a prediction. The concept of feature contribution is similar to the data science concept of "feature importance". However,
    Howso is robust against several common challenges (correlated features, redundant features, difference in scale between features, and multiple distinguishing features) faced by other feature importance tools, 
    including the SHAP metric, which often lead to misleading results.

- Know Engine's confidence in each decision.​

    Other AI hallucinates, predicting false information with high confidence, because it can't accurately calculate uncertainties. Howso understands what it should know about the uncertainty of the data, and uses
    that to inform what it actually does know about the data. This enables Howso to provide accurate "confidence metrics" for decisions, so its clear when the data are insufficient to give a trustworthy answer.

Conviction
----------

Howso bridges IBL and information theory and the link becomes apparent in the concept of **conviction**, which is a measure of surprisal. Surprisal is a concept of information theory that describes how likely an event
will be. For example, if event A has a smaller probability of occurring than event B, you would be surprised if event A occurs. Howso's surprisal metric (conviction) is the computed ratio of actual information to
expected information, i.e., a measure of how surprising an event is given what is expected to occur. Conviction has a range of zero to infinity. A conviction value of one is average, as the actual information is
equal to the expected information. Convictions less than one indicate higher surprisal, as the actual information
is less than the expected information, while convictions greater than one indicate lower surprisal, since the actual information is higher than the expected information.

Actual information is the amount of information that a data point actually adds when it is evaluated. Expected information is what the value of a new data point should be on average, given
all knowledge of the data. 
The concept of surprisal,
quantified by conviction, is prevalent throughout many of Howso's analysis capabilities and can be adapted for a variety of tools and use cases.

Targeted *and* Targetless Analysis
--------------------------------

- **Targeted**

    Most modeling workflows require a set of one or more independent input variables (or features) and output a set of one or more variables that depend on the input. Often, these outputs, which are the
    values you want to generate or predict, are called "target" features. Workflows which predict target features are a type of *targeted*, or supervised, analysis. Howso performs targeted analysis when the user specifies `context features`, or input features, and `action features`, or target features, in the `analyze()` call. When a targeted analysis is specified, Howso specifically optimizes its
    underlying IBL algorithm to perform well at predicting the action features, enabling excellent model performance and low error predictions.

- **Targetless**

    In contrast to targeted predictions, because of Howso's data-centric nature, context (input) and action (output/target) features do not need to be specified, and *targetless* analysis can be performed. Targetless
    analysis means that predictions can be made about any features, given the other features; this allows the user to easily predict a variety of features without specifying new inputs and outputs. 
    Howso performs targetless analysis by default for all predictions.

