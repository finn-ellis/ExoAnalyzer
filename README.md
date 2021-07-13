# ExoAnalyzer
Analyzes data from the NASA exoplanet archive

Still need to make this a python package and clean up usage.

An example of using the tool:
```python
import exoanalyzer

data = exoanalyzer.data.query()
pairs = exoanalyzer.util.get_system_pairs(data)

exoanalyzer.plot_pair_comparison(pairs, 'pl_orbeccen', use_log10 = False, max_deviations = 3)
```