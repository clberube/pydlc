# PyDenseLines
Python implementation of the Density Line Chart by Moritz &amp; Fisher. Useful to visualize a large quantity of time series on a single chart.


## Example

```python
import numpy as np
import matplotlib.pyplot as plt
from dlines import dlines

# Generate random synthetic time series
x = np.linspace(0, 100, 50)
ys = []
for _ in range(1000):
    ys.append(3 + 1.5*np.random.randn(1)*np.exp(-x/100))

# Plot here
fig, axs = plt.subplots(1, 2, figsize=(8, 3), sharey=True, sharex=True)
axs[0].plot(x, np.array(ys).T, lw=1)
im = dlines(ys, x, cmap='magma', ax=axs[1])
plt.colorbar(im)
plt.tight_layout()
plt.show()
```

[!img](./figures/example.png)
