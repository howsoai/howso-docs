Howso's Trustworthy AI
========

Whether you are an individual or a large enterprise, AI has likely already impacted your daily life. While AI has likely opened up many exciting new opportunities, you have probably 
heard stories of AI generating "hallucinations" and grossly biased predictions. Understandably, you might have a nagging suspicion that the AI available today cannot be trusted. 
And because this AI is inherently “black box”, you cannot understand, trust, or control why its decisions were made, the data it used, or its reliability.  

Enter Howso. Howso is the result of years of research and innovation to solve the problem of trustworthy AI. 
Howso is rooted in instance-based learning, so all of its decisions are made directly from the data. Howso stores information in memory and makes predictions from the 
similarities and differences between data points, not an underlying black box model, leading to fully transparent decisions with perfect attribution back to the source data. 
Howso utilizes cutting edge advances in the fields of statistics, physics, game theory, and information theory to make IBL understandable, performant, versatile, and trustworthy. 

In the spirit of providing trustworthy AI to all, Howso has open sourced its Engine platform. Engine enables you to... 

- Make accurate predictions and avoid hallucinations

- Perfectly cite the data used to make predictions

- Utilize state of the art interpretability tools, to identify how your dataset influenced predictions

- Automatically poerform a variety of data science tasks

- Identify and maintain integretity during adversarial attacks on your data

- And more!

So, how can you use Howso Engine, to harness the power of AI without sacrificing understanding, trust, and control? Our docs are purpose 
built to provide you the tools and resources to confidently harness Engine to make important, human-centric decisions. Join us and learn... how so? 

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

    Currently, we only work with structured data. We are in beta testing for semi-structured data, tiptoeing toward generative language, and images are on the distant horizon.

- Feature width

    We work well with hundreds of features, but we are not yet able to handle thousands of features in practical applications.

- Very large datasets

    Handling very large datasets with subtle signals currently requires manual work from engineering, data science, and subject matter expert teams.

What's next? How to use these guides...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have not already installed Howso Engine, that's your first step! You can find our :doc:`installation guide here <installing>`.

Once you're installed, you can try out Howso using a variety of pre-built :doc:`jupyter notebook examples <../examples>`. These notebooks will provide "recipes" for how to utilize
Understandable AI in many applications.

Additionally, you can gain insight into Howso's capabilities by exploring our :doc:`key concepts <concepts>`, :doc:`terminology <terminology>`, and :doc:`user guides <../user_guide>` or by digging into our python code :doc:`API references <../api_reference>`.

And, as always, we welcome your participation and feedback on our `github page <https://github.com/howsoai>`_!
