import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/src/")
import exoanalyzer

data = exoanalyzer.data.query(query_columns = [
    "pl_name",
    "hostname",
    "pl_orbper",
    "pl_orbsmax",
    "pl_orbeccen",
    "pl_bmasse",
    "st_met",
    "st_teff",
    "st_metratio",
    "st_mass"])
# exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_bmasse', use_log10 = True)
# exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_orbper', use_log10 = True)
# exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_orbeccen', use_log10 = True)
# exoanalyzer.plot_dual(data, 'st_mass', 'pl_bmasse', use_log10 = True)

# pairs = exoanalyzer.util.get_system_pairs(data)
# exoanalyzer.plot_pair_ratio(pairs, 'pl_bmasse', use_log10 = True, max_deviations = 3)
# exoanalyzer.plot_pair_ratio(pairs, 'pl_orbper', use_log10 = True, max_deviations = 3)
# exoanalyzer.plot_pair_ratio(pairs, 'pl_orbsmax', use_log10 = True)

exoanalyzer.plot_system_average(data, "st_mass", "pl_bmasse", use_log10_main=True, use_log10_avg=True)
exoanalyzer.plot_system_average(data, "st_teff", "pl_orbsmax", use_log10_main=True, use_log10_avg=True)
exoanalyzer.plot_system_average(data, "st_met", "pl_bmasse", use_log10_main=False, use_log10_avg=True)
exoanalyzer.plot_ratio_to_greatest(data, "pl_bmasse", use_log10=True)
exoanalyzer.plot_ratio_to_greatest(data, "pl_orbsmax", use_log10=True)