# ExoAnalyzer
Provides tools to analyze data and graph from the NASA exoplanet archive.

Provides functions to graph various quantitative data about exoplanets.
See example code below for examples on how to use. List of data options coming soon.

## Installation
```
pip install --index-url https://test.pypi.org/simple/ --no-deps exoanalyzer-fellis
```

## Example Code
```python
data = exoanalyzer.data.query()
exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_bmasse', use_log10 = True)
exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_orbper', use_log10 = True)
exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_orbeccen', use_log10 = True)

pairs = exoanalyzer.util.get_system_pairs(data)
exoanalyzer.plot_pair_ratio(pairs, 'pl_bmasse', use_log10 = True, max_deviations = 3)
exoanalyzer.plot_pair_ratio(pairs, 'pl_masse', use_log10 = True, max_deviations = 3)
exoanalyzer.plot_pair_ratio(pairs, 'pl_orbper', use_log10 = True, max_deviations = 3)
```

## Versions
### 0.0.17
#### Added:
    exoanalyzer.util.get_label_list()
    > returns:
        list: A list of all possible data categories for obtainable exoplanet data.

### 0.0.14: New feature
#### Added:
    exoanalyzer.plot_dual(data, x_label, y_label, **kwargs)
        data: array
            raw data from .data.query()
        x_label: str
            data label to graph on the x-axis
        y_label: str
            data label to graph on the y-axis
        
        **kwargs
        use_log10: bool
            use log10 form (good for large values)
        file_path: str
            path to save the file to. defaults to './graphs/'
        file_name: str
            name of file to save. defaults to "Graph_of_{x_label}_and_{y_label}.png"

#### Changed:
    exoanalyzer.plot_pair_comparison -> exoanalyzer.plot_pair_ratio
    
### 0.0.13: Initial stable release.
    exoanalyzer.plot_pair_comparison(pair_data, plotLabel, **kwargs)
        pair_data: array
            data from .util.get_system_pairs(data)
        plotLabel: str
            data label to graph
        
        **kwargs
        use_log10: bool
            use log10 form (good for large values)
        max_deviations: int
            outlier removal. values cannot deviate from the mean by more than std*this number.
        file_path: str
            path to save the file to. defaults to './graphs/'
        file_name: str
            name of file to save. defaults to "Graph_of_{plotLabel}.png"