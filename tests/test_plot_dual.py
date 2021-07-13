import exoanalyzer

data = exoanalyzer.data.query()

exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_bmasse', use_log10 = True)