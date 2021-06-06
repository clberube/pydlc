# @Author: charles
# @Date:   2021-06-05 09:06:98
# @Email:  charles.berube@polymtl.ca
# @Last modified by:   charles
# @Last modified time: 2021-06-05 11:06:20


import numpy as np
import matplotlib.pyplot as plt


def dense_lines(ys, x=None, ny=100, ax=None, pad_y=0.01, normalize=True,
                **kwargs):
    """Returns a Density Line Chart.

    Args:
        ys (:obj:`list` of :obj:`1darrays`): The lines to plot.
        x (:obj:`1darray`, optional): The x values corresponding to
            the data passed with `ys`. If not provided, range(0, len(ys))
            is used.
        ny (:obj:`int`, optional): The vertical grid size. Higher values
            yield a smoother density estimation. Lower values may yield a
            pixelated result. Default: 100.
        ax (:obj:`matplotlib axes`, optional): The axes to plot on. If not
            provided a new figure will be created.
        pad_y (:obj:`float`, optional): The padding fraction to establish the
            grid limits past the data values. Must be greater than 0.
            Default: 0.01 (1%).
        normalize (:obj:`bool`, optional): Normalize the plot so the density
            is between 0 and 1. Default: True.
        **kwargs: Arbitrary keyword arguments to pass to plt.imshow().

    Returns:
        A plt.imshow() object.

    """
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
    gridx = np.linspace(x.min(),  # unused for now
                        x.max(),
                        x.shape[0])

    grid = np.zeros((ys.shape[0], gridy.shape[0], gridx.shape[0]))
    indices = np.searchsorted(gridy, ys) - 1

    for i, idx in enumerate(indices):
        grid[i, idx, range(len(x))] = 1

    grid = np.sum(grid, axis=0)

    if normalize:
        grid /= grid.max()

    extent = (gridx.min(), gridx.max(), gridy.min(), gridy.max())
    img = ax.imshow(grid, extent=extent, **kwargs)
    return img
