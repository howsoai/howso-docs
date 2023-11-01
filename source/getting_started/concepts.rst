Key Concepts
============

What makes the Howso Engine AI you can understand, trust, and control?  Howso is built on fundamentally different technology from today's black box AI, which enables a variety of new capabilities. Below, we review some of
our key technological differentiators.

Instance-Based Learning (IBL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Howso Engine is rooted in instance-based learning (IBL), which is truly data-centric analysis. As an IBL platform, Howso stores your data in memory and makes predictions
from the similarities and differences between data points, not an underlying black box model, leading to fully transparent and attributable decisions.

This is very different from today's typical AI workflows. Most AI today, such as deep neural networks, use models, or abstractions of relationships within data, to make predictions on new information.
By nature, these models are not human interpretable (“black box”), and their predictions cannot be mapped back to original data, making them inherently unexplainable.

To compete with the speed and performance of today's AI, Howso utilizes cutting edge advances in spatial query systems and information probability theory to make IBL practical and accurate. These technological
advances enable all of Engine's insight and analysis capabilites, including state-of-the-art understandability, reliability, and control.

- Rank order which data points contributed the most to your decisions.

  Unlike other AI tools, Howso calculates how much influence each original data point has on a prediction. This influence is related to the probability that the data point is representative of
  the prediction. Influence weights are computed across all features and then aggregated per data point; the most influential data have the highest total influence weights. Being able to see the
  influence of each data point
  on a decision provides direct evidence for why a decision was made.

- Outperform other commonly used feature importance metrics, including SHAP.

  Howso quantifies individual feature contributions to a prediction, i.e., how much an individual feature impacts a prediction. The concept of feature contribution is similar to the data science concept of "feature importance". However,
  Howso is robust against several common challenges (correlated features, redundant features, difference in scale between features, and multiple distinguishing features) faced by other feature importance tools,
  including the SHAP metric, which often lead to misleading results.

- Know Engine's confidence in each decision.

  Popular AI that are based on deep learning are often found to confidently predict and present patently false information as though it were true (informally known as "hallucinating")
  because they cannot accurately calculate uncertainty in their predictions. In contrast, Howso accurately measures the confidence levels of all the predictions it makes, and provides
  these metrics as part of its mission of transparency and understandability. In other words, Howso understands what it should know about the uncertainty of the data, and uses
  that to inform what it actually does know about the data.

- Maintain the integrity of your data and decisions, with real-world safety.

  Adversarial attacks attempt to maliciously deceive AI into making poor decisions. To be trusted with human-centric decisions, AI must be robust to these attacks. Howso outperforms other AI methods at both
  identifying which data is mostly likely malicious and maintaining
  decision-making integrity after the attack occurs.


