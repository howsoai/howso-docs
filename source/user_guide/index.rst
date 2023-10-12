===========
User Guides
===========

User guides are designed to help you get started working with Howso Engine. These guides cover the basics of setting up the Engine for
a variety of data science tasks, explore Howso's understandability toolkit, and demonstrate advanced capabilities useful for particular applications
of Howso Engine. Additionaly, they teach you terminology that is unique to Howso, provide insight into how Howso approaches data science
problems, and identify key API references. They also contain examples of how a particular tool might be used within a data science workflow. To help you decide which user guide
is best for you, we have grouped them into three categories:

The Basics
^^^^^^^^^^

Here, you will gain insight into Howso Engine can be implemented so you have full trust and control of your data and decisions. 
These guides will acquaint you with the basic workflow for building a :py:class:`~Trainee`
and making your first AI predictions. Additionally, we review the important step of setting up your - :py:meth:`~howso.utilities.infer_feature_attributes`, which helps the Engine
understand the relationships between your data. Finally, we demonstrated the basics of editing your :py:class:`~Trainee`, and storing it for future use. 

   - :doc:`Basic Workflow <basic_workflow>`
   - :doc:`Feature Attributes <feature_attributes>`
   - :doc:`Derived Features <derived_features>`
   - :doc:`Predictions <predictions>`
   - :doc:`Editing Trainees and Case Weighting <editing_case_weighting>`
   - :doc:`Saving and Loading <save_load>`

Intro to Understandability
^^^^^^^^^^^^^^^^^^^^^^^^^^

With these guides, you will learn how to use Howso's unique tools for understandability and trust. You will gain skills understanding Engine's predictions, including how
to identify the data that directly influenced your decisions, counterfactuals, and Engine's uncertainty. Additionally, these guides will show you how to understand and use
Howso's feature importance tools.

    - :doc:`Understanding Predictions <understanding_predictions>`
    - :doc:`Model Performance <model_performance>`
    - :doc:`Influential Data, Counterfactuals, and Uncertainties of Predictions <influential_data_counterfactuals_uncertainty>`
    - :doc:`Feature Importance <feature_importance>`

Advanced Capabilities
^^^^^^^^^^^^^^^^^^^^^

These guides introduce you to a variety of capabilities that make the Howso Engine so versatile to use. This includes anomaly detection, 
bias mitigation, and reinforcement 
learning, as well as Howso's special techniques for handling json, sparse, and time series data and generative analysis. Although these guides are fairly generic, they should be very easily
adapted to your specific dataset or application.

    - :doc:`Anomaly Detection <anomaly_detection>`
    - :doc:`Bias Mitigation <bias_mitigation>`
    - :doc:`Generative AI and Data Synthesis <generative_AI_synth>`
    - :doc:`Handling Sparse Data <sparse_data>`
    - :doc:`JSON Features <json_features>`
    - :doc:`Reinforcement Learning <reinforcement_learning>`
    - :doc:`Time Series and Sequential Data Analysis <time_series>`

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

    basic_tools
    understandability_tools
    capabilities
    datasets
    
