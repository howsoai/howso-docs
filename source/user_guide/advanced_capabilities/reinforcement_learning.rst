.. currentmodule:: howso.engine


Reinforcement Learning
======================
.. topic:: What is covered in this user guide

    In this guide, you will learn the basics of how to incorporate Howso Engine into a Reinforcement Learning (RL) framework.


Objectives: what you will take away
-----------------------------------
- **Definitions & Understanding** How :py:class:`~Trainee` s fits into a RL framework.
- **How-To** train and retrain a :py:class:`~Trainee` during RL.


Prerequisites: before you begin
-------------------------------
- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have a understanding of :doc:`Howso Engine workflow and concepts <../basic_capabilities/basic_workflow>`
- You have a basic understanding of the concepts of RL and a python RL framework, preferably `Gymnasium <https://gymnasium.farama.org/>`__.


Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover and provide a complete example using several RL games:

- `RL recipe <https://github.com/howsoai/howso-engine-rl-recipes>`__

Concepts & Terminology
----------------------
To understand this guide, we recommend being familiar with the following concepts:

- :ref:`trainee`
- :ref:`conviction`
- :ref:`react`
- :ref:`case`
- :ref:`feature`
- :ref:`action_features`
- :ref:`context_features`

Additional concepts to be familiar with include the `Gymnasium RL Framework <https://gymnasium.farama.org/>`_ and the RL games in the recipes,
`Cartpole <https://gymnasium.farama.org/environments/classic_control/cart_pole/>`_ and
`Wafer Thin Mints (PDF Download Link) <https://www.aaai.org/ojs/index.php/AIIDE/article/download/5218/5074>`__.

How-To Guide
------------
In the learning cycle of RL as shown below, Howso Engine acts as the Agent. As an Agent, Howso Engine both outputs an action value as well as intakes the observation and resulting reward.
Once the reward (goal) and observations are processed, the Howso Engine is trained again based on the results and another action is output.

.. image:: /_images/RL.png

Image Source: `https://gymnasium.farama.org/content/basic_usage/ <https://gymnasium.farama.org/content/basic_usage/>`__

Setup
^^^^^
The Howso Engine Trainee must be initialized in the RL framework before the learning loop. As part of the setup process, enabling :py:meth:`Trainee.set_auto_analyze_params`
can help the user analyze the Trainee after all training steps. This methods eliminates the need to manually analyze after training, which can be done.

.. code-block:: python

    trainee.set_auto_analyze_params(
        auto_analyze_enabled=True,
        context_features=self.context_features + self.action_features,
        rebalance_features=self.goal_features
    )


Action
^^^^^^
In the Action phase, a standard :meth:`Trainee.react` call will provide the resulting action. Most of the parameters have been covered in the other Howso Engine guides,
however ``into_series_store`` may be new for most users. Since we are using the Trainee to learn a series of actions, underneath the hood Engine is treating the contexts and cases
as part of a series.  The parameter ``into_series_store`` allows the user to label the series store, which in this case, is the round or loop number.  The parameter ``goal_features_map```
conditions the results towards the specified goal, which is typically to maximize a score.

.. code-block:: python

    react = trainee.react(
                desired_conviction=desired_conviction,
                contexts=[[observation]],
                context_features=self.context_features,
                action_features=self.action_features,
                goal_features_map=self.goal_features_map,
                into_series_store=str(round_num),
            )
    action = react['action']['action'][0]

    return action

Environment, Reward, and Observation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This step processes the action from Action phase and outputs a observation and reward. The reward and observation is sent back to the Trainee where
it can be used to train the Trainee. These steps are generally handled by your RL framework.

Agent
^^^^^
This is the step where Howso Engine learns from the previous loop, by training in the new reward value as a goal. The Trainee should be analyzed after every train step, which
should be automated by the :py:meth:`Trainee.set_auto_analyze_params` method.

.. code-block:: python

    trainee.train(
        features=self.goal_features,
        cases=[[score]],
        series=str(round_num),
    )

Completion
^^^^^^^^^^
The RL learning phase is repeated until the desired stop condition, whether it is a termination due to result or a truncation such as a limited number of steps. The Trainee
has now been trained and analyzed using Reinforcement Learning.


API References
--------------
- :meth:`Trainee.set_auto_analyze_params`
- :meth:`Trainee.react`
- :meth:`Trainee.train`

