.. currentmodule:: howso.engine


Working with Null and Sparse Data
=================================
.. topic:: What is covered in this user guide

    In this guide, you will learn the basics of using sparse data in your :class:`~Trainee` s as well as
    understand some of the prediction performance characteristics around data of increasing sparsity.


Objectives
----------
- **Definitions & Understanding** of what sparse data are, how to use them with a :class:`~Trainee`, and
  how prediction performance changes as data sparsity increases.

Prerequisites
-------------
- You have successfully :doc:`installed Howso Engine <../../getting_started/installing>`
- You have an understanding Howso's :doc:`basic workflow <../basic_capabilities/basic_workflow>`.

Concepts & Terminology
----------------------
This guide focuses primarily on the concept of sparse data.  We additionally recommend being familiar with the following concepts:

- :ref:`trainee`
- :ref:`react`
- :ref:`action_features`
- :ref:`context_features`
- :doc:`Feature Attributes <../basic_capabilities/feature_attributes>`

Sparse Data
^^^^^^^^^^^
The term `sparse data <https://en.wikipedia.org/wiki/Sparse_matrix>`_ usually refers to data which consist of primarily zeroes, with
few values being nonzero.  While Howso Engine has no trouble with these sorts of data, this article is primarily concerned with data that
are sparse in that the data contain **missing values**.  For example,

.. math::

  \begin{bmatrix}
    1   & NaN & a      & 5\\
    2   & -2  & (null) & 6\\
    NaN & -3  & c      & NaN\\
    4   & -4  & d      & 8\\
  \end{bmatrix}.


How-To Guide
------------
Howso Engine handles sparse and missing data without any extra setup.  Simply :meth:`~Trainee.train` your data, with or without missing values, and the
Engine will handle them.  There is no need to preprocess missing data and, in fact, preprocessing missing data may **harm predictive power or robustness
to unseen data**.  As such, we recommend performing no preprocessing if possible.

.. note::

  Preprocessing may be warranted if missing values are used to represent something with specific meaning in your dataset.  In that instance, it would be
  best to replace missing values that abide by this representation with a non-missing value and leave any values which are truly missing as they are.


What a Missing Value Means
^^^^^^^^^^^^^^^^^^^^^^^^^^
When computing similarity between cases, a missing value is considered to be of maximal :ref:`uncertainty`
for that feature.  This is true even if both cases have missing values in the same place.  After all, :math:`NaN \neq NaN`.  As mentioned above,
if the data you are working with contain missing values that represent something specific, those should be changed from missing values to something
else.  If we were to treat those values as missing, matches would not be considered similar and may therefore harm predictions in that instance.


How Well are Sparse Data Handled
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As shown in the :download:`Sparse Data Prediction <https://github.com/howsoai/howso-engine-recipes/blob/main/engine_sparse_data.ipynb>` recipe, we maintain high degrees of accuracy even as
large percentages of the data are replaced with missing values.

.. image:: /_images/plots/sparse_data_plot.png
  :alt: A plot showing the accuracy, precision, and recall as sparsity increases from 0 to 100%.


Outputting Missing Values
^^^^^^^^^^^^^^^^^^^^^^^^^
In order to output missing values, the ``allow_null`` feature attribute must be set in the ``bounds`` of that feature.  If this is set, both
discriminative and generative :meth:`~Trainee.react` s can output missing values.  This can be set using :func:`~howso.utilities.infer_../basics/feature_attributes`.

.. code-block:: python

  features = infer_feature_attributes(
    df,
    features={"Clump_Thickness": {"bounds": {"allow_null": True}}}
  )
  trainee = Trainee(features=features)
  trainee.train(df)
  trainee.react(contexts=contexts, action_features=action_features)


API References
--------------
- :py:class:`~Trainee`
- :py:meth:`Trainee.train`
- :py:meth:`Trainee.analyze`
- :func:`howso.utilities.infer_../basics/feature_attributes`
- :func:`Trainee.react`

