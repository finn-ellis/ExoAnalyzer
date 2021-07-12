# ExoAnalyzer
Analyzes data from the NASA exoplanet archive

Still need to make this a python package and clean up usage.

An example of using the tool:
```python
from query import query_db
from planet_pair_analyzer import get_system_pairs, plot_results

pair_data = get_system_pairs(query_db())
plot_results(pair_data, "pl_orbeccen", use_log10 = False, max_deviations=2)
plot_results(pair_data, "pl_bmasse", use_log10 = True, max_deviations=3)
plot_results(pair_data, "pl_orbsmax", use_log10 = True, max_deviations=2)
```