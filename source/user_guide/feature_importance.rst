.. currentmodule:: howso.engine


Feature Importance
==================
.. topic:: What is covered in this user guide

    In this guide, you will learn how to retrieve the feature importance metrics, :ref:`Feature Contributions <user_guide/terminology:Contribution>` and :ref:`Feature Mean Decrease in Accuracy (MDA) <user_guide/terminology:MDA>` from a Trainee. Feature importance metrics
    provides information about which features are useful for predicting a target or :ref:`action <user_guide/terminology:Action Features>` feature. In addition to learning informative metrics about the data and the model, these insights can be used as guidance for further action such as feature selection or feature engineering.


Objectives
----------
- **Definitions & Understanding** Difference between global vs local, and robust vs non-robust :ref:`Feature Contributions <user_guide/terminology:Contribution>` and :ref:`Feature MDA <user_guide/terminology:MDA>`.
- **How-To** obtain both feature importance metrics.
- **API References** How to use :meth:`Trainee.get_prediction_stats`, :py:meth:`Trainee.react`.


Prerequisites: before you begin 
-------------------------------
- You have successfully :doc:`installed Howso Engine <installing>`
- You have :doc:`loaded, configured, trained, and analyzed data <basic_workflow>`


Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover:

- :download:`Interpretability </_assets/recipes/2-interpretability.ipynb>`


Concepts & Terminology
----------------------
The main piece of terminology this guide introduces is the concept of Feature Importance. To understand this, we
recommend being familiar with the following concepts:

- :ref:`Trainee <user_guide/terminology:trainee>`
- :ref:`React <user_guide/terminology:react>`
- :ref:`Feature <user_guide/terminology:feature>`
- :ref:`Action Features <user_guide/terminology:action features>`
- :ref:`Context Features <user_guide/terminology:context features>`
- :ref:`Feature Contributions <user_guide/terminology:Contribution>`
- :ref:`Feature MDA <user_guide/terminology:MDA>`
- :doc:`Feature Attributes <feature_attributes>`


Local vs Global
^^^^^^^^^^^^^^^
Feature Contributions and Feature MDA can be calculated and retrieved both locally and globally. Conceptually, global metrics are measured using all of the cases in the Trainee, while local metrics use either a specific subset of those cases or a set of new cases and calculates the metrics using cases most similar to those specified cases.  

- **Local** :py:meth:`Trainee.react` along with the ``details`` parameter can be used for local metrics.
- **Global**  :py:meth:`Trainee.react_into_trainee` along with :py:meth:`Trainee.get_prediction_stats` are used for global metrics.


Robust vs Non-Robust
^^^^^^^^^^^^^^^^^^^^
In order to calculate feature importance, Howso Engine measures the impact on the prediction by comparing predictions with and without the feature. The feature set without the feature of interest may include either all of the other features, or a combination of features that 
may include any number of other features. Non-robust calculations use a leave-one-out approach to calculate these metrics, thus the metrics reflect the results when all features expect the feature of interest is used. Robust feature contributions instead sample from
the power set set of all combinations of features without the feature of interest. Robust metrics are recommended as they encompass a greater variety of feature sets, and they include a calculation performance boost as the number of features increases.

How-To-Guide
------------


Global Feature Importance
^^^^^^^^^^^^^^^^^^^^^^^^^
To get global feature importance metrics, :py:meth:`Trainee.react_into_trainee`, is first called on a trained and analyzed Trainee. :py:meth:`Trainee.react_into_trainee` calls react internally on the cases already trained into the Trainee and calculates the metrics. In this method, the desired metrics can be selected as parameters. These parameters are named indivdiually
and setting them to ``True`` will cache the desired metrics. For example, ``mda_robust`` and ``contributions_robust`` will calculate the robust versions of MDA and Feature Contributions, while ``mda`` and ``contributions`` will calculate the non-robust versions. 

.. code-block:: python
    :caption: Global Feature Importance Calculation Example:

    t.react_into_trainee(
        context_features=context_features,
        action_feature=action_features[0],
        mda_robust=True,
        contributions_robust=True
    )

In order to extract the metrics, :py:meth:`Trainee.get_prediction_stats` is called. An action feature must be specified, and the ``stats`` parameter is used determine which metrics to return. The ``stats`` parameter takes a list, so multiple
metrics may be specified together, but for this example they are separated. If robust metrics are calculated, then the ``robust`` parameter must be set to ``True`` to retrieve these metrics. If non-robust metrics are calculated, then the ``robust`` parameter can be set to the default value.

.. code-block:: python
    :caption: Global Feature Importance Extraction Example:

    robust_feature_contributions = t.get_prediction_stats(action_feature=action_features[0], robust=True, stats=['contribution'])
    robust_feature_mda = t.get_prediction_stats(action_feature=action_features[0], robust=True, stats=['mda'])

Local Feature Importance
^^^^^^^^^^^^^^^^^^^^^^^^
To get local feature importance metrics, :py:meth:`Trainee.react`, is first called on a trained and analyzed Trainee. In this method, the desired metrics, ``feature_contributions`` and ``feature_mda``, can be selected as inputs to the ``details`` parameters as key value pairs from a dictionary. These parameters are named individually
and setting them to ``True`` will calculate the desired metrics. To calculate the robust versions, ``robust_computation`` is set to True.  

.. code-block:: python
    :caption: Local Feature Importance Calculation Example:

    details = {
        'robust_computation':True,
        'feature_contributions':True,
        'feature_mda':True,
    }

    results = t.react(
        df, 
        context_features=context_features, 
        action_features=action_features,
        details=details
    )

In order to retrieve the calculated stats, they can be retrieved from the :py:meth:`Trainee.react` output dictionary. They are stored under the ``explanation`` key under the name of the metric. Whether these metrics are robust or non-robust is determined when the metrics
are calculated in :py:meth:`Trainee.react` from the previous step.

.. code-block:: python
    :caption: Global Feature Importance Extraction Example:

    robust_feature_contributions = results['explanation']['feature_contributions']
    robust_feature_contributions = results['explanation']['feature_mda']


.. warning::

    Contributions and MDA are also metrics for cases and not just features, so please be aware when reading other guides that may use those terms.


Example Use-Cases
^^^^^^^^^^^^^^^^^
In addition to the examples above, here are a few example use-cases for feature importance.

- Bias Determination
    - e.g., determing which features are important to your model to gauge the possibility of bias in the model.
- Reducing :class:`~Trainee` size
    - By strategically removing unimportant features, information can be maintained while the size of the :class:`~Trainee`
      is decreased


API References
--------------
- :meth:`Trainee.react`
- :meth:`Trainee.react_into_trainee`
- :meth:`Trainee.get_prediction_stats`

