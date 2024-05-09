.. currentmodule:: howso.engine

Influential Cases
=================
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics of using Howso Engine to query influential, similiar, and boundary cases.


Prerequisites: before you begin
-------------------------------
- **Installation** - You have successfully installed :doc:`Howso Engine <../../getting_started/installing>`.
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.

Data
----

Our example dataset for this guide is the well-known ``Adult`` dataset, accessible via the ``pmlb`` package installed
in the prerequisites using the ``fetch_data()`` function.

Concepts & Terminology
----------------------
Influential cases and most similiar cases represent the cases with the smallest distance to the case of interest. They are closely related,
as most similar cases can be any of number of cases ranked by distance while influential cases are a subset of most similiar cases comprising 
of cases close enough to influence the case of interest. Boundary cases are the most similiar cases that have a different action value.

- :ref:`influential_cases`
- :ref:`most_similar_cases`
- :ref:`boundary_cases`

How-To Guide
------------

Setup
^^^^^
The user guide assumes you have created and setup a :class:`~Trainee` as demonstrated in :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
The created :class:`~Trainee` will be referenced as ``trainee`` in the sections below.


Configure the details parameter and react
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ``details`` parameter allows us to select which details to return when using :meth:`~Trainee.react`.

Influential Cases
^^^^^^^^^^^^^^^^^
Influential cases can be retrieved by setting ``influential_cases`` to ``True``.  

.. code-block:: python

    details = {'influential_cases': True}

 
Most Similiar Cases
^^^^^^^^^^^^^^^^^^^

The most similiar cases can be retrieved by setting ``most_similar_cases`` to ``True``. The number
of cases retrieved can be set by configuring the ``num_most_similar_cases`` parameter.

.. code-block:: python

    details = {
        'most_similar_cases': True,
        'num_most_similar_cases': 30,
    }

Boundary Cases
^^^^^^^^^^^^^^

Boundary cases can be retrieved by setting ``boundary_cases`` to ``True``. The number
of cases retrieved can be set by configuring the ``num_boundary_cases`` parameter.

.. code-block:: python

    details = {
        'boundary_cases': True,
        'num_boundary_cases': 30,
    }
            
React
^^^^^

Calling :meth:`~Trainee.react` on the test case will retrieve the details for that case. The
details in the sections above may be retrieved all at once as shown below.

   
.. code-block:: python

    details = {
        'most_similar_cases': True,
        'num_most_similar_cases': 30,
        'boundary_cases': True,
        'num_boundary_cases': 30,
        'influential_cases': True,
    } 

    results = t.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=details
    )


Step 6 - Retrieve Details
^^^^^^^^^^^^^^^^^^^^^^^^^
Review the results of the details retrieved.

.. code-block:: python

    influential_cases = pd.DataFrame(results['details']['influential_cases'][0])
    similiar_cases = pd.DataFrame(results['details']['similiar_cases'][0])
    boundary_cases = pd.DataFrame(results['details']['boundary_cases'][0])

Combined Code
^^^^^^^^^^^^^

.. code-block:: python

    import pandas as pd
    from pmlb import fetch_data

    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

    df = fetch_data('adult', local_cache_dir="data/adult")

    # Subsample the data to ensure the example runs quickly
    df = df.sample(1000, random_state=0).reset_index(drop=True)

    # Split out the last row for a prediction set and drop the Action Feature
    test_case = df.iloc[[-1]].copy()
    df.drop(df.index[-1], inplace=True)

    # Auto detect features
    features = infer_feature_attributes(df)

    # Specify Context and Action Features
    action_features = ['target']
    context_features = features.get_names(without=action_features)

    # Create a new Trainee, specify features
    trainee = Trainee(features=features)

    # Train and analyze
    trainee.train(df)
    trainee.analyze()

    details = {
        'most_similar_cases': True,
        'num_most_similar_cases': 30,
        'boundary_cases': True,
        'num_boundary_cases': 30,
        'influential_cases': True,
    } 

    results = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
        details=details
    )

    influential_cases = pd.DataFrame(results['details']['influential_cases'][0])
    similiar_cases = pd.DataFrame(results['details']['most_similar_cases'][0])
    boundary_cases = pd.DataFrame(results['details']['boundary_cases'][0])


API References
^^^^^^^^^^^^^^
- :class:`~Trainee`
- :meth:`Trainee.train`
- :meth:`Trainee.analyze`
- :meth:`Trainee.react`
- :meth:`Trainee.react_into_trainee`
- :meth:`Trainee.get_prediction_stats`
- :meth:`Trainee.predict`