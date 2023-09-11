<!-- Auto-generated do not edit -->
# FeatureAutoDeriveOnTrainCustom

`````{py:module} howso.openapi.models
:noindex:

````{py:class} FeatureAutoDeriveOnTrainCustom

Derive feature using the specified `code`. For each series, where each series is defined by `series_id_features`, the rows are processed in order, after being sorted by `ordered_by_features`. If series is not specified, processes the entire dataset. Referencing data in rows uses 0-based indexing, where the current row index is 0, the previous row's is 1, etc. Specified code may do simple logic and numeric operations on feature values referenced via feature name and row offset.

Examples:
- ``"#x 1"`` : Use the value for feature 'x' from the previously processed row (offset of 1, one lag value).
- ``"(- #y 0 #x 1)"`` : Feature 'y' value from current (offset 0) row  minus feature 'x' value from previous (offset 1) row.


```{py:attribute} derive_type
:type: str

The train derive operation type.
```

```{py:attribute} code
:type: str

Amalgam code describing how feature could be derived.
```

```{py:attribute} series_id_features
:type: Optional[List[str]]

Feature name(s) of series for which to derive this feature. A series is the conjunction of all the features specified by this attribute.

```

```{py:attribute} ordered_by_features
:type: Optional[List[str]]

Feature name(s) by which to order the series specified by `series_id_features`. Series values are order by the order of feature names specified by this attribute.

```

````
`````
