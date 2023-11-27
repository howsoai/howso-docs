.. currentmodule:: howso.engine


Understanding Predictions
=========================
.. topic:: What is covered in this user guide

    In this guide, you will learn how to audit the cases in your Trainee, including determining which cases influence a specific prediction, as well as which cases influence the :class:`~Trainee` 's predictions as a whole.


Objectives: what you will take away
-----------------------------------
- **Definitions & Understanding** Difference between similar/influential cases
  vs case importance and robust vs non-robust :ref:`Case Contributions
  <contribution>` and :ref:`Case MDA <mda>`.
- **How-To** audit specific cases as well as determine which cases impact
  Trainee predictions.


Prerequisites: before you begin
-------------------------------
- You have successfully :doc:`installed Howso Engine <../getting_started/installing>`
- You have :doc:`loaded, configured, trained, and analyzed data <basic_workflow>`


Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover:

- :download:`Interpretability <https://github.com/howsoai/howso-engine-recipes/blob/main/2-interpretability.ipynb>`


Concepts & Terminology
----------------------
The main piece of terminology this guide introduces is the concept of case auditing. To understand this, we
recommend being familiar with the following concepts:

- :ref:`trainee`
- :ref:`react`
- :ref:`influential_cases`
- :ref:`most_similar_cases`
- :ref:`Case MDA <mda>`
- :ref:`Case Contributions <contribution>`


How-To Guide
------------


Influential Cases and Most Similar Cases
----------------------------------------

Howso allows the user to audit individual cases to determine the closest cases that may influence a prediction. **Most Similar Cases** allows the user to return a designated number of most similar cases,
while the **Most Influential Cases** only returns cases that have an influence on the prediction. If the desired number of most similar cases is greater than the number of most influential cases, then the most influential
cases is a subset of the most similar cases.

The parameters to get the most similar cases or influential cases can be accessed in the ``details`` parameter as a key value pair shown below. ``num_most_similar_cases`` allows the user to specify exactly how many similar cases to return.

.. code-block:: python

    details = {
        'influential_cases':True,
        'most_similar_cases':True,
        'num_most_similar_cases':20,
    }

    reaction = t.react(
        df,
        context_features=context_features,
        action_features=action_features,
        details=details
    )

In order to retrieve the calculated stats, they can be retrieved from the :py:meth:`Trainee.react` output dictionary. They are stored under the ``explanation`` key under the name of the metric.

.. code-block:: python

    influential = pd.DataFrame(reaction['explanation']['influential_cases'][0])
    most_similar_cases = pd.DataFrame(reaction['explanation']['most_similar_cases'][0])


Case Importance
---------------

As opposed to influential and similar cases which examines the influence of cases on a single case or prediction, case importance examines how important a case is in regards to the overall predictions on a group of cases. Case importance share the same underlying methodology with  :doc:`Feature Importance <feature_importance>`.
Unlike feature contributions, case contributions are calculated just locally. Conceptually, local metrics use either a specific subset of the cases that are trained into the Trainee or a set of new cases.

Robust vs Non-Robust
^^^^^^^^^^^^^^^^^^^^
In order to calculate case importance, Howso Engine measures the impact on the prediction by comparing predictions with and without the case. The case set without the case of interest may include either all of the other cases, or a combination of cases that
may include any number of other cases. Non-robust calculations use a leave-one-out approach to calculate these metrics, thus the metrics reflect the results when all cases except the case of interest is used. Robust case contributions compares the results from sampling from
the power set of all combinations with and without the case of interest. Robust metrics are recommended as they encompass a greater variety of case sets, and they include a calculation performance boost as the number of cases increases.


To get the case importance metrics, :py:meth:`Trainee.react`, is first called on a trained and analyzed Trainee. In this method, the desired metrics, ``case_contributions`` and ``case_mda``, can be selected as inputs to the ``details`` parameters as key value pairs from a dictionary. These parameters are named individually
and setting them to ``True`` will calculate the desired metrics. Robust computation is performed by default.

.. code-block:: python

    details = {
        'case_contributions':True,
        'case_mda':True,
    }

    reaction = t.react(
        df,
        context_features=context_features,
        action_features=action_features,
        details=details
    )

These metrics can be retrieved the same way as the method to retrieve the most similar cases. Whether these metrics are robust or non-robust is determined when the metrics
are calculated in :py:meth:`Trainee.react` from the previous step.

.. code-block:: python

    robust_case_contributions = reaction['explanation']['case_contributions']
    robust_case_contributions = reaction['explanation']['case_mda']


.. warning::

    Contributions and MDA are also metrics for features and not just cases, so please be aware when reading other guides that may use those terms.


Example Use-Cases
^^^^^^^^^^^^^^^^^
In addition to the examples above, here are a few example use-cases for for similar cases and case importance.

- Auditability and Tracing
    - e.g., determining which cases are important to the prediction to manually audit the prediction and learn why a prediction was made.
- Reducing :class:`~Trainee` size
    - By strategically removing unimportant cases, information can be maintained while the size of the :class:`~Trainee`
      is decreased


API References
--------------
- :meth:`Trainee.react`
