<!-- Auto-generated do not edit -->
# ReactDetails

`````{py:module} howso.openapi.models
:noindex:

````{py:class} ReactDetails

Returns explanation and audit data for a given reaction for the specified audit data flags.
Local and regional models are used to determine explanations:
    Local model -  only the most similar cases used to directly determine the prediction value, used to compute affects of cases directly
                    responsible for the predicted output.
    Regional model - the most similar cases to the prediction, represented by the maximum of either 30 or the local model size. Used in
                    situations where relying on a small local model may produce noisy results.


```{py:attribute} robust_residuals
:type: Optional[bool]

When false, uses leave-one-out for features (or cases, as needed) for all residual computations. When true, uses uniform sampling from the power set of all combinations of features (or cases, as needed) instead. Default behavior is false.

```

```{py:attribute} robust_influences
:type: Optional[bool]

When true, uses leave-one-out for features (or cases, as needed) for all MDA and contribution computations. When true, uses uniform sampling from the power set of all combinations of features (or cases, as needed) instead. Default behavior is true.

```

```{py:attribute} influential_cases
:type: Optional[bool]

When true, outputs the most influential cases and their influence weights based on the surprisal of each case relative to the context being predicted among the cases. Uses only the context features of the reacted case.

```

```{py:attribute} derivation_parameters
:type: Optional[bool]

If True, outputs a dictionary of the parameters used in the react call. These include k, p, distance_transform, feature_weights, feature_deviations, nominal_class_counts, and use_irw.

```

```{py:attribute} influential_cases_familiarity_convictions
:type: Optional[bool]

When true, outputs familiarity conviction of addition for each of the influential cases.
```

```{py:attribute} influential_cases_raw_weights
:type: Optional[bool]

When true, outputs the surprisal for each of the influential cases.

```

```{py:attribute} most_similar_cases
:type: Optional[bool]

When true, outputs an automatically determined (when 'num_most_similar_cases' is not specified) relevant number of similar cases, which will first include the influential cases. Uses only the context features of the reacted case.

```

```{py:attribute} num_most_similar_cases
:type: Optional[float]

When defined, outputs this manually specified number of most similar cases, which will first include the influential cases. Takes precedence over 'most_similar_cases' parameter.

```

```{py:attribute} num_most_similar_case_indices
:type: Optional[float]

When defined, outputs the specified number of most similar case indices when 'distance_ratio' is also set to true.

```

```{py:attribute} num_robust_influence_samples_per_case
:type: Optional[float]

Specifies the number of robust samples to use for each case. Applicable only for computing robust feature contributions or robust case feature contributions. Defaults to 2000 when unspecified. Higher values will take longer but provide more stable results.

```

```{py:attribute} boundary_cases
:type: Optional[bool]

When true, outputs an automatically determined (when 'num_boundary_cases' is not specified) relevant number of boundary cases. Uses both context and action features of the reacted case to determine the counterfactual boundary based on action features, which maximize the dissimilarity of action features while maximizing the similarity of context features. If action features aren't specified, uses familiarity conviction to determine the boundary instead.

```

```{py:attribute} num_boundary_cases
:type: Optional[float]

When defined, outputs this manually specified number of boundary cases. Takes precedence over 'boundary_cases' parameter.

```

```{py:attribute} boundary_cases_familiarity_convictions
:type: Optional[bool]

When true, outputs familiarity conviction of addition for each of the boundary cases.
```

```{py:attribute} features
:type: Optional[List[str]]

A list of feature names that specifies for what features will per-feature details be computed (residuals, contributions, mda, etc.). This should generally preserve compute, but will not when computing details robustly. Details will be computed for all context and action features if this is not specified.

```

```{py:attribute} feature_residuals
:type: Optional[bool]

When true, outputs feature residuals for all (context and action) features locally around the prediction. Uses only the context features of the reacted case to determine that area. Relies on 'robust_residuals' parameter to determine whether to do standard or robust computation.

```

```{py:attribute} feature_mda
:type: Optional[bool]

When true, outputs each context feature's mean decrease in accuracy of predicting the action feature given the context. Uses only the context features of the reacted case to determine that area. Relies on 'robust_influences' parameter to determine whether to do standard or robust computation.

```

```{py:attribute} feature_mda_ex_post
:type: Optional[bool]

When true, outputs each context feature's mean decrease in accuracy of predicting the action feature as an explanation given that the specified prediction was already made as specified by the action value. Uses both context and action features of the reacted case to determine that area. Relies on 'robust_influences' parameter to determine whether to do standard or robust computation.

```

```{py:attribute} feature_contributions
:type: Optional[bool]

When true, outputs each context feature's absolute and directional differences between the predicted action feature value and the predicted action feature value if each context were not in the model for all context features in the local model area. Relies on 'robust_influences' parameter to determine whether to do standard or robust computation. Directional feature contributions are returned under the key 'directional_feature_contributions'.

```

```{py:attribute} case_feature_contributions
:type: Optional[bool]

When true, outputs each context feature's absolute and directional differences between the predicted action feature value and the predicted action feature value if each context feature were not in the model for all context features in this case, using only the values from this specific case. Relies on 'robust_influences' parameter to determine whether to do standard or robust computation. Directional case feature contributions are returned under the 'case_directional_feature_contributions' key.

```

```{py:attribute} case_feature_residuals
:type: Optional[bool]

When true, outputs feature residuals for all (context and action) features for just the specified case. Uses leave-one-out for each feature, while using the others to predict the left out feature with their corresponding values from this case. Relies on 'robust_residuals' parameter to determine whether to do standard or robust computation.

```

```{py:attribute} case_mda
:type: Optional[bool]

When true, outputs each influential case's mean decrease in accuracy of predicting the action feature in the local model area, as if each individual case were included versus not included. Uses only the context features of the reacted case to determine that area. Relies on 'robust_influences' parameter to determine whether to do standard or robust computation.

```

```{py:attribute} case_contributions
:type: Optional[bool]

When true, outputs each influential case's differences between the predicted action feature value and the predicted action feature value if each individual case were not included. Uses only the context features of the reacted case to determine that area. Relies on 'robust_influences' parameter to determine whether to do standard or robust computation.

```

```{py:attribute} global_case_feature_residual_convictions
:type: Optional[bool]

When true, outputs this case's feature residual convictions for the global model. Computed as: global model feature residual divided by case feature residual. Relies on 'robust_residuals' parameter to determine whether to do standard or robust computation.

```

```{py:attribute} local_case_feature_residual_convictions
:type: Optional[bool]

When true, outputs this case's feature residual convictions for the region around the prediction. Uses only the context features of the reacted case to determine that region. Computed as: region feature residual divided by case feature residual. Relies on 'robust_residuals' parameter to determine whether to do standard or robust computation.

```

```{py:attribute} outlying_feature_values
:type: Optional[bool]

When true, outputs the reacted case's context feature values that are outside the min or max of the corresponding feature values of all the cases in the local model area. Uses only the context features of the reacted case to determine that area.

```

```{py:attribute} categorical_action_probabilities
:type: Optional[bool]

When true, outputs probabilities for each class for the action. Applicable only to categorical action features.

```

```{py:attribute} hypothetical_values
:type: Optional[Dict[object]]

A dictionary of feature name to feature value. If specified, shows how a prediction could change in a what-if scenario where the influential cases' context feature values are replaced with the specified values. Iterates over all influential cases, predicting the action features each one using the updated hypothetical values. Outputs the predicted arithmetic over the influential cases for each action feature.

```

```{py:attribute} distance_ratio
:type: Optional[bool]

When true, outputs the ratio of distance (relative surprisal) between this reacted case and its nearest case to the minimum distance (relative surprisal) in between the closest two cases in the local area. All distances are computed using only the specified context features.

```

```{py:attribute} distance_contribution
:type: Optional[bool]

When true, outputs the distance contribution (expected total surprisal contribution) for the reacted case. Uses both context and action feature values.

```

```{py:attribute} similarity_conviction
:type: Optional[bool]

When true, outputs similarity conviction for the reacted case. Uses both context and action feature values as the case values for all computations. This is defined as expected (local) distance contribution divided by reacted case distance contribution.

```

```{py:attribute} observational_errors
:type: Optional[bool]

When true, outputs observational errors for all features as defined in feature attributes.

```

````
`````
