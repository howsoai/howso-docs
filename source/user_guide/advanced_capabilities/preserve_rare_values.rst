.. currentmodule:: howso.engine


Rare Value Preservation
=======================
.. topic:: What is covered in this user guide

    In this guide, you will learn how to configure the "preserve_rare_values" feature attribute and how to use it to protect
    rare signals in your data.


Prerequisites
-------------
- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding of Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.


Background
----------
In some use-cases, the segment of the data that is most integral to the problem may represent a vanishingly small
proportion of the overall data. For example, one may be investigating the failure cases of a particularly stable
system where failure occurs less than 0.1% of the time, but that 0.1% still represents a significant number of trained
cases.

In such cases, it may be beneficial to artificially manipulate the probability masses of these rare values in order
to boost their signal or make them more significant in the case that the Trainee will undergo data reduction via
:py:meth:`Trainee.reduce_data`, where formerly significant data masses may lose some significance in the reduction process.

Additionally, this functionality offers avenues to the user for bias mitigation techniques where minority classes
are boosted in mass to be equally or more fairly represented in the context of the dataset.


Configuring `preserve_rare_values`
----------------------------------
To offer solutions to these types of problems, :py:meth:`~howso.utilities.infer_feature_attributes` offers a few
different parameters allowing users to specify the rare values they want preserved and possibly the exact values with
which to boost their signal based on their use-case.

In the case that you want to protect values of a specific feature but you do not know to what extent, then you should
use the `preserve_rare_values_map` parameter which takes a map of feature name to list of values to be protected. In
these cases, the Engine automatically decides how to scale up weights of the relevant cases.
For example:

.. code-block:: python

    features = infer_feature_attributes(
        data,
        preserve_rare_values_map={
            # Protects the "FAIL" value of the "result" feature.
            "result": ["FAIL"],
        }
    )

Alternatively, if you know the exact scale to which you want to scale up the probability mass of a value, then you
should use the `preserve_rare_values_config` parameter. This parameter allows users to specify the collection of
values that need protection as well as the exact multipliers to use when scaling up the weight of the associated cases.

.. code-block:: python

    features = infer_feature_attributes(
        data,
        preserve_rare_values_config={
            # The feature whose values should be protected
            "result": [
                {
                    # The feature value to increase probability mass of
                    "value": "FAIL",
                    # The scalar value to multiply probability mass by
                    "multiplier": 4.0
                },
                # Other protected values...
            ]
        }
    )


Using `preserve_rare_values`
----------------------------
Once rare value preservation is configured through :py:meth:`~howso.utilities.infer_feature_attributes`, the
manipulation of the associated case weights occurs as data is trained into the Trainee and will automatically
influence all downstream tasks using that Trainee.


API References
--------------
- :py:meth:`~howso.utilities.infer_feature_attributes`
- :py:meth:`Trainee.reduce_data`

