# @Author: charles
# @Date:   2021-06-05 11:06:90
# @Email:  charles.berube@polymtl.ca
# @Last modified by:   charles
# @Last modified time: 2021-06-05 11:06:27


import numpy as np
import matplotlib.pyplot as plt
from pydlc import dense_lines

# Generate random synthetic time series
x = np.linspace(0, 100, 50)
ys = []
for _ in range(1000):
    ys.append(3 + 1.5*np.random.randn(1)*np.exp(-x/100))

# Plot here
fig, axs = plt.subplots(1, 2, figsize=(8, 3), sharey=True, sharex=True)
axs[0].plot(x, np.array(ys).T, lw=1)
axs[0].set_title('Line Chart')
im = dense_lines(ys, x=x, ax=axs[1], cmap='magma')  # accepts plt.imshow() kwargs
axs[1].set_title('Density Lines Chart')
fig.colorbar(im)
fig.tight_layout()
plt.show()
