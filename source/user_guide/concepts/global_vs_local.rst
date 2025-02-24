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
Global metrics in Howso refers to calculations done using all of the cases available. Sometimes they are sampled for efficiency, however they are still representative of
the overall Trainee.

Global metrics in Howso are calculated internally using a leave one out approach to the datapoints trained into the trainee that is
called by the :meth:`~Trainee.react_aggregate` method.

.. code-block:: python

    # Getting global prediction contributions
    feature_robust_prediction_contributions = trainee.react_react_aggregate(
        action_feature=action_features[0],
        details={"feature_robust_prediction_contributions": True}
    )

Local metrics
^^^^^^^^^^^^^
Local metrics in Howso refers to calculations done using all of the cases available. Local metrics are calculated using the local space of the provided case(s). These cases may either be new cases or existing cases.
The local space refers to the set of closest cases to the provided case(s). While the exact number of cases that consists of the local space varies depending on several factors, generally it includes at least 30 cases if there is enough cases.

Local metrics are controlled through the ``details`` parameter in :py:meth:`Trainee.react`.

.. code-block:: python

    details = {'feature_robust_prediction_contributions' : True}
    # Getting global prediction contributions
    results = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=details
    )

    feature_contributions = results['details']['feature_robust_prediction_contributions']


API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
- :py:meth:`Trainee.react_aggregate`
