.. currentmodule:: howso.engine

Reacting to Existing vs New Cases
=================================
.. topic:: What is covered in this user guide.

   In this guide, you will learn the basics about the different types of cases you can :py:meth:`Trainee.react` to in your :py:class:`~Trainee`.

Objectives: what you will take away
-----------------------------------
- **Definitions & an understanding** how to react on existing vs. new cases.

Prerequisites: before you begin
-------------------------------
- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.

Data
----
Our example dataset for this guide is the well-known ``Adult`` dataset, accessible via the ``pmlb`` package installed
in the prerequisites using the ``fetch_data()`` function.

Concepts & Terminology
----------------------

- :ref:`trainee`
- :ref:`react`
- :ref:`case`
- :ref:`feature`
- :ref:`action_features`
- :ref:`context_features`

How-To Guide
------------

Setup
^^^^^
The user guide assumes you have created and setup a :class:`~Trainee` as demonstrated in :doc:`basic workflow <../basic_capabilities/basic_workflow>`.
The :class:`~Trainee` will be referenced as ``trainee`` in the sections below.

New Cases
^^^^^^^^^
Using :py:meth:`Trainee.react` with new cases is straightfoward and simple. This is often the default use case of most workflows.
When cases are passed into react, :py:meth:`Trainee.react`, it acts upon the cases as if they were new cases.

.. code-block:: python

    results = trainee.react(
        test_case[context_features],
        context_features=context_features,
        action_features=action_features,
    )

Existing Cases
^^^^^^^^^^^^^^

In certain workflows, you might want to examine cases already trained into the trainee. To do this, a list of cases must
be passed into the ``case_indices`` parameter in :py:meth:`Trainee.react`. This list passed into ``case_indices`` must consist of iterables of cases
where the first value is the ``session_id`` and the second value is the ``session_training_index``.

To get the ``session_id``, :py:meth:`Trainee.get_sessions` retrieves the available sessions.
Once you have the ``session_id``, using :py:meth:`Trainee.get_cases` with the ``session_id`` allows you to see the ``session_training_index``,
where are the indexes of the returning dataframe.

.. code-block:: python

    # Get data from the first session
    session = trainee.get_sessions()[0]['id']

    # See the case indices
    trainee.get_cases(session='db3ebfc0-0bb3-4b33-b475-7ca7d21267e2')

    # React to the first case in this session
    case = [(session, 1)]

Once you have the case(s) in the right format, then they must be passed into the ``case_indices`` parameter.
Generally, ``leave_case_out`` is set to ``True`` to indicate that this case must be excluded when reacting. This is typically
desired behavior because we don't want the react to be skewed by an identical case.

``preserve_feature_values`` is also generally set to the context features to preserve their values.

.. code-block:: python

    new_result = trainee.react(
        case_indices=case,
        preserve_feature_values=context_features,
        leave_case_out=True
        action_features=action_features
    )

API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :py:meth:`Trainee.react`
