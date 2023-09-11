.. currentmodule:: howso.engine


Editing Trainees and Case Weighting
===================================
.. topic:: What is covered in this user guide

    In this guide, you will learn the basics of editing :py:class:`~Trainee` s and applying case
    weights to data contained within the Trainee.


Objectives
----------
- **Definitions & Understanding** of how :py:class:`~Trainee` s can be edited without re-training and what effects case-
  weighting can have on prediction.
- **How-To** remove, edit, and weigh cases in a :py:class:`~Trainee` .
- **API References** How to use, :meth:`Trainee.add_feature`, :py:meth:`Trainee.remove_cases`, and :py:meth:`Trainee.edit_cases` .


Prerequisites
-------------
- You have successfully :doc:`installed Howso Engine <../getting_started/installing>`
- You have :doc:`loaded, configured, trained, and analyzed data <basic_workflow>`


Data
----
Our example dataset for this guide is the well-known ``Adult`` dataset, accessible via the ``pmlb`` package installed
in the prerequisites using the ``fetch_data()`` function.


Notebook Recipe
---------------
There are two recipes which supplement the content this guide will cover:

- :download:`Auditing and Editing </_assets/recipes/4-audit_edit.ipynb>`
- :download:`Bias Mitigation </_assets/recipes/5-bias_mitigation.ipynb>`


Concepts & Terminology
----------------------
The main piece of terminology this guide introduces is the concept of case weights.  To understand this, we
recommend being familiar with the following concepts:

- :ref:`Trainee <user_guide/terminology:trainee>`
- :ref:`React <user_guide/terminology:react>`
- :ref:`Case <user_guide/terminology:case>`
- :ref:`Feature <user_guide/terminology:feature>`
- :ref:`Action Features <user_guide/terminology:action features>`
- :ref:`Context Features <user_guide/terminology:context features>`
- :doc:`Feature Attributes <feature_attributes>`

Additional concepts to be familiar with are `classification <https://en.wikipedia.org/wiki/Statistical_classification>`_ and 
`overfitting <https://en.wikipedia.org/wiki/Overfitting>`_.


Case Weights
^^^^^^^^^^^^
Similar to how feature weights determine how important a particular feature is, case weights determine how important a particular case is:

.. plot::
    :caption: A Demonstration of Case Weighting

    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns

    sns.set_style("whitegrid")
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(8, 3))

    x = np.linspace(-10, 10, num=100)
    uniform_weights = np.array([1/len(x)] * len(x))
    right_biased_weights = np.array([1] * (x <= 5).sum() + [2.5] * (x > 5).sum())
    right_biased_weights = right_biased_weights / right_biased_weights.sum()

    sns.kdeplot(ax=ax1, x=x, weights=uniform_weights, fill=True)
    ax1.set_title("Uniformly-Weighted")
    sns.kdeplot(ax=ax2, x=x, weights=right_biased_weights, fill=True)
    ax2.set_title("x \u2265 5 Weighted 2.5x Normal")
    plt.show()


In the above plot, the right side of the second distribution is weighted to be 2.5 times as important as the left side.  This is 
reflected in the density of the distribution.


How-To-Guide
------------

.. warning::

    Editing and removing cases without exercising the proper due-diligence can lead to overfitting or the introduction of biases
    that may affect downstream use-cases. Exercise caution and consult any necessary experts when editing a :class:`~Trainee`.


Adding Features
^^^^^^^^^^^^^^^
Adding features to a :class:`~Trainee` can be done with a single call to :meth:`Trainee.add_feature`:

.. code-block:: python

    t.add_feature("gender", feature_value="nb", feature_attributes={"type": "nominal"})


In this example, we use it to add a nominal feature to each case in the model with a default value of ``"nb"``.  In addition, 
features can also be added to only certain cases, or without updating the :class:`~Trainee`'s metadata.  For more information on 
the capabilities of :meth:`~Trainee.add_feature`, see the :ref:`API Reference <api-reference>`.


Adding & Using Case Weights
^^^^^^^^^^^^^^^^^^^^^^^^^^^
:meth:`Trainee.add_feature` can also be used to manually add case weights to a :class:`~Trainee`.

.. code-block:: python

    t.add_feature("my_case_weight", feature_value=1.0)


Note that we do not add any feature attributes here, since they are assumed to be continuous by default.  Once added, the case 
weight feature can be used with :meth:`~Trainee.react` and other methods, e.g.:

.. code-block:: python
    
    t.react(contexts, action_features=["target"], use_case_weights=True, weight_feature="my_case_weight")


Which will predict ``"target"`` while using the case weights stored in that feature.  Features which are already in the model may 
similarly be used as case weights. For example, the ``"fnlwgt"`` feature:

.. code-block:: python

    t.react(contexts, action_features=["target"], uase_case_weights=True, weight_feature="fnlwgt")


Editing Cases
^^^^^^^^^^^^^
Like adding features, editing cases is done with calls to :meth:`Trainee.edit_cases`.  Let's say we've consulted an expert and they 
have determined that cases in the adult dataset with a ``workclass`` of ``0`` (an unknown work class) have universally been mis-classified.  
We can edit cases that meet this condition with the following code:

.. code-block:: python

    t.edit_cases([1], condition={"workclass": 0}, features=["target"])


This will set the target for all cases that meet that condition to 1.  Cases may also be edited using their indices or on non-exact matches 
of conditions.  For more information on :meth:`~Trainee.edit_cases`, see the :ref:`API Reference <api-reference>`.

Manually Updating Case Weights
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:meth:`~Trainee.edit_cases` can also be used to manually update case weights. Say we want to address some bias in the data by weighing women 
who have high salaries more highly than those who don't, so that the :class:`~Trainee` is more likely to make balanced predictions.  That can 
be done with the following code:

.. code-block:: python

    t.edit_cases([1.25], condition={"sex": 0, "target": 1}, features=["my_case_weight"])

Of course, this is a surface-level attempt at addressing bias.  For more information on bias mitigation, see the `5-bias_mitigation` recipe.


Removing Cases
^^^^^^^^^^^^^^
Using an API that is very similar to that of :meth:`~Trainee.edit_cases`, :meth:`Trainee.remove_cases` can be used to remove cases from the 
model.  If one or more cases are found to be invalid after they have been trained, they can be removed to ensure the model stays up-to-date 
without needing to train or analyze again.  Let's say that it is discovered that the cases with a ``workclass`` of ``6`` (self-employed, not 
incorporated) were not reported correctly by the dataset creators.  We can remove those cases with the following code:

.. code-block:: python

    num_workclass_6 = len(t.get_cases(condition={"workclass": 6}))
    t.remove_cases(num_workclass_6, condition={"workclass": 6})


Cases can also be removed by index, just how cases can be edited in that fashion as well. For more information on :meth:`~Trainee.remove_cases`,
see the :ref:`API Reference <api-reference>`.


Automatically Updating Case Weights
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When using :meth:`~Trainee.remove_cases`, the weights from removed cases can be automatically distributed to their neighbors upon 
removal using the ``distribute_weight_feature`` parameter. For example,

.. code-block:: python

    num_workclass_6 = len(df[df.workclass == 6])
    t.remove_cases(num_workclass_6, condition={"workclass": 6}, distribute_weight_feature="my_weight_feature")

will remove the cases that satisfy the condition and distribute their weight to their neighbors, allowing cases which are similar 
to increase in importance as these are removed.


Example Use-Cases
^^^^^^^^^^^^^^^^^
In addition to the examples above, here are a few example use-cases for case editing and case weighting:

- Tuning relevance of particular cases in response to user input
    - e.g., weighing liked songs in terms of user preference
- Reducing :class:`~Trainee` size
    - By strategically removing cases while retaining weights, information can be maintained while the size of the :class:`~Trainee`
      is decreased


API References
--------------
- :meth:`Trainee.add_feature`
- :meth:`Trainee.edit_cases`
- :meth:`Trainee.remove_cases`

