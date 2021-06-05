# PyDenseLines
Python implementation of the Density Line Chart by [Moritz &amp; Fisher (2018)](https://arxiv.org/abs/1808.06019). This chart is useful to visualize a large quantity of time series.

## Installation

Simply install DenseLines with `pip`.

```console
pip install DenseLines
```

## Usage

```python
import numpy as np
import matplotlib.pyplot as plt
from dlines import plot_dlines

# Generate random synthetic time series
x = np.linspace(0, 100, 50)
ys = []
for _ in range(1000):
    ys.append(3 + 1.5*np.random.randn(1)*np.exp(-x/100))

# Plot here
fig, axs = plt.subplots(1, 2, figsize=(8, 3), sharey=True, sharex=True)
axs[0].plot(x, np.array(ys).T, lw=1)  # a normal line chart
im = plot_dlines(ys, x, cmap='magma', ax=axs[1])  # the DenseLines chart
plt.colorbar(im)
plt.tight_layout()
plt.show()
```

<p align="center">
  <img src="./figures/example.png" width="80%">
</p>

## Algorithm
The following graphical abstract explains the algorithm [(source)](https://idl.cs.washington.edu/papers/dense-lines/).
<p align="center">
  <img src="./figures/dense-lines.png" width="80%">
</p>
