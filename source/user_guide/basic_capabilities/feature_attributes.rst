.. _feature_attributes:
.. currentmodule:: howso.engine


Feature Attributes
==================

Understanding and properly utilizing **Feature Attributes** is the most
important step for successful use of Howso. Feature attributes can be
specified manually but are often built using the :py:meth:`~howso.utilities.infer_feature_attributes` (IFA)
utility function. This section will answer common questions related to both IFA
and the feature attributes in general.

Related api reference pages for feature attributes:
  - :py:class:`~howso.openapi.models.FeatureAttributes` type.
  - :py:meth:`~howso.utilities.infer_feature_attributes` utility function.

How do I use Infer Feature Attributes?
--------------------------------------
- In general, IFA is an iterative process:

  1. If you're new to IFA or are not familiar with your data types, just
     pass-in your data and ``print`` the dictionary. A subset of your data
     may also be provided if not all features' attributes are intended to be inferred,
     however this is not recommended, as all features that are used with Howso are recommended
     to have a corresponding set of feature attributes mappings.

     .. code-block:: python

       features = infer_feature_attributes(data)

  2. Audit the dictionary to ensure the mapping matches your data. Some common
     mappings that should be reviewed:

     a. ``type`` being `nominal`, `ordinal`, or `continuous`.
     b. ``bounds``: ``min`` and ``max`` values.
     c. ``date_time_format`` for specifying the dates/times correctly.

  3. Pass in any changes as arguments to IFA and run it again. The following
     are some of the common arguments:

     a. Create a **partial feature dictionary** and pass it to the argument
        ``features``. This is common when specifying the ``type``, for example when
        a feature is `nominal`.
     b. Pass in a dictionary that specifies the correct datetime format using
        ``datetime_feature_formats``.
     c. The exception is specifying the ``bounds``. Edit the dictionary after
        it's been built by IFA.

  4. ``print`` the dictionary and audit.
  5. Repeat steps 2 - 3 until the **feature mapping** is built properly.

What is the difference between **nominal**, **ordinal**, and **continuous** features?
-------------------------------------------------------------------------------------
- `continuous`: A numeric value that can be any value between two arbitrary numbers. e.g. price, date, distance
- `nominal`: An unordered value. e.g. name, phone number, shirt size
- `ordinal`: An ordered value. e.g. priority number, product rating, education degree

How do I map **ordinal** features?
----------------------------------
- If the feature is `numeric`, all you must do is specify the ``type`` as
  `ordinal` inside IFA.
- If the feature is `ordinal` but not `numeric`, pass a dictionary specifying
  the order to IFA using the ``ordinal_feature_values`` argument. - An example
  is: ``{ "size" : [ "small", "medium", "large", "huge" ] }``

How do I map **cyclic** features?
---------------------------------
Cyclic features are set by specifying a ``cycle_length`` value in the feature attributes.
``cycle_length`` requires a single value, which is the upper bound of the difference for
the cycle range. For example, if ``cycle_length`` is 360,  then a value of 1 and 359 will
have a difference of 2. Cyclic features have no restrictions in the input dataset, however,
cyclic features will be output on a scale from 0 to ``cycle_length``. To constrain the output
to a different range, modify the ``min`` and ``max`` ``bounds`` feature attribute.

- Specify the ``type`` as `continuous` inside IFA.
- Specify the maximum value (exclusive) as the ``cycle_length`` feature attribute.

How do I specify dates?
-----------------------
- Often, IFA can intuit the proper date format especially if the dates are a
  Python ``datetime`` object.
- They can also be specified by passing a dictionary to IFA using the
  ``datetime_feature_formats`` argument.
  - An example is: ``{ "end_date" : "%Y-%m-%d" }``

What are **partial features**?
------------------------------
- **Partial features** is a term used to describe a partial dictionary from
  which IFA builds the rest of the feature mapping. It is also a variable-name
  passed to the ``features`` argument inside IFA. Below is an example:

  .. code-block:: python

    # Infer features using DataFrame format
    partial_features = {'education-num':{'type':'nominal'}, 'age':{'type':'continuous'}}
    features = infer_feature_attributes(df, features=partial_features)

- ``partial_features`` are important because they allow IFA to correctly specify
  the bounds. For example, imagine a `nominal` feature of US zip codes (90016,
  91334, etc.). IFA may infer these values to be `continuous` and the resulting
  dictionary will include ``min`` and ``max`` bounds. You can edit the ``type`` to be
  `nominal` post calling IFA, but the `continuous` bounds may cause an issue
  when reacting to the model. This is why it's often better to use
  ``partial_features`` as a core to pass into IFA.

What are **dependent features**?
--------------------------------
- Dependent features are those features which depend on each other. These
  features are specified using the ``dependent_features`` feature attribute.
  Common examples include lab results and their units of measure. During
  predictions, it's imperative the lab results match the units of measure like
  the original dataset.

.. code:: python

    # Specify the dependencies between the feature description, units, and value.
    dependent_features={
        "measurement": [ "measurement_amount" ]
    }

    # Pass in the dependent_features to infer_feature_attributes.
    features = infer_feature_attributes(
        df,
        dependent_features=dependent_features,
        features=features
    )

Derivation Attributes
---------------------
Derived during-training features should have a feature attribute of
[auto_derive_on_train](howso.openapi.models.FeatureAutoDeriveOnTrain),
containing the configuration on how to derive the feature.

A ``derive_type`` value is required to define the type of derivation, one of
[custom](howso.openapi.models.FeatureAutoDeriveOnTrainCustom) or
[progress](howso.openapi.models.FeatureAutoDeriveOnTrainProgress) is allowed.
Each type has its own attribute set.

Allowed list of operations for ``code`` attributes. All operations use prefix notation:

    \+ - * / = != < <= > >= number string concat if and or xor not null min max
    mod sqrt pow abs log exp floor ceil round rand sin cos acos tan atan sinh
    asinh cosh acosh tanh atanh


Advanced Configurations
-----------------------

Feature Bounds
^^^^^^^^^^^^^^
Feature values are generally given fuzzy bounds derived from the actual values. This allows for some variation in the data.
If strict bounds are more appropriate for the feature, there are 3 ways to set this.

The first is by passing through a list in the ``tight_bounds`` parameter of :py:func:`~howso.utilities.infer_feature_attributes`. The features
specified in this list will use the exact bounds present in the original data.

.. code:: python

    features = infer_feature_attributes(df, tight_bounds=["feature_a", "feature_b"])

The second method is to directly modify the features map created by :py:func:`~howso.utilities.infer_feature_attributes`.
For numeric values, ``min`` and ``max`` can be set in ``bounds`` to set the minimum and maximum values.

.. code:: python

    features["Year"]["bounds"]["min"] = fuel_df["Year"].min()
    features["Year"]["bounds"]["max"] = fuel_df["Year"].max()

Lastly, these bounds can also be set directly through the ``feature_bounds_map`` parameter as shown below.

.. code:: python

    gen_df = s.synthesize_cases(
        n_samples=n_samples,
        desired_conviction=desired_conviction,
        feature_bounds_map={"Year": {"min": 1970, "max": 2020}},
        generate_new_cases="always",
    )

.. _null_values_IFA:

Nulls and Missing Values
^^^^^^^^^^^^^^^^^^^^^^^^
The feature attributes map produced by :py:func:`~howso.utilities.infer_feature_attributes` sets the ``allow_null`` parameter depending on whether the
original data contains nulls. This controls whether predictions can also contains nulls. In order to override the inferred value,
the ``allow_null`` parameter in the feature attributes map can be manually configured as shown below. Additionally, in the case of predictions,
:py:meth:`Trainee.react` also supports an `allow_null` parameter.

.. code:: python

    features["Year"]["bounds"]["allow_null"] = False