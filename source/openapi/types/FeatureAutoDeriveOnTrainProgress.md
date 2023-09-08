<!-- Auto-generated do not edit -->
# FeatureAutoDeriveOnTrainProgress

`````{py:module} howso.openapi.models
:noindex:

````{py:class} FeatureAutoDeriveOnTrainProgress

Derive feature by creating two new continuous features: `.series_progress` and `.series_progress_delta`. Series progress values range from 0 to 1.0 for each case in the series. Series progress delta values are the delta value of the progress for each case. Both of these features are used to determine when to stop series synthesis.


```{py:attribute} derive_type
:type: str

The train derive operation type.
```

```{py:attribute} series_id_features
:type: List[str]

Feature name(s) of series for which to derive this feature. A series is the conjunction of all the features specified by this attribute.

```

````
`````
