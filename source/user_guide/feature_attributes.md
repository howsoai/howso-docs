# Feature Attributes
Understanding and properly utilizing **Feature Attributes** is the most important step for successful use of Diveplane. Feature attributes can be specified manually but are often built using the infer feature attributes (IFA) utility function. This section will answer common questions related to both IFA and the feature attributes in general.

Related api reference pages for feature attributes:
  - [FeatureAttributes type](howso.openapi.models.FeatureAttributes)
  - [infer_feature_attributes() utility function](howso.utilities.infer_feature_attributes)

## How do I use Infer Feature Attributes?
- In general, IFA is an iterative process:
  1. If you're new to IFA or are not familiar with your data types, just pass-in your data and `print` the dictionary:
     `features = infer_feature_attributes(data)`.
  2. Audit the dictionary to ensure the mapping matches your data. Some common mappings that should be reviewed:
     1. `type` being `nominal`, `ordinal`, or `continuous`.
     2. `bounds`: `min` and `max` values.
     3. `date_time_format` for specifying the dates/times correctly.
  3. Pass in any changes as arguments to IFA and run it again. The following are some of the common arguments:
     1. Create a **partial feature dictionary** and pass it to the argument `features`. This is common when specifying the `type`, for example when a feature is `nominal`.
     2. Pass in a dictionary that specifies the correct datetime format using `datetime_feature_formats`.
     3. The exception is specifying the `bounds`. Edit the dictionary after it's been built by IFA.
  4. `print` the dictionary and audit.
  5. Repeat steps 2 - 3 until the **feature mapping** is built properly.

## What is the difference between **nominal**, **ordinal**, and **continuous** features?
- `continuous`: A numeric value that can be any value between two arbitrary numbers. e.g. price, date, distance
- `nominal`: An unordered value. e.g. name, phone number, shirt size
- `ordinal`: An ordered value. e.g. priority number, product rating, education degree

## How do I map **ordinal** features?
- If the feature is `numeric`, all you must do is specify the `type` as `ordinal` inside IFA.
- If the feature is `ordinal` but not `numeric`, pass a dictionary specifying the order to IFA using the `ordinal_feature_values` argument.
  - An example is: `{ "size" : [ "small", "medium", "large", "huge" ] }`

## How do I map **cyclic** features?
Cyclic features start at 0 and end at the value specified exclusively. e.g. To specify days of the week provide a `cycle_length` of 7 and values in your data should be 0 to 6.
- Specify the `type` as `continuous` inside IFA.
- Specify the maximum value (exclusive) as the `cycle_length` feature attribute.

## How do I specify dates?
- Often, IFA can intuit the proper date format especially if the dates are a Python `datetime` object.
- They can also be specified by passing a dictionary to IFA using the `datetime_feature_formats` argument.
  - An example is: `{ "end_date" : "%Y-%m-%d" }`

## What are **partial features**?
- **Partial features** is a term used to describe a partial dictionary from which IFA builds the rest of the feature mapping. It is also a variable-name passed to the `features` argument inside IFA. Below is an example:
```Python
# Infer features using DataFrame format
partial_features = {'education-num':{'type':'nominal'}, 'age':{'type':'continuous'}}
features = infer_feature_attributes(df, features=partial_features)
```
- `partial_features` are important because they allow IFA to correctly specify the bounds. For example, imagine a `nominal` feature of US zip codes (90016, 91334, etc.). IFA may infer these values to be `continuous` and the resulting dictionary will include `min` and `max` bounds. You can edit the `type` to be `nominal` post calling IFA, but the `continuous` bounds may cause an issue when reacting to the model. This is why it's often better to use `partial_features` as a core to pass into IFA.

## What are **dependent features**?
- Dependent features are those features which depend on each other. These features are specified using the `dependent_features` feature attribute. Common examples include lab results and their units of measure. During synthesis, it's imperative the lab results match the units of measure like the original dataset.

## Derivation Attributes

Derived during-training features should have a feature attribute of [auto_derive_on_train](howso.openapi.models.FeatureAutoDeriveOnTrain),
containing the configuration on how to derive the feature.

A `derive_type` value is required to define the type of derivation, one of [custom](howso.openapi.models.FeatureAutoDeriveOnTrainCustom) or
[progress](howso.openapi.models.FeatureAutoDeriveOnTrainProgress) is allowed. Each type has its own attribute set.

Allowed list of operations for `code` attributes. All operations use prefix notation:

    + - * / = != < <= > >= number string concat if and or xor not null min max
    mod sqrt pow abs log exp floor ceil round rand sin cos acos tan atan sinh
    asinh cosh acosh tanh atanh