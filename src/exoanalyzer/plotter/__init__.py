import os
from matplotlib import pyplot as plt
import numpy as np
from ..util import get_readable
from ..util import get_pair_data, remove_outliers_from_both

def plot_pair_comparison(pair_data, plotLabel, **kwargs):
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
    defaultKwargs = {
        'use_log10': True,
        'max_deviations': None,
        'file_path': "./graphs/",
        'file_name': "Graph_of_"+plotLabel+".png",
    }
    kwargs = { **defaultKwargs, **kwargs }
    use_log10 = kwargs.get("use_log10")
    max_deviations = kwargs.get("max_deviations") or None

    extracted = None
    if use_log10:
        extracted = get_pair_data(pair_data, plotLabel, modifier = lambda v: np.log10(v))
    else:
        extracted = get_pair_data(pair_data, plotLabel)

    x = [vals[0]/vals[1] for vals in extracted]
    y = [vals[0] for vals in extracted]
    if max_deviations:
        remove_outliers_from_both(x, y, max_deviations)

    plt.scatter(x, y, color="red")

    # plt.legend(["A of Pair", "B of Pair"])
    # plt.xlabel("Ratio of " + readableLabels[plotLabel] + " (A/B)")
    # plt.ylabel("Ratio of " + readableLabels[plotLabelB] + " (A/B)")

    title = get_readable(plotLabel)
    if max_deviations:
        title = title + " (|x-x̄| < " + str(max_deviations) + "σ)"
    plt.title(title)
    xlabel = "Ratio of A/B"
    if use_log10:
        xlabel = "log10 of " + xlabel
    plt.xlabel(xlabel)
    ylabel = "A of Pair"
    if use_log10:
        xlabel = "log10 of " + ylabel
    plt.ylabel(ylabel)
    full_path = kwargs.get("file_path") + kwargs.get("file_name")
    print("Saving: '" + full_path + "', length of data: " + str(len(pair_data)))
    try:
        plt.savefig(full_path)
    except:
        os.mkdir(kwargs.get("file_path"))
        plt.savefig(full_path)