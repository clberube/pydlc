# @Author: charles.berube@polymtl.ca
# @Date:   2021-06-05 09:06:98
# @Last modified by:   charles.berube@polymtl.ca
# @Last modified time: 2021-06-05 09:06:15


import numpy as np
import matplotlib.pyplot as plt


def dlines(ys, x=None, ny=100, ax=None, pad_y=0.01, normalize=True,
           **kwargs):

    if ax is None:
        ax = plt.gca()

    if isinstance(ys, list):
        ys = np.array(ys)

    assert isinstance(ys, np.ndarray), (
           "`ys` must be a list of 1D arrays or a 2D array")

    assert pad_y > 0, (
           "`pad_y` must be greater than 0")

    if x is None:
        x = np.arange(ys.shape[1])

    kwargs.setdefault('aspect', 'auto')
    kwargs.setdefault('origin', 'lower')

    drange = ys.max() - ys.min()
    gridy = np.linspace(ys.min() - pad_y*drange,
                        ys.max() + pad_y*drange,
                        ny)
    gridx = np.linspace(x.min(),
                        x.max(),
                        len(x))
    grid = np.zeros((len(gridy), len(gridx)))

    for y in ys:
        idx = np.searchsorted(gridy, y) - 1
        grid[idx, range(len(x))] += 1

    if normalize:
        grid /= grid.max()

    extent = (gridx.min(), gridx.max(), gridy.min(), gridy.max())
    img = ax.imshow(grid, extent=extent, **kwargs)
    return img
