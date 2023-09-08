"""
.. _howso scikit example:

Scikit Example
==============

An example to demonstrate the usage of Howso in "traditional" ML ways.

The Howso python package extends the `scikit-learn`_ Estimator via the following classes:

* :class:`howso.scikit.HowsoEstimator`
* :class:`howso.scikit.HowsoClassifier`
* :class:`howso.scikit.HowsoRegressor`

HowsoEstimator provides users with a Python interface that follows the conventions of sklearn estimators. For use
of Howso's functionality use :class:`howso.engine.Trainee`.

This is a simple example on how to use the :class:`howso.scikit.HowsoRegressor` which extends the
:class:`howso.scikit.HowsoEstimator` to fit data and make predictions based on that data.

.. _scikit-learn: http://scikit-learn.org/
"""

import os
import pandas as pd

from pprint import pprint
from howso.scikit import HowsoClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# sphinx_gallery_thumbnail_path = '_static/gallery/scikit.png'


# Get path of breast cancer data included in the python package.
data_path = os.path.join("breast_cancer.csv")

# Read in the data.
print("Reading breast cancer data set.")
df = pd.read_csv(data_path)

# Split the dataset into the feature (X) and targets (y)
X = df.drop('y', axis=1).values.astype(float)
y = df['y'].values.astype(float)

le = LabelEncoder()
le.fit(df['y'])
y = le.transform(df['y'])

print(f"Target values encoded from {list(le.classes_)} to "
      f"{list(le.transform(le.classes_))}.")

# Split the dataset into an 80/20 train/test set.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=True)

# Create a classifier.
hc = HowsoClassifier()

# Fit the training data.
print("Training on a random selection of 80% of the data.")
hc.fit(X_train, y_train)

# Test against the reserved test data.
print("Scoring against 20% reserve test data:")
score = hc.score(X_test, y_test)

# Print the resulting accuracy.
print(score)

# Detailed prediction results
results = hc.describe_prediction(X_test)
print("Getting details for most similar cases from the first prediction:")
pprint(results['explanation']['most_similar_cases'][0])

print("Getting class probabilities and classes for the model:")
probas = hc.predict_proba(X_test)
pprint(probas)
pprint(hc.classes_)
