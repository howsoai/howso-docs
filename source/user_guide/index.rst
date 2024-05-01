===========
User Guides
===========

User guides are designed to help you get started working with Howso Engine. These guides teach the basics of setting up the Engine for
a variety of data science tasks, explore Howso's understandability toolkit, and demonstrate advanced capabilities useful for particular applications
of Howso Engine. Additionaly, they teach you terminology that is unique to Howso, provide insight into how Howso approaches data science
problems, and identify key API references. They also contain examples for using each Howso tool within a data science workflow. To help you decide which user guide
is best for you, we have grouped them into three categories:

Basic Capabilities
^^^^^^^^^^^^^^^^^^

Here, you will gain insight into how Howso Engine provides full trust and control of your data and decisions.
These guides will acquaint you with the basic workflow for building a :py:class:`~howso.engine.trainee.Trainee`
and making your first AI predictions. Additionally, we review the important step of setting up your - :py:meth:`~howso.utilities.infer_feature_attributes`, which helps the Engine
understand the relationships between your data. 

- :doc:`Basic Workflow <basic_capabilities/basic_workflow>`
- :doc:`Feature Attributes <basic_capabilities/feature_attributes>`
- :doc:`Derived Features <basic_capabilities/derived_features>`
- :doc:`Predictions <basic_capabilities/predictions>`
- :doc:`Saving, loading, and deleting <basic_capabilities/save_load_delete>`

Advanced Capabilities
^^^^^^^^^^^^^^^^^^^^^

With these guides, you will learn how to use Howso's unique tools for understandability and trust. You will gain skills for understanding Engine's predictions, including how
to identify the data that directly influenced your decisions, counterfactuals, and Engine's uncertainty.

- :doc:`Bias Mitigation <advanced_capabilities/bias_mitigation>`
- :doc:`Case Importance <advanced_capabilities/case_importance>`
- :doc:`Feature Imprtance <advanced_capabilities/feature_importance>`
- :doc:`Generative AI/Synth <advanced_capabilities/generative_AI_synth>`
- :doc:`Influential Cases <advanced_capabilities/influential_cases>`
- :doc:`JSON/YAML as features <advanced_capabilities/json_features>`
- :doc:`Time Series <advanced_capabilities/time_series>`
- :doc:`Editing Trainees and Case Weighting <advanced_capabilities/editing_case_weighting>`
- :doc:`Reinforcement Learning <advanced_capabilities/reinforcement_learning>`

Concepts
^^^^^^^^

There may be concepts that are new when exploring Howso's engine. This section goes over concepts that are unique to Howso and differ from other machine learning workflows as well as any other interesting pieces of information that may help you in your journey of using Howso.

- :doc:`Reacting to existing vs new cases <concepts/existing_vs_new>`
- :doc:`Global vs local <concepts/global_vs_local>`
- :doc:`Model Performance <concepts/model_performance>`
- :doc:`Working with Sparse or Null data<concepts/null_sparse_data>`


Datasets
^^^^^^^^

Here, we provide references to all the datasets used throughout these user guides as well as in our :doc:`Recipes <../examples/index>`.

Now it's time to start exploring!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a friendly reminder, Howso Engine is actively being developed and our team is constantly trying to improve documentation with new information and resources for a better user
experience. If you have ideas for how we could improve these user guides or would like to contribute, we welcome any feedback on our `github page <https://github.com/howsoai>`_!

.. toctree::
    :maxdepth: 2
    :hidden:

    basic_capabilities/index
    advanced_capabilities/index
    concepts/index
    datasets

