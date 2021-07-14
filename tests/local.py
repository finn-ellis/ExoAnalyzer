import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/src/")
import exoanalyzer

data = exoanalyzer.data.query()
exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_bmasse', use_log10 = True)
exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_orbper', use_log10 = True)
exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_orbeccen', use_log10 = True)

pairs = exoanalyzer.util.get_system_pairs(data)
exoanalyzer.plot_pair_ratio(pairs, 'pl_bmasse', use_log10 = True, max_deviations = 3)
exoanalyzer.plot_pair_ratio(pairs, 'pl_masse', use_log10 = True, max_deviations = 3)
exoanalyzer.plot_pair_ratio(pairs, 'pl_orbper', use_log10 = True, max_deviations = 3)