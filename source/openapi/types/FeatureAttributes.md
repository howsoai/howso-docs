<!-- Auto-generated do not edit -->

# FeatureAttributes

`````{py:module} howso.openapi.models
:noindex:

````{py:class} FeatureAttributes

The mapping of attributes for a single feature.


```{py:attribute} type
:type: str

The type of the feature.

- continuous: A continuous numeric value. (e.g. Temperature or humidity)
- nominal: A numeric or string value with no ordering. (e.g. The name of a fruit)
- ordinal: A nominal numeric value with ordering. (e.g. Rating scale, 1-5 stars)

```

```{py:attribute} auto_derive_on_train
:type: Optional[FeatureAutoDeriveOnTrain]


```

```{py:attribute} bounds
:type: Optional[FeatureBounds]


```

```{py:attribute} cycle_length
:type: Optional[int]

Cyclic features start at 0 and have a range of [0, cycle_length). The `cycle_length` is the maximum value (exclusive) of the cycle. Values exceeding the cycle length are normalized to the original cycle (e.g., cycles with length 360 for degrees will evaluate a 370 as 10 and 360 as 0). Negative values are not supported in cyclic features. Only applicable to continuous or ordinal features.

Examples:
- degrees: values should be 0-359, cycle_length = 360
- days: values should be 0-6, cycle_length = 7
- hours: values should be 0-23, cycle_length = 24

```

```{py:attribute} data_type
:type: Optional[str]

Specify the data type for features with a type of nominal or continuous. Default is `string` for nominals and
`number` for continuous.

Valid values include:

- `string`, `number`, `json`, `amalgam`, `yaml`: Valid for both nominal and continuous.

- `string_mixable`: Valid only when type is continuous (predicted values may result in interpolated strings
  containing a combination of characters from multiple original values).

- `boolean`: Valid only for nominals.

```

```{py:attribute} date_time_format
:type: Optional[str]

If specified, feature values should match the date format specified by this string. Only applicable to continuous features.

```

```{py:attribute} decimal_places
:type: Optional[int]

Decimal places to round to, default is no rounding. If `significant_digits` is also specified, the number will be rounded to the specified number of significant digits first, then rounded to the number of decimal points as specified by this parameter.

```

```{py:attribute} dependent_features
:type: Optional[List[str]]

A list of other feature names that this feature either depends on or features that depend on this feature. Should be used when there are multi-type value features that tightly depend on values based on other multi-type value features.

```

```{py:attribute} derived_feature_code
:type: Optional[str]

Code defining how the value for this feature could be derived if this feature is specified as a `derived_context_feature` or a `derived_action_feature` during react flows. For `react_series`, the data referenced is the accumulated series data (as a list of rows), and for non-series reacts, the data is the one single row. Each row is comprised of all the combined context and action features. Referencing data in these rows uses 0-based indexing, where the current row index is 0, the previous row's is 1, etc. The specified code may do simple logic and numeric operations on feature values referenced via feature name and row offset.

Examples:
- ``"#x 1"``: Use the value for feature 'x' from the previously processed row (offset of 1, one lag value).
- ``"(- #y 0 #x 1)"``: Feature 'y' value from current (offset 0) row  minus feature 'x' value from previous (offset 1) row.

```

```{py:attribute} dropna
:type: Optional[bool]

DEPRECATED - When true, samples where the feature value is NaN are removed.
```

```{py:attribute} id_feature
:type: Optional[bool]

Set to true for nominal features containing nominal IDs, specifying that his feature should be used to compute case weights for id based privacy. For time series, this feature will be used as the id for each time series generation.

```

```{py:attribute} locale
:type: Optional[str]

The date time format locale. If unspecified, uses platform default locale.

```

```{py:attribute} non_sensitive
:type: Optional[bool]

Flag a categorical nominal feature as non-sensitive. It is recommended that all nominal features be represented with either an `int-id` subtype or another available nominal subtype using the `subtype` attribute. However, if the nominal feature is non-sensitive, setting this parameter to true will bypass the `subtype` requirement. Only applicable to nominal features.

```

```{py:attribute} null_is_dependent
:type: Optional[bool]

Modify how dependent features with nulls are treated during a react, specifically when they use null as a context value. Only applicable to dependent features.
When false (default), the feature will be treated as a non-dependent context feature. When true for nominal types, treats null as an individual dependent class value, only cases that also have nulls as this feature's value will be considered. When true for continuous types, only the cases with the same dependent feature values as the cases that also have nulls as this feature's value will be considered.

```

```{py:attribute} observational_error
:type: Optional[float]

Specify the observational mean absolute error for this feature. Use when the error value is already known. Defaults to 0.
```

```{py:attribute} original_type
:type: Optional[FeatureOriginalType]


```

```{py:attribute} original_format
:type: Optional[Dict[object]]

Original data formats used by clients. Automatically populated by clients to store client language specific context about features.

```

```{py:attribute} post_process
:type: Optional[str]

Custom Amalgam code that is called on resulting values of this feature during react operations.
```

```{py:attribute} significant_digits
:type: Optional[int]

Round to the specified significant digits, default is no rounding.

```

```{py:attribute} subtype
:type: Optional[str]

The type used in novel nominal substitution.
```

```{py:attribute} time_delta_format
:type: Optional[str]

Format of the delta for date time features, default is 'seconds'. Valid values are: milliseconds, seconds, minutes, hours, days, weeks, years.

```

```{py:attribute} time_series
:type: Optional[FeatureTimeSeries]


```

```{py:attribute} unique
:type: Optional[bool]

Flag feature as only having unique values. Only applicable to nominals features.
```

````
`````
