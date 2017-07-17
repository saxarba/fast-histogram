from __future__ import division

import numpy as np

from .histogram_cython import histogram1d_cython, histogram2d_cython

__all__ = ['histogram1d', 'histogram2d']


def histogram1d(x, nx, xmin, xmax):
    """
    Compute a 1D histogram assuming equally spaced bins.

    Parameters
    ----------
    x, y : `~numpy.ndarray`
        The positon of the points to bin in the 1D histogram
    nx : int
        The number of bins in the x direction
    xmin, xmax : float, optional
        The range in the x direction

    Returns
    -------
    array : `~numpy.ndarray`
        The 1D histogram array
    """
    return histogram1d_cython(x, nx, xmin, xmax)


def histogram2d(x, y, nx, xmin, xmax, ny, ymin, ymax):
    """
    Compute a 2D histogram assuming equally spaced bins.

    Parameters
    ----------
    x, y : `~numpy.ndarray`
        The positon of the points to bin in the 2D histogram
    nx : int
        The number of bins in the x direction
    xmin, xmax : float, optional
        The range in the x direction
    ny : int
        The number of bins in the x direction
    ymin, ymax : float, optional
        The range in the x direction

    Returns
    -------
    array : `~numpy.ndarray`
        The 2D histogram array
    """
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    return histogram2d_cython(x, y, nx, xmin, xmax, ny, ymin, ymax)