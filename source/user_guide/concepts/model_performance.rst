.. currentmodule:: howso.engine

Model Performance
=================
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of gauging model performance using the Howso Engine.

Objectives: what you will take away
-----------------------------------
- **How-To** gauge performance using Howso's native performance metrics.

Prerequisites: before you begin
-------------------------------
- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
- You have an understanding of :doc:`global vs local <../concepts/global_vs_local>` metrics.

Data
----
Our example dataset for this recipe is the well known ``Adult`` dataset. It is accessible via the `pmlb <https://github.com/EpistasisLab/pmlb>`__ package installed earlier. We use the ``fetch_data()`` function to retrieve the dataset in Step 1 below.


Concepts & Terminology
----------------------

- :ref:`trainee`
- :ref:`analyze`
- :ref:`react`
- :ref:`residuals`

How-To Guide
------------

Setup
^^^^^
The user guide assumes you have created and setup a :class:`~Trainee` as demonstrated in :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
The :class:`~Trainee` will be referenced as ``trainee`` in the sections below.

Global model performance
^^^^^^^^^^^^^^^^^^^^^^^^

Global performance is calculated by Howso internally using a leave one out approach to the datapoints trained into the trainee that is
called by the :meth:`~Trainee.react_in_trainee` method. By setting ``residuals`` to `True`, you can retrieve global
performance stats.

**Available Stats**

- continuous features: mean absolute error ("mae"), root mean squared error ("rmse"), r2 ("r2"), spearman coefficient ("spearman_coeff")
- nominal features: Matthews correlation coefficient ("mcc"), accuracy ("accuracy"), precision ("precision"), recall ("recall"), the confusion matrix ("confusion_matrix")

.. note::
    The string representation of each statistic is listed in the parenthesis.

.. code-block:: python

    prediction_stats = t.react_aggregate(
        details={"prediction_stats": True}
    )


Conditional Model Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Trainee is also able to compute and return performance statistics on subsets of the trained data that match a
certain set of conditions. For example, a user might want to investigate the performance of their Trainee on
cases that represent individuals over the age of 40. This is calculated through calling :meth:`~Trainee.react_aggregate`
while passing in a `action_condition` parameter in the `details` dictionary.

The user from the example would want to do the following:

.. code-block:: python

    # Conditions for continuous features take a tuple
    # that represents the range of the condition.
    performance_stats = t.react_aggregate(
        details={
            "prediction_stats": True,
            "action_condition": {"age": [40, 9999]}
        }
    )



These conditions can even be much more elaborate. For example a user could be interested in the performance
on cases that represent individuals over the age of 40, who are also married and unemployed.

.. code-block:: python

    # Conditions for continuous features take a tuple
    # that represents the range of the condition.
    performance_stats = trainee.react_aggregate(
        details={
            "prediction_stats": True,
            "action_condition": {
                "age": [40, 9999],
                "marital-status": "married",
                "job-status": "unemployed",
        }
    )

API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react_aggregate`
