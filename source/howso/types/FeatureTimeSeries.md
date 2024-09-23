<!-- Auto-generated do not edit -->

# FeatureTimeSeries


````{py:class} FeatureTimeSeries

Time series options for a feature.


```{py:attribute} type
:type: str

When `rate` is specified, uses the difference of the current value from its previous value divided by the change in time since the previous value. When `delta` is specified, uses the difference of the current value from its previous value regardless of the elapsed time. Set to `delta` if feature has `time_feature` set to true.

```

```{py:attribute} order
:type: Optional[int]

If provided, will generate the specified number of derivatives and boundary values.

```

```{py:attribute} derived_orders
:type: Optional[int]

The number of orders of derivatives that should be derived instead of synthesized. Ignored if order is not provided.

```

```{py:attribute} delta_min
:type: Optional[List[float]]

If specified, ensures that the smallest difference between features values is not smaller than this specified value. A null value means no min boundary. The length of the list must match the number of derivatives as specified by `order`. Only applicable when time series type is set to `delta`.

```

```{py:attribute} delta_max
:type: Optional[List[float]]

If specified, ensures that the largest difference between feature values is not larger than this specified value. A null value means no max boundary. The length of the list must match the number of derivatives as specified by `order`. Only applicable when time series type is set to `delta`.

```

```{py:attribute} lags
:type: Optional[List[int]]

If specified, generates lag features containing previous values using the enumerated lag offsets. Takes precedence over `num_lags`. If neither `num_lags` nor `lags` is specified for a feature, then a single lag feature is generated.

```

```{py:attribute} num_lags
:type: Optional[int]

If specified, generates the specified amount of lag features containing previous values. If `lags` is specified, then this parameter will be ignored. If neither `num_lags` nor `lags` is specified for a feature, then a single lag feature is generated.

```

```{py:attribute} rate_min
:type: Optional[List[float]]

If specified, ensures that the rate (the difference quotient, the discrete version of derivative) for this feature won't be less than the value provided. A null value means no min boundary. The value must be in epoch format for the time feature. The length of the list must match the number of derivatives as specified by `order`. Only applicable when time series type is set to `rate`.

```

```{py:attribute} rate_max
:type: Optional[List[float]]

If specified, ensures that the rate (the difference quotient, the discrete version of derivative) for this feature won't be more than the value provided. A null value means no max boundary. The value must be in epoch format for the time feature. The length of the list must match the number of derivatives as specified by `order`. Only applicable when time series type is set to `rate`.

```

```{py:attribute} series_has_terminators
:type: Optional[bool]

When true, requires that the model identify and learn values that explicitly denote the end of a series. Only applicable to id features for a series.

```

```{py:attribute} stop_on_terminator
:type: Optional[bool]

When true, requires that a series ends on a terminator value. Only applicable to id features for a series.

```

```{py:attribute} time_feature
:type: Optional[bool]

When true, the feature will be treated as the time feature for time series modeling. Additionally, time features must use type `delta`.

```

````
