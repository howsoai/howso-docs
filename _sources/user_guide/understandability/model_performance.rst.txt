.. currentmodule:: howso.engine


Model Performance
=================

.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of evaluating the prediction performance of your :class:`~Trainee` using the Howso Engine.

Objectives: what you will take away
-----------------------------------
- **Definitions & an understanding** of residuals, MAE, and, Conditions using the Howso Engine.
- **How-To** retrieve the performance statistics that describe the Trainee's performance.

Prerequisites: before you begin
-------------------------------
- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have :doc:`loaded, configured, trained, and analyzed data <../basics/basic_workflow>`

Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover:

- :download:`Engine Intro <https://github.com/howsoai/howso-engine-recipes/blob/main/1-engine-intro.ipynb>`

Concepts & Terminology
----------------------

To understand this guide, we recommend being familiar with the following concepts:

- :ref:`trainee`
- :ref:`feature`
- :ref:`residual`

How-To Guide
------------
In any machine learning workflow, an important step is to evaluate the performance of the model. This remains
true when using the Howso Engine, but we would like to highlight :class:`~Trainee` functionality that helps gauge this
performance while lessening the required effort of the user.

Step 1 - Global Model Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most basic and quintessential measure of model performance and uncertainty within a :class:`~Trainee` are the feature residuals.
The :ref:`residual` is described in more detail in the terminology section, but in this
context, the feature residuals describe the average difference between the models prediction for a feature and the
true value. These values are also called the Mean Absolute Error (MAE).

Alternatively, :class:`~Trainee` s are also able to compute more traditional model performance statistics. Some of the most obvious
of which include accuracy, precision, recall, and :math:`R^2`. These performed on a per-feature basis just as residuals.

.. note::

    Metrics like accuracy, precision, and recall computed through :meth:`~Trainee.react_into_trainee` are
    computed using a leave-one-out approach. This is notably different from the more traditional train-test split
    that is commonly used in deep-learning paradigms. Evaluating a Trainee using a train-test split is possible,
    but will likely yield different results than using :meth:`~Trainee.react_into_trainee`.

One important detail of how :class:`~Trainee` s evaluate performance is that these performance statistics are computed once and
cached. Of course, they can be computed as often as the user would like, but these operations are expensive due to
the instance-based learning approach embraced by the Howso Engine. The computation and caching of these performance
statistics take place through calls to :meth:`Trainee.react_into_trainee`, which takes boolean parameters indicating which
groups of statistics the user would like to compute and cache. Then to retrieve these statistics, the user makes a call to
:meth:`Trainee.get_prediction_stats`.

So, for example, to see a collection of performance statistics about the accuracy of predictions on each feature,
the user would do the following:

.. code-block:: python

    trainee.react_into_trainee(residuals=True)
    performance_stats = trainee.get_prediction_stats()
    print(performance_stats)


Step 2 - Conditional Model Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Trainee is also able to compute and return performance statistics on subsets of the trained data that match a
certain set of conditions. For example, a user might want to investigate the performance of their Trainee on
cases that represent individuals over the age of 40. These conditioned prediction stats are not cached in the
Trainee, so the call to :meth:`~Trainee.react_into_trainee` is unnecessary. Instead, the user can directly call
:meth:`~Trainee.get_prediction_stats` while passing the `condition` parameter.

The user from the example would want to do the following:

.. code-block:: python

    # Conditions for continuous features take a tuple
    # that represents the range of the condition.
    performance_stats = trainee.get_prediction_stats(condition={"age": [40, 9999]})
    print(performance_stats)

These conditions can even be much more elaborate. For example a user could be interested in the performance
on cases that represent individuals over the age of 40, who are also married and unemployed.

.. code-block:: python

    # Conditions for continuous features take a tuple
    # that represents the range of the condition.
    performance_stats = trainee.get_prediction_stats(
        condition={
            "age": [40, 9999],
            "marital-status": "married",
            "job-status": "unemployed",
        }
    )
    print(performance_stats)

API References
--------------
- :meth:`Trainee.react_into_trainee`
- :meth:`Trainee.get_prediction_stats`
