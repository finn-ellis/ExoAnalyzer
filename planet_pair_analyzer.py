import os
import sys
from matplotlib import pyplot as plt
import numpy as np
import math
from query import query_db
from readables import readableLabels

def get_system_planets(data, do_sort = True):
    """Returns a dictionary where key = hostname and value = list of planets from data which is a list of planet data"""
    hosts = {}
    for planet_id in range(len(data)):
        planet = data[planet_id]
        hostname = planet['hostname']
        if not hostname in hosts:
            hosts[hostname] = []
        hosts[hostname].append(planet_id)
    if do_sort:
        for hostname, planets in hosts.items():
            hosts[hostname] = sorted(planets, key=lambda i: data[i]['pl_orbsmax'] or 0)
    return hosts

def get_system_pairs(data, do_sort = True):
    system_planets = get_system_planets(data, do_sort)
    pairs = []
    for host, planets in system_planets.items():
        if len(planets) > 1:
            for i in range(len(planets)):
                if i%2==0:
                    pairs.append((data[planets[i-1]], data[planets[i]]))
    return pairs

def is_num_clean(n):
    return not (math.isinf(n) or math.isnan(n))

def get_pair_data(pairs, label, clean=True, **kwargs):
    pairData = []
    for pair in pairs:
        valA, valB = pair[0].get(label), pair[1].get(label)
        if valA and valB:
            modifier = kwargs.get("modifier")
            if modifier:
                valA, valB = modifier(valA), modifier(valB)
            if clean:
                if valA != 0 and valB != 0 and is_num_clean(valA) and is_num_clean(valB):
                    pairData.append([valA, valB])
            else:
                pairData.append([valA, valB])
    return pairData

def get_is_outlier(array, max_deviations = 2):
    mean = np.mean(array)
    std = np.std(array)
    # dist_from_mean = abs(array - mean)
    is_outlier = lambda x: abs(x-mean) > max_deviations * std
    return is_outlier

def remove_outliers_from_both(a, b, md):
    is_outlier = get_is_outlier(a, md)
    removes = 0
    for i in range(len(a)):
        i = i-removes
        if is_outlier(a[i]):
            removes += 1
            a.pop(i)
            b.pop(i)

def plot_results(pair_data, plotLabel, **kwargs):
    defaultKwargs = {
        'use_log10': True,
        'file_path': "./graphs/",
        'file_name': "Graph_of_"+plotLabel+".png",
    }
    kwargs = { ** defaultKwargs, **kwargs }
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

    title = readableLabels[plotLabel]
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
    plt.savefig(full_path)

if __name__ == "__main__":
    pair_data = get_system_pairs(query_db())
    file_path = "/home/fellis/Documents/Code/ExoAnalyzer/graphs/"
    plot_results(pair_data, "pl_orbeccen", use_log10 = False, max_deviations=2)
    plot_results(pair_data, "pl_bmasse", use_log10 = True, max_deviations=3)
    plot_results(pair_data, "pl_orbsmax", use_log10 = True, max_deviations=2)