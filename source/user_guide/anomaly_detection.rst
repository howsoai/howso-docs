.. currentmodule:: howso.engine

Anomaly Detection
=================
.. topic:: What is covered in this user guide

    In this guide, you will learn the basics of anomaly detection using
    a :class:`~Trainee`

Objectives: what you will take away
-----------------------------------
- **Definitions & Understanding** of various :class:`~Trainee` metrics that be used to evaluate anomalies.
- **How-To** perform anomaly detection using a :class:`~Trainee`.
- **API References** How to use, :meth:`Trainee.react`, :meth:`Trainee.react_into_features`, and :meth:`Trainee.get_cases`.

Prerequisites: before you begin
-------------------------------
- You have successfully :doc:`installed Howso Engine <../getting_started/installing>`
- You have :doc:`loaded, configured, trained, and analyzed data <basic_workflow>`

Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover:

- :download:`Anomaly Detection <https://github.com/howsoai/howso-engine-recipes/blob/main/3-anomaly_detection.ipynb>`

Concepts & Terminology
----------------------
In order to perform anomaly detection, we utilize a few new metrics that are exposed through the :class:`~Trainee`.
To understand this, we recommend being familiar with the following concepts:

- :ref:`Trainee <../getting_started/terminology:trainee>`
- :ref:`React <../getting_started/terminology:react>`
- :ref:`Conviction <../getting_started/terminology:Conviction>`
- :ref:`Familiarity Conviction <../getting_started/terminology:Familiarity Conviction>`
- :ref:`Similarity Conviction <../getting_started/terminology:Similarity Conviction>`


We also recommend being familiar with the concept of `anomaly detection <https://en.wikipedia.org/wiki/Anomaly_detection>`_.

How-To Guide
------------
Anomaly detection, is one of the most significant domains of artificial intelligence and machine learning. Some of the most
common use cases of anomaly detection are fraud detection, health monitoring, and attack detection in cybersecurity. The
idea is to be able to detect data that doesn't seem to fit in with the rest of the observed data.

Detecting anomalies
^^^^^^^^^^^^^^^^^^^
To detect anomalies using the Howso Engine, we recommend the use of either Familiarity Conviction or Similarity Conviction.
Both of these metrics are forms of conviction, which makes them a ratio of surprisal. This ratio being an expected surprisal
divided by an observed surprisal.

These ratios are well designed for anomaly detection because cases which are not anomalous should have surprisals that are
close to the expected. Consequently, non-anomalies should be expected to have conviction values of around ~1.0. Any values
that deviate too far below or above 1.0 can be deemed as anomalies.


Determining anomalies among trained data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Computing conviction values for each case that has been trained in the model is very simple. To do this,
use :meth:`Trainee.react_into_features`. This method takes parameters for each feature the user can compute
and cache into each case. In the context of anomaly detection, the relevant parameters are
`similarity_conviction`, `familiarity_conviction_addition`, and `familiarity_conviction_removal`.

.. code-block:: python

    t.react_into_features(similarity_conviction=True)

This makes the :class:`Trainee` compute similarity conviction for every case in the model and cache the
values into each case. To then view all of the similarity conviction values, we recommend using
:meth:`Trainee.get_cases`:

.. code-block:: python

    t.get_cases(['similarity_conviction'])

Then with the similarity conviction values for each case, users can determine what thresholds are appropriate
to use for anomaly detection and begin classifying each case as anomalous or not.


Determining anomalies among unseen data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When performing anomaly detection on data not trained into the :class:`Trainee`, :meth:`~Trainee.react_into_features`
is not applicable. Instead, :meth:`Trainee.react` must be used. To get conviction values for unseen data with
:meth:`~Trainee.react`, the 'details' parameter must be passed as a dictionary with the desired conviction value
keywords as keys with 'True' values.

.. code-block:: python

    reaction = t.react(
        context_values,
        context_features=context_features,
        details={'similarity_conviction': True}
    )

    similarity_conviction = reaction['explanation']['similarity_conviction']


This is all that is necessary to get the similarity conviction for an unseen case from :class:`Trainee`.
If familiarity conviction is desired instead, the required calls are no different, but instead
'familiarity_conviction_addition' or 'familiarity_conviction_removal' must be specified instead of
'similarity_conviction'.

Once these values are computed for the cases in question, the conviction values can be compared to
predetermined thresholds that will determine if the case is classified as an anomaly.

Determining the threshold of conviction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Since conviction values are a ratio of surprisals, these values must be interpreted carefully.
Conviction values below 1.0 indicate cases that are more surprising than expected while values
above 1.0 indicate cases that are less surprising than expected.

However, these two sides are asymmetric. For example, a conviction of 0.5 is more anomalous than
a value of 1.5 due to the nature of ratios. We recommend using a threshold below 1.0 to determine
outliers that is determined through a series of experiments on a per-dataset basis. We find that
0.75 is a generally acceptable threshold for outlier detection, but encourage users to find the
best threshold for their data and use-case.

If inliers are of interest as well, then another threshold above 1.0 should be used to detect cases
with unexpectedly low surprisals.

API References
--------------
- :meth:`Trainee.react_into_features`
- :meth:`Trainee.get_cases`
- :meth:`Trainee.react`

