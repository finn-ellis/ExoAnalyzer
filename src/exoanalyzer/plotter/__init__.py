import os
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
from ..util import get_readable
from ..util import get_pair_data, remove_outliers_from_both

def save_plt(plt, file_path, file_name):
    full_path = file_path + file_name
    print("Saving: '" + full_path)
    try:
        plt.savefig(full_path)
    except:
        os.mkdir(file_path)
        plt.savefig(full_path)

def plot_pair_ratio(pair_data, plotLabel, **kwargs):
    """
    Creates a graph comparing the ratio of a specified data in pairs
    of planets to the first planet in the pair.

    Arguments:
        'use_log10': Base values in log10 (recommended for large data)
        'max_deviations': Removes outliers which deviate from the mean
                            by the standard deviation * this value.
        'file_path': File path to save graphs to.
        'file_name': Custom name for the file.
    """

    # setup arguments
    defaultKwargs = {
        'use_log10': True,
        'max_deviations': None,
        'file_path': "./graphs/",
        'file_name': f"Graph_of_{plotLabel}_Pair_Ratios.png",
    }
    kwargs = { **defaultKwargs, **kwargs }
    max_deviations = kwargs.get('max_deviations') or None

    # define axes
    extracted = get_pair_data(pair_data, plotLabel)
    x = [vals[0]/vals[1] for vals in extracted]
    y = [vals[0] for vals in extracted]

    # remove outliers
    if max_deviations:
        remove_outliers_from_both(x, y, max_deviations)

    # create the plot
    plt.scatter(x, y, color="red")

    if kwargs.get('use_log10'):
        axes = plt.gca()
        axes.set_yscale('log')
        axes.set_xscale('log')

    title = get_readable(plotLabel)
    if max_deviations:
        title = title + " (|x-x̄| < " + str(max_deviations) + "σ)"
    plt.title(title)
    plt.xlabel("Ratio of A/B")
    plt.ylabel("A of Pair")
    save_plt(plt, kwargs.get("file_path"), kwargs.get("file_name"))

def plot_dual(data, x_label, y_label, **kwargs):
    """
    Plot chart with two different categories as x and y
    """

    # setup arguments
    defaultKwargs = {
        'use_log10': True,
        'file_path': "./graphs/",
        'file_name': f"Graph_of_{x_label}_and_{y_label}.png",
    }
    kwargs = { **defaultKwargs, **kwargs }

    # get axes for
    x = [pl[x_label] for pl in data]
    y = [pl[y_label] for pl in data]

    plt.scatter(x, y, color="red")

    if kwargs.get('use_log10'):
        axes = plt.gca()
        axes.set_yscale('log')
        axes.set_xscale('log')

    x_readable = get_readable(x_label)
    y_readable = get_readable(y_label)
    plt.title(x_readable+" and "+y_readable)
    plt.xlabel(x_readable)
    plt.ylabel(y_readable)
    save_plt(plt, kwargs.get("file_path"), kwargs.get("file_name"))