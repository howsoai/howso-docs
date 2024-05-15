Overview of Howso's Trustworthy AI
==================================

Key Features of the Howso Engine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Understandability
-----------------

- Perfect attribution traces decisions directly back to the source data, enabling complete auditability

- Challenge misleading results from current interpretability approaches with breakthroughs in feature importance analysis

  Howso is robust against several common challenges (correlated features, redundant features, difference in scale between features, and multiple distinguishing features)
  faced by other feature importance tools, including the SHAP metric, which often lead to misleading results.

- Fix bias and debug

Easily add, edit, and remove data without spending more costly re-training time and computational resources.

- Identify counterfactuals and perform "what if?" scenario analyses

Performance
-----------

On average, Howso outperforms LightGBM classification and regression accuracy, and demonstrates notable success with small datasets. Additionally, Howso intelligently handles and
imputes sparse and missing data.

Versatility
-----------

- Perform multiple tasks automatically, including...

  - Supervised and unsupervised learning
  - Online learning
  - Reinforcement learning
  - Generative and discriminative analysis
  - Anomaly detection
  - Bias detection and prediction monitoring

- Utilize structured and semi-structured data

- Flexibly handle a variety of data types, including time-series data and nominals

Trustworthiness
---------------

- Calculate reliable uncertainties for your predictions

  Avoid hallucinations with complete and accurate knowledge of uncertainties so you can deliver accountability and know when there is not enough information to make good decisions.

- Remain robust to adversarial attacks that exploit AI in action, and reliably detect them

  Howso outperforms other AI methdos and maintaining the integrity of your data and decisions, even after an attack.

Limitations
-----------

Howso values gracious intellectual honesty. In that spirit, we're telling you up front where we struggle and how we are planning to improve.

- Additional data types

  Currently, we only work with structured data. We are in beta testing for semi-structured data, tiptoeing toward generative language, and images handling is on the distant horizon.

- Feature width

  We work well with hundreds of features, but we are not yet able to handle thousands of features in practical applications.

- Very large datasets

  Handling very large datasets with subtle signals (e.g., datasets requiring tens of millions of records and/or thousands of features to capture the complex relationships within the data)
  currently requires manual work from engineering, data science, and subject matter expert teams. However, currently available Howso tools, including ablation and non-robust feature contribution calculations,
  can be used to help identify subsamples of large datasets that
  contain enough signal to be used for data science analysis.

What's next? How to use these guides...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have not already installed Howso Engine, that's your first step! You can
find our :doc:`installation guide here <installing>`.

Once you're installed, you can try out Howso using a variety of pre-built
:doc:`Jupyter notebook Recipes <../examples/index>`. These notebooks will provide
"recipes" for how to utilize Understandable AI in many applications.

Additionally, you can gain insight into Howso's capabilities by exploring our
:doc:`key concepts <concepts>`, :doc:`terminology <terminology>`, and
:doc:`user guides <../user_guide/index>` or by digging into our python code :doc:`API
references <../api_reference/index>`.

And, as always, we welcome your participation and feedback on our `github page
<https://github.com/howsoai>`_!
