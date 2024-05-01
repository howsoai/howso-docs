.. currentmodule:: howso.engine

Global vs Local
===============
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of global vs local metrics.

Objectives: what you will take away
-----------------------------------
- **How-To** retrieve global and local metrics.

Prerequisites: before you begin
-------------------------------
- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding of :doc:`global vs local <../concepts/global_vs_local>` metrics.

Data
----
Our example dataset for this recipe is the well known ``Adult`` dataset. It is accessible via the `pmlb <https://github.com/EpistasisLab/pmlb>`__ package installed earlier. We use the ``fetch_data()`` function to retrieve the dataset in Step 1 below.


Concepts & Terminology
----------------------
Howso Engine is a generalized Machine Learning (ML) and Artificial Intelligence platform that creates powerful decision-making models that are fully explainable, auditable, and editable. Howso Engine uses Instance-Based Machine Learning which stores instances, i.e., data points, in memory and makes predictions about new instances given their relationship to existing instances. This technology harnesses a fast spatial query system and information theory for performance and accuracy.

- :ref:`trainee`
- :ref:`react`

How-To Guide
------------

Setup
^^^^^
The user guide assumes you have create and setup a :class:`~Trainee` as demonstrated in :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
The :class:`~Trainee` will be referenced as ``trainee`` in the sections below.

Global metrics
^^^^^^^^^^^^^^

Global metrics in Howso are calculated internally using a leave one out approach to the datapoints trained into the trainee that is 
called by the :meth:`~Trainee.react_in_trainee` method. 

.. code-block:: python

    # Getting global feature contributions
    t.react_into_trainee(action_feature=action_features[0], residuals=True)
    stats = t.get_prediction_stats()
    feature_contribution = stats["contribution"]

Local metrics
^^^^^^^^^^^^^
Local metrics are calcluated using the local space of the provided case(s). These cases may either be new cases or existing cases.
Local metrics are controlled through the ``details`` parameter in :py:meth:`Trainee.react`.

.. code-block:: python

    details = {"feature_contributions" : True}
    # Getting global feature contributions
    results = t.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=details
    )    

    feature_contributions = results['details']['feature_contributions']


API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.react_into_trainee`
- :py:meth:`Trainee.react`
