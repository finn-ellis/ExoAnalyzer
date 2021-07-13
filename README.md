# ExoAnalyzer
Provides tools to analyze data from the NASA exoplanet archive.

Install using command:
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps exoanalyzer-fellis
```

An example of using the tool:
```python
import exoanalyzer

data = exoanalyzer.data.query()
pairs = exoanalyzer.util.get_system_pairs(data)

exoanalyzer.plot_pair_comparison(pairs, 'pl_orbeccen', use_log10 = False, max_deviations = 3)
```