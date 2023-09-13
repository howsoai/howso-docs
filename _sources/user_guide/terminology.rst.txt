.. _terminology:

Terminology
===========

Concepts
^^^^^^^^

Howso's |tmk| technology operates a little differently than traditional machine learning (ML) systems and thus certain terminology is
specific to Howso.

Included below are some core concepts and details on how to use them.


Trainee
-------

A collection of cases that comprise knowledge. In traditional ML, this is typically referred to as a model, but a
Trainee may additionally include metadata, parameters, details of feature attributes, and data lineage and provenance.

Feature
-------

An individual metric, property, or characteristic that can be observed. A feature is generally referred to by its name,
which is generally a mnemonic string or phrase. Features are often numbers, but can also be strings, dates, or other
data. The feature may be described by feature attributes, which may include ranges, whether it is cyclic, allowed
values, etc. In database and spreadsheet terms, features are often referred to as columns.

For more information, see :doc:`Feature Attributes <feature_attributes>`

Value
-----

The number, string, or other value representing a measurement, expectation, observation, choice, attribute, prediction, or
other input or output that corresponds to a particular feature. If a value is an input to train a supervised learning to
make a prediction, this is sometimes referred to in the literature as a "label" representing "labeled data".

Context Features
----------------

A set of features that is used to describe values being used for input, observation, or other computation. In
traditional ML this is often referred to as input features, or sometimes just features.

Action Features
---------------

A set of features that is used as to describe values for output of a Trainee when it reacts, which is often as a
response to input Context Features. In traditional supervised ML this is often referred to as targets, target features,
or labels, and in generative ML, Action Features are the resulting data.

Derived Features
----------------

A feature that is derived via a function which operates on one or more other features rather than something that is measured
directly.  Derived features are described by a type and a derived feature code, which is a snippet of Amalgam-like code that
will be used to derive the feature values.  For example, if a dataset contains `mass`, `acceleration`, and `force` features,
the force feature may be derived from the product of `mass` and `acceleration`.  Time-series features, particular deltas, rates,
and lags, are also derived features.

For more information, see :doc:`Feature Attributes <feature_attributes>`,
the `Amalgam Language documentation <https://htmlpreview.github.io/?https://github.com/howsoai/amalgam/blob/main/doc/Language.html>`_ ,
and the `Derived Features user guide <derived_features>`_ .

Case
----

A set of feature values representing a situation observed. For supervised learning, this may be thought of as a set of
context features and action features, and for unsupervised learning, this may be thought of just a set of features,
though to the Trainee, they are all just feature values. In database or spreadsheet terms, this would be a row of
values.

Training Session
----------------

A set of cases that is added to a Trainee from a source in a sequential order. Multiple sessions can be added to a
Trainee either all at once or periodically added over time. May include metadata and can be queried and referenced by
id which is useful for auditability for the lineage and/or provenance of the data.

Residual
--------

The mean absolute error between a predicted value and actual value for a prediction which characterizes the model's
uncertainty. Residuals may be for a given prediction, and expected Residuals may be for a given feature, either
globally across the entire model or for a particular prediction.

Contribution
------------

Feature contribution is the difference between a prediction in an action feature when each feature or case is
considered versus not considered. Case contribution is the same but for a case rather than a feature. When applied in
a robust fashion, this is an approximation of the commonly used SHAP feature importance measure. The difference being
that SHAP is an exact value of a model (which itself is an approximation) whereas robust contribution is an
approximation of the feature importance of the relationships expressed in the data.

MDA
---

The *Mean Decrease in Accuracy* of an Action Feature when each feature or case is considered versus not considered.

Robust
------

A feature or case contribution or MDA that is robust means that it is computed over the power set of possible
combinations of features or cases, as approximated by a uniform distribution. For feature contributions, robust means
it is an approximation to the well-known SHAP values.

Relevant Features
-----------------

Features whose values were important in determining prediction value(s). Generally, this refers to feature MDA or
contribution, which yield similar but complementary insights.

Contexts
--------

The cases used to make a prediction or to derive a result.

Uncertainty
-----------

`Uncertainty <https://en.wikipedia.org/wiki/Measurement_uncertainty>`_ is an expression of the measurement error of
a particular feature.  One example of an uncertainty measure is the standard deviation of a distribution.  When Howso
Engine computes distances between one or more missing values, they are treated as having maximal uncertainty for
the feature.


Operations
^^^^^^^^^^

Train
-----

Introduce one or more cases to the Trainee which may result in the Trainee being updated. It is a single training step;
it may happen at each decision, at a certain sampling rate of observations per second, at certain events, or all at once.

Analyze
-------

Evaluate and update uncertainties about the data for use in future queries, as well as tune internal parameters to
improve performance and accuracy of predictions and analysis.

React
-----

Querying the Trainee for some response, potentially for a given set of context feature values, whether to determine
action features, or to determine other details. This is the primary verb that can encompass supervised learning
(e.g., with context features being the input features and action features being the prediction), unsupervised learning
(e.g., determining surprisal values or convictions from a set of context feature values), generative outputs via a
conviction value (e.g., specifying only action features, or doing conditioned generative outputs via context and action
features), and to determine various interpretations, explanations, and support data for any reaction.

Synthesize
----------

Generate synthetic cases from an existing Trainee using react.


Conviction
^^^^^^^^^^

Howso's algorithms can measure the "conviction" of different measures by using the computed ratio of the expected
surprisal over the actual surprisal. The range is 0 to infinity. A value of 1 is average - therefore a conviction of
less than 1 means it is more surprising than typical data. The higher the number above one, the less surprising it is.


Familiarity Conviction
----------------------

How confident or familiar the Trainee is in some data that it has been trained on, as determined by the KL Divergence
of how the particular data affects the probability density function of the data. The lower the conviction, the less
familiar the system is with the result, so 0.01 corresponds to 'no idea, but this is unusual', 2 corresponds to
'decently familiar'. Low values can also be used to determine when further training is needed to improve the Trainee's
ability to provide accurate results.

Distance Contribution
---------------------

The expected total surprisal contribution for a case. How much distance (or knowledge) a case adds to the model where
the distance is measured in surprisal.

Similarity Conviction
---------------------

How similar a case is in distance compared to other cases in the local model. For example, in a uniformly dense model a case
that is very close to another case will have very high prediction similarity conviction, where a case that is far away
will have lower prediction similarity conviction. For any given case, this is the ratio of the expected distance
contribution of the local model divided by the actual case distance contribution.

Prediction Residual Conviction
------------------------------

The amount of surprisal in the uncertainty of a prediction. This is the ratio of the expected model residual divided by
the computed prediction residual that, due to some unique properties of the underlying uncertainty mathematics, ends up
being a ratio of surprisal values. Howso computes the prediction residual via approximation by computing the actual
residuals for the cases in the local area around that prediction.


Interpretability, Explainability, and Auditability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When reacting to a context, by setting the appropriate parameters, you can see exactly why decisions were made in the
resulting explanation. Below are specific details about each set of information provided.


Outlying Feature Values
-----------------------

Feature values from the reaction case that are below the minimum or above the maximum value of similar cases that were
identified during a prediction.

Observational Errors
--------------------

Known observational feature errors or uncertainties as defined by the user; errors in the input measurements. For
example, a value of 2 for a feature called "degrees", which references temperature taken by a thermometer.

Most Similar Cases
------------------

The cases which are most similar to another case or a prediction.

Influential Cases
-----------------

The cases which were identified as most influential during a prediction, along with their weights when predicting the
expected value or drawing a value from the distribution of expected values for generative outputs.

Boundary Cases
--------------

Cases that are the most similar to the Context Feature values that has maximally different values for Action Features.
For example, if the prediction for a fruit type was a "peach", a boundary case might be a very peach-looking "apple" or
"nectarine".

Categorical Action Probabilities
--------------------------------

For categorical features, shows the probability that each of the specified category values would be the correct prediction.

Hypothetical Values
-------------------

Values which are used to show how a prediction could change in a what-if scenario where the influential cases' context
feature values are replaced with the specified values.

Distance Ratio
--------------

The ratio of distance between a prediction and its nearest case to the minimum distance in between the closest two cases in the local area.

.. |tmk|    unicode:: U+02122 .. TRADEMARK SIGN
