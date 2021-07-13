import math
import numpy as np

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
    """
        Get pairs of planets.

        Args:
            'do_sort': Should the planets be sorted by distance from host star
    """
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