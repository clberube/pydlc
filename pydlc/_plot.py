# @Author: charles
# @Date:   2021-06-05 09:06:98
# @Email:  charles.berube@polymtl.ca
# @Last modified by:   charles
# @Last modified time: 2021-06-05 11:06:20


import numpy as np
import matplotlib.pyplot as plt


def dense_lines(ys, x=None, ax=None, ny=100, y_pad=0.01, normalize=True,
                **kwargs):
    """Returns a Density Line Chart.

    Args:
        ys (:obj:`list` of :obj:`1darray`): The lines to plot. Can also be
            passed as a `2darray`.
        x (:obj:`1darray`, optional): The x values corresponding to
            the data passed with `ys`. If not provided, range(0, len(ys))
            is used.
        ax (:obj:`matplotlib axes`, optional): The axes to plot on. If not
            provided a new figure will be created.
        ny (:obj:`int`, optional): The vertical grid size. Higher values
            yield a smoother density estimation. Lower values may yield a
            pixelated result. Default: 100.
        y_pad (:obj:`float`, optional): The padding fraction to establish the
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

    assert y_pad > 0, (
           "`y_pad` must be greater than 0")

    if x is None:
        x = np.arange(ys.shape[1])

    kwargs.setdefault('aspect', 'auto')
    kwargs.setdefault('origin', 'lower')

    nx = x.shape[0]
    x_range = np.arange(nx)
    y_pad *= (ys.max() - ys.min())

    y_grid = np.linspace(ys.min()-y_pad, ys.max()+y_pad, ny)
    x_grid = np.linspace(x.min(), x.max(), nx)

    grid = np.zeros((ny, nx))
    indices = np.searchsorted(y_grid, ys) - 1

    for idx in indices:
        grid[idx, x_range] += 1

    if normalize:
        grid /= grid.max()

    extent = (x_grid.min(), x_grid.max(), y_grid.min(), y_grid.max())
    img = ax.imshow(grid, extent=extent, **kwargs)
    return img
