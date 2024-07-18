================
Derived Features
================

.. topic:: In this user guide...
    
    You will learn how to specify derived features to maintain feature relationships
    during Engine operations.


Objectives & Takeaways
----------------------

- **Definitions & an understanding** of how to use derived features as well as
  which situations or data derived features are appropriate for.


Prerequisite
------------

- You've successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/standard_workflow>`

Data
----
The dataset for this recipe highlights one of the common use-cases for derived features
and can be downloaded :download:`here </_assets/dates_generated.parquet>`. This dataset
consists of a start time, and end time, and a duration column. We will use derived features
to ensure that the end time is equal to the start time plus the duration.


Concepts & Terminology
----------------------

- :ref:`case`
- :ref:`derived_features`


How-To guide
------------

Here we will define a derived feature and then react to the dataset. This will ensure
that the features maintain their relationhips.


Load Data
^^^^^^^^^

First, we load the data using `Pandas`. Note that the data are stored as a `Parquet` file
in order to preserve the datetime data types.

.. code-block:: python

    # These are the necessary imports for this user guide:
    import datetime
    import pandas as pd
    
    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

    # Load in the data using pandas
    df = pd.read_parquet('data/dates_generated.parquet')

    df


Define Derived Feature Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Derived features use code that is similar to https://github.com/howsoai/amalgam to define a
relationship. Then, rather than predicting, the feature will be derived according to that code.

To do this, we create a partial `feature attributes` dictionary which will be fed to
:func:`~howso.utilities.infer_feature_attributes`. In the partial `feature attributes`
dictionary, we define the derived feature code which instructs Engine in how to derive
the ``end`` feature as a function of the ``start`` abd ``duration`` features.

.. code-block:: python

    partial_features = {
        'end': {
            'derived_feature_code': '(+ #start 0 #duration 0),
        }


The derived feature code that we use, ``(+ #start 0 #duration 0)`` instructs Engine to add
``duration`` to ``start``. The zeros are offsets that are only non-zero for time-series operations,
and refer to how far back in the time-series to look.


Map Data
^^^^^^^^
Now we can use :meth:`~howso.utilities.infer_feature_attributes` to understand the properties
and characteristics of the data.

.. code-block:: python

    features = infer_feature_attributes(df, features=partial_features)


By supplying the partial feature attributes we defined in step 2, the derived feature code will
be populated for the ``end`` feature.


Train and Analyze
^^^^^^^^^^^^^^^^^
Here the original data are trained into Howso Engine, so that it understands relationships between all
data points.

.. code-block:: python
    
    trainee = Trainee(features=features)
    trainee.train(df)
    trainee.analyze()


React
^^^^^
Here we perform a generative react to generate 5 cases.

.. code-block:: python

    reaction = t.react(
        action_features=['start', 'end', 'duration'],
        derived_action_features=['end'],
        desired_conviction=5,
        generate_new_cases='no',
        num_cases_to_generate=5,
    )
    synth_df = reaction['action']
    synth_df['end'] = synth_df.end.apply(
        lambda x: datetime.datetime.fromtimestamp(x)
    )


The ``derived_action_features`` parameter instructs Engine to derive the ``end`` feature rather than generating it.

Finally, we can validate that the derivation behaved as expected:

.. code-block:: python

    for i, row in synth_df.iterrows():
        assert row.start + pd.to_timedelta(row.duration, unit='s') == row.end


Complete Code
^^^^^^^^^^^^^
The code from all of the steps in this guide is combined below:

.. code-block:: python

    # These are the necessary imports for this user guide:
    import datetime
    import pandas as pd
    
    from howso.engine import Trainee
    from howso.utilities import infer_feature_attributes

    # Load in the data using pandas
    df = pd.read_parquet('data/dates_generated.parquet')

    df

    trainee = Trainee(features=features)
    trainee.train(df)
    trainee.analyze()

    reaction = t.react(
        action_features=['start', 'end', 'duration'],
        derived_action_features=['end'],
        desired_conviction=5,
        generate_new_cases='no',
        num_cases_to_generate=5,
    )
    synth_df = reaction['action']
    synth_df['end'] = synth_df.end.apply(
        lambda x: datetime.datetime.fromtimestamp(x)
    )

    for i, row in synth_df.iterrows():
        assert row.start + pd.to_timedelta(row.duration, unit='s') == row.end


API References
--------------

- :func:`howso.utilities.infer_feature_attributes`
- :class:`howso.engine.Trainee`
    - :meth:`howso.engine.Trainee.train`
    - :meth:`howso.engine.Trainee.react`