[![DOI](https://zenodo.org/badge/374140211.svg)](https://zenodo.org/badge/latestdoi/374140211)


# PyDLC - Density Line Charts with Python
Python implementation of the Density Line Chart [(Moritz &amp; Fisher, 2018)](https://arxiv.org/abs/1808.06019) to visualize time series collections.

<p align="center">
  <img src="./figures/example.png" width="75%">
</p>

## Installation

### Python Package Index

```console
$ pip install pydlc
```

### Requirements
- [numpy](numpy.org/)
- [matplotlib](matplotlib.org/)


## Usage

### Example
The following example shows how to import and use the `dense_lines` plotting function.
```python
import numpy as np
import matplotlib.pyplot as plt
from pydlc import dense_lines

# Generate random synthetic time series
x = np.linspace(0, 90, 25)
ys = []
for _ in range(10000):
    ys.append(np.random.randn(1)*np.exp(-x/100))

# Plot here
fig, axs = plt.subplots(1, 2, figsize=(8, 3), sharey=True, sharex=True)
axs[0].plot(x, np.array(ys).T, lw=1)  # this is slow and cluttered
axs[0].set_title('Line Chart')
im = dense_lines(ys, x=x, ax=axs[1], cmap='magma')  # this is fast and clean
axs[1].set_title('Density Lines Chart')
fig.colorbar(im)
fig.tight_layout()
plt.show()
```

### Arguments
- ys (`list` of `1darray`): The lines to plot. Can also be
    passed as a `2darray`.
- x (`1darray`, optional): The x values corresponding to
    the data passed with `ys`. If not provided, `range(0, len(ys))`
    is used.
- ax (`matplotlib axes`, optional): The axes to plot on. If not
    provided a new figure will be created.
- ny (`int`, optional): The vertical grid size. Higher values
    yield a smoother density estimation. Default: 100.
- y_pad (`float`, optional): The padding fraction to set the
    grid limits past the data values. Must be greater than 0.
    Default: 0.01.
- normalize (`bool`, optional): Normalize the plot so the density
    is between 0 and 1. Default: True.
- **kwargs: Arbitrary keyword arguments to pass to `plt.imshow()`.

## Limitations
- All series to be included in the density estimation and passed in the `ys` argument must have the same length.
- The vertical grid size can be adjusted with the `ny` parameter. Higher values of `ny` yield a smoother density visualization. However, the horizontal grid size is currently limited to the same size as the input sequences and there is no parameter to adjust it (yet). 

## Algorithm
This graphical abstract explains the algorithm ([source](https://idl.cs.washington.edu/papers/dense-lines/)).
<p align="center">
  <img src="./figures/dense-lines.png" width="75%">
</p>
