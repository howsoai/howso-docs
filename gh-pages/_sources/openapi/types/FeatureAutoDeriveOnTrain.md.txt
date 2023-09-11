<!-- Auto-generated do not edit -->
# FeatureAutoDeriveOnTrain

`````{py:module} howso.openapi.models
:noindex:

````{py:class} FeatureAutoDeriveOnTrain

Define how to create and derive all the values for this feature from the trained dataset.


```{py:attribute} derive_type
:type: str

The train derive operation type.
```

```{py:attribute} code
:type: str

Amalgam code describing how feature could be derived.
```

```{py:attribute} series_id_features
:type: List[str]

Feature name(s) of series for which to derive this feature. A series is the conjunction of all the features specified by this attribute.

```

```{py:attribute} ordered_by_features
:type: Optional[List[str]]

Feature name(s) by which to order the series specified by `series_id_features`. Series values are order by the order of feature names specified by this attribute.

```

````
`````
