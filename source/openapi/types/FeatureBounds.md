<!-- Auto-generated do not edit -->
# FeatureBounds

`````{py:module} howso.openapi.models
:noindex:

````{py:class} FeatureBounds

Bounds for feature value generation.

```{py:attribute} min
:type: Optional[object]

The minimum value to be output. May be a number or date string.
```

```{py:attribute} max
:type: Optional[object]

The maximum value to be output. May be a number or date string.
```

```{py:attribute} allowed
:type: Optional[List[object]]

Explicitly allowed values to be output.
```

```{py:attribute} allow_null
:type: Optional[bool]

Allow nulls to be output, per their distribution in the data. Defaults to true.
```

```{py:attribute} constraint
:type: Optional[str]

Amalgam code, whose logic has to evaluate to true for value to be considered valid when this feature is being generated. Same format as 'derived_feature_code'.

Examples:
- ``"(> #f1 0 #f2 0)"``: Feature 'f1' value from current (offset 0) data must be bigger than feature 'f2' value from current (offset 0) data.

```

````
`````
