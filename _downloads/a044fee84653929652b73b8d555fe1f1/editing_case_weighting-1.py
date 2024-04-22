import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("whitegrid")
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(8, 3))

x = np.linspace(-10, 10, num=100)
uniform_weights = np.array([1/len(x)] * len(x))
right_biased_weights = np.array([1] * (x <= 5).sum() + [2.5] * (x > 5).sum())
right_biased_weights = right_biased_weights / right_biased_weights.sum()

sns.kdeplot(ax=ax1, x=x, weights=uniform_weights, fill=True)
ax1.set_title("Uniformly-Weighted")
sns.kdeplot(ax=ax2, x=x, weights=right_biased_weights, fill=True)
ax2.set_title("x \u2265 5 Weighted 2.5x Normal")
plt.show()