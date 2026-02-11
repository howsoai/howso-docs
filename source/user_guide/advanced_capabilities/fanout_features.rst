.. currentmodule:: howso.engine


Fan-out Features
================
.. topic:: What is covered in this user guide

    In this guide, you will learn what fan-out features are, how to configure them, and when to configure them.


Prerequisites
-------------
- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.


Background
----------
In some datasets, there exist features that have the same values across multiple rows that all derive from a single
observation or example in the real world. For example, in a time-series dataset with stationary features, the stationary
feature values will be replicated for every timestep, but that series and its stationary properties are singular.

Alternatively, a user may have a table of transaction data that was created by joining tables from a relational database.
In such data, features joined from a table with product attributes would have duplicated values for any collection of rows
describing purchases of the same product (where the product ID feature has the same value). However, that product and its
properties are only a singular observation in the original table they derive from.

Consider the following example of a transaction dataset created by joining product and store tables:

.. csv-table:: Example transaction dataset with fan-out features
   :header: "transaction_id", "product_id", "store_id", "quantity", "product_weight", "product_color", "product_price", "store_supply"

   1, "A", "S1", 3, 2.5, "red", 10.99, 50
   2, "B", "S1", 1, 1.0, "blue", 5.99, 30
   3, "A", "S2", 2, 2.5, "red", 12.99, 20
   4, "A", "S1", 5, 2.5, "red", 10.99, 50
   5, "B", "S2", 4, 1.0, "blue", 7.99, 15

In this table, ``product_weight`` and ``product_color`` are fan-out features keyed on ``product_id`` — their values are
always the same for a given product regardless of the store or transaction. Meanwhile, ``product_price`` and ``store_supply``
are fan-out features keyed on the combination of ``product_id`` and ``store_id`` — their values are consistent for a given
product at a given store. The remaining features, ``transaction_id`` and ``quantity``, vary independently per row.


Configuring Fan-out Features
----------------------------
When calling :py:meth:`~howso.utilities.infer_feature_attributes`, features can be configured as fan-out features by
specifying the ``fanout_features_map`` parameter.

The parameter accepts a value of ``dict[str | tuple[str], list[str]]`` where the key is either a single feature name
or a tuple of feature names describing the features whose values select cases with the same values for the associated
fan-out features, which are the list of feature names the key maps to.

.. code-block:: python

    features = infer_feature_attributes(
        data,
        fanout_features_map={
            "product_id": ["product_weight", "product_color", ...],
            # Or if data was joined on multiple features
            ("product_id", "store_id"): ["product_price", "store_supply"]
        }
    )

Configuring fan-out features will allow the Engine to understand the relationships between these features
and have the ability to more fairly measure uncertainty on these fan-out features when the user needs it.


Using Configured Fan-out Features
----------------------------------
Once fan-out features are configured, you as the user need to indicate to the Engine if a particular
operation should filter out the cases with duplicated values while predicitng fan-out feature values.

To do this, many Engine endpoints such as ``react``, ``react_series``, and ``react_aggregate`` support the
``filter_fanout_values`` flag. This flag defaults to ``False``, but when specified as ``True`` the Engine
can take advantage of the configured fan-out feature information to ensure there is no data leakage
when predicting the values for fan-out features.

.. code-block:: python
    :caption: Using the ``filter_fanout_values`` parameter in ``react_aggregate``.

    trainee.react_aggregate(
        details={"prediction_stats": True},
        filter_fanout_values=True,
    )


API References
--------------
- :py:meth:`~howso.utilities.infer_feature_attributes`
- :py:meth:`Trainee.react_aggregate`

