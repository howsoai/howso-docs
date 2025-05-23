Terminology
===========

Concepts
^^^^^^^^

Howso's™ technology operates a little differently than traditional machine learning (ML) systems and thus certain terminology is
specific to Howso.

Included below are some core concepts and details on how to use them.

.. _trainee:

Trainee
-------

A collection of cases that comprise knowledge. In traditional ML, this is typically referred to as a model, but a
Trainee may additionally include metadata, parameters, details of feature attributes, and data lineage and provenance.

.. _feature:

Feature
-------

An individual metric, property, or characteristic that can be observed. A feature is generally referred to by its name,
which is generally a mnemonic string or phrase. Features are often numbers, but can also be strings, dates, or other
data. The feature may be described by feature attributes, which may include ranges, whether it is cyclic, allowed
values, etc. In database and spreadsheet terms, features are often referred to as columns.

For more information, see :ref:`feature_attributes`

.. _value:

Value
-----

The number, string, or other value representing a measurement, expectation, observation, choice, attribute, prediction, or
other input or output that corresponds to a particular feature. If a value is an input to train a supervised learning to
make a prediction, this is sometimes referred to in the literature as a "label" representing "labeled data".

.. _context_features:

Context Features
----------------

A set of features that is used to describe values being used for input, observation, or other computation. In
traditional ML this is often referred to as input features, or sometimes just features.

.. _action_features:

Action Features
---------------

A set of features that is used as to describe values for output of a Trainee when it reacts, which is often as a
response to input Context Features. In traditional supervised ML this is often referred to as targets, target features,
or labels, and in generative ML, Action Features are the resulting data.

.. _derived_features:

Derived Features
----------------

A feature that is derived via a function which operates on one or more other features rather than something that is measured
directly.  Derived features are described by a type and a derived feature code, which is a snippet of Amalgam-like code that
will be used to derive the feature values.  For example, if a dataset contains `mass`, `acceleration`, and `force` features,
the force feature may be derived from the product of `mass` and `acceleration`.  Time-series features, particular deltas, rates,
and lags, are also derived features.

For more information, see :ref:`feature_attributes`,
the `Amalgam Language documentation <https://htmlpreview.github.io/?https://github.com/howsoai/amalgam/blob/main/doc/Language.html>`_,
and the `Derived Features user guide <derived_features>`_.

.. _case:

Case
----

A set of feature values representing a situation observed. For supervised learning, this may be thought of as a set of
context features and action features, and for unsupervised learning, this may be thought of just a set of features,
though to the Trainee, they are all just feature values. In database or spreadsheet terms, this would be a row of
values.

.. _training_session:

Training Session
----------------

A set of cases that is added to a Trainee from a source in a sequential order. Multiple sessions can be added to a
Trainee either all at once or periodically added over time. May include metadata and can be queried and referenced by
id which is useful for auditability for the lineage and/or provenance of the data.

.. _residual:

Residual
--------

The mean absolute error between a predicted value and actual value for a prediction which characterizes the model's
uncertainty. Residuals may be for a given prediction, and expected Residuals may be for a given feature, either
globally across the entire model or for a particular prediction.

.. _pc:

Prediction Contributions (PC)
-----------------------------

Prediction contributions is the measured difference between a prediction in an action feature when each feature (Feature Prediction Contributions)
or case (Case Prediction Contributions) is considered versus not considered. When Feature Prediction Contributions is applied in
a robust fashion, this is an approximation of the commonly used SHAP feature importance measure. The difference being
that SHAP is an exact value of a model (which itself is just an approximation of the data) whereas robust contribution is an
approximation of the feature importance of the relationships expressed in the data.

.. _ac:

Accuracy Contributions (AC)
---------------------------
Accuracy contributions is the accuracy difference in an action feature when each feature (Feature Accuracy Contributions)
or case (Case Accuracy Contributions) is considered versus not considered.

.. _robust:

Robust
------

A feature or case contribution that is robust means that it is computed over the power set of possible
combinations of features or cases, as approximated by a uniform distribution. For prediction contributions, robust means
it is an approximation to the well-known SHAP values.

.. _relavant_features:

Relevant Features
-----------------

Features whose values were important in determining prediction value(s). Generally, this refers to prediction or accuracy contributions, which yield similar but complementary insights.

.. _contexts:

Contexts
--------

The cases used to make a prediction or to derive a result.

.. _uncertainty:

Uncertainty
-----------

`Measurement Uncertainty
<https://en.wikipedia.org/wiki/Measurement_uncertainty>`_ is an expression of
the measurement error of a particular feature.  One example of an uncertainty
measure is the standard deviation of a distribution.  When Howso Engine
computes distances between one or more missing values, they are treated as
having maximal uncertainty for the feature.

.. _operations:

Operations
^^^^^^^^^^

.. _train:

Train
-----

Introduce one or more cases to the Trainee which may result in the Trainee being updated. It is a single training step;
it may happen at each decision, at a certain sampling rate of observations per second, at certain events, or all at once.

.. _analyze:

Analyze
-------

Evaluate and update uncertainties about the data for use in future queries, as well as tune internal parameters to
improve performance and accuracy of predictions and analysis.

- **Targeted**

  Most modeling workflows require a set of one or more independent input variables (or features) and output a set of one or more variables that depend on the input. Often, these outputs, which are the
  values you want to generate or predict, are called "target" features. Workflows which predict target features are a type of *targeted*, or supervised, analysis. Howso performs targeted analysis when the user specifies `context features`, or input features, and `action features`, or target features, in the `analyze()` call.
  When a targeted analysis is specified, Howso specifically optimizes its
  underlying IBL algorithm to perform well at predicting the action features, enabling excellent model performance and low error predictions.

- **Targetless**

  In contrast to targeted predictions, because of Howso's data-centric nature, context (input) and action (output/target) features do not need to be specified, and *targetless* analysis can be performed. Targetless
  analysis means that predictions can be made about any features, given the other features; this allows the user to easily predict a variety of features without specifying new inputs and outputs.
  Howso performs targetless analysis by default for all predictions.

.. _react:

React
-----

Querying the Trainee for some response, potentially for a given set of context feature values, whether to determine
action features, or to determine other details. This is the primary verb that can encompass supervised learning
(e.g., with context features being the input features and action features being the prediction), unsupervised learning
(e.g., determining surprisal values or convictions from a set of context feature values), generative outputs via a
conviction value (e.g., specifying only action features, or doing conditioned generative outputs via context and action
features), and to determine various interpretations, explanations, and support data for any reaction.

.. _synthesize:

Synthesize
----------

Generate synthetic cases from an existing Trainee using react.


.. _conviction:

Conviction
^^^^^^^^^^

Howso bridges instance-based learning with information theory by harnessing the concept of "surprisal" which quantifies the surprise of an event being observed. For example, if an event has a probability of one
(i.e., it is certain to occur),
the event is unsurprising and yields no new information. However, as the probability of an event decreases, it becomes more surprising and yields more information.

As an analogy, imagine you are watching a
professional magician's show. The magician performs many tricks (or ~illusions~) that may seem impossible. You purchased a ticket to the show because the astonishment of each "big reveal" is
amusing to you. In less exciting terms, the magician makes tricks with an extremely low probability of occurring in every day life and you are highly surprised!

In addition to reporting exact surprisals, Howso calculates "conviction", or the ratio of an outcome's expected surprisal to actual surprisal. Conviction communicates surprisals of events relative to the
expected surprisal within the underlying data. This is useful for overcoming differences in scale between the surprisals of different quantities.
Conviction has a range of zero to infinity. A conviction value of one is average, as an outcome's actual surprisal is
equal to its expected surprisal. Convictions less than one indicate higher surprisal, as the actual surprisal
is more than the expected surprisal, while convictions greater than one indicate lower surprisal, since the actual surprisal is less than the expected surprisal.

Returning to our analogy, pretend now that you have now attended hundreds of magic shows and are familiar with pretty much all the tricks in the book. At this point, your expected surprisal is going to be very low because you've
"seen it all", as they say. Now, if you attend your five-year-old kid's magic show, the actual amount you are surprised is very low. So if Howso were to assign you a conviction at your kid's show, it would definitely be greater than one.
However, if you go to the show of the most outstanding magician in the world, who is an innovator constantly developing new tricks, you may actually still find yourself very surprised. In this case, your conviction
would be less than one because your actual surprisal is much greater than your expected surprisal.

Conviction is prevalent throughout many of Howso's analysis capabilities and the Howso Engine assesses the "conviction" of variety of different measures, which is discussed more below.
If you are interested in learning more about information theory and
surprisal, we recommend this `wikipedia article <https://en.wikipedia.org/wiki/Information_content>`_ as a good starting reference.


.. _familiarity_conviction:

Familiarity Conviction
----------------------

How confident or familiar the Trainee is in some data that it has been trained on, as determined by the KL Divergence
of how the particular data affects the probability density function of the data. The lower the conviction, the less
familiar the system is with the result, so 0.01 corresponds to 'no idea, but this is unusual', 2 corresponds to
'decently familiar'. Low values can also be used to determine when further training is needed to improve the Trainee's
ability to provide accurate results.

.. _distance_contribution:

Distance Contribution
---------------------

The expected total surprisal contribution for a case. How much distance (or knowledge) a case adds to the model where
the distance is measured in surprisal.

.. _similarity_conviction:

Similarity Conviction
---------------------

How similar a case is in distance compared to other cases in the local model. For example, in a uniformly dense model a case
that is very close to another case will have very high prediction similarity conviction, where a case that is far away
will have lower prediction similarity conviction. For any given case, this is the ratio of the expected distance
contribution of the local model divided by the actual case distance contribution.

.. _prediction_residual_conviction:

Prediction Residual Conviction
------------------------------

The amount of surprisal in the uncertainty of a prediction. This is the ratio of the expected model residual divided by
the computed prediction residual that, due to some unique properties of the underlying uncertainty mathematics, ends up
being a ratio of surprisal values. Howso computes the prediction residual via approximation by computing the actual
residuals for the cases in the local area around that prediction.

.. _interpretability_explainability_and_auditability:

Interpretability, Explainability, and Auditability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When reacting to a context, by setting the appropriate parameters, you can see exactly why decisions were made in the
resulting explanation. Below are specific details about each set of information provided.

.. _outlying_feature_values:

Outlying Feature Values
-----------------------

Feature values from the reaction case that are below the minimum or above the maximum value of similar cases that were
identified during a prediction.

.. _observational_errors:

Observational Errors
--------------------

Known observational feature errors or uncertainties as defined by the user; errors in the input measurements. For
example, a value of 2 for a feature called "degrees", which references temperature taken by a thermometer.

.. _most_similar_cases:

Most Similar Cases
------------------

The cases which are most similar to another case or a prediction as determined by the distance of the context features. Returns cases that are similar, regardless of their
influence.

.. _influential_cases:

Influential Cases
-----------------

The cases which were identified as most influential during a prediction, along with their weights when predicting the
expected value or drawing a value from the distribution of expected values for generative outputs. The influential
cases are a subset of the :ref:`most_similar_cases`, returning only those cases whose cumulative influence weights added in
descending order is below the influential weight threshold.

.. _boundary_cases:

Boundary Cases
--------------

Cases that are the most similar to the Context Feature values that has maximally different values for Action Features.
For example, if the prediction for a fruit type was a "peach", a boundary case might be a very peach-looking "apple" or
"nectarine".

.. _categorical_action_probabilities:

Categorical Action Probabilities
--------------------------------

For categorical features, shows the probability that each of the specified category values would be the correct prediction.

.. _hypothetical_values:

Hypothetical Values
-------------------

Values which are used to show how a prediction could change in a what-if scenario where the influential cases' context
feature values are replaced with the specified values.

.. _distance_ratio:

Distance Ratio
--------------

The ratio of distance between a prediction and its nearest case to the minimum distance in between the closest two cases in the local area.

.. |tmk|    unicode:: U+02122 .. TRADEMARK SIGN
