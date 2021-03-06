# ExoAnalyzer
Provides tools to analyze data and graph from the NASA exoplanet archive.

Provides functions to graph various quantitative data about exoplanets.
See example code below for examples on how to use. List of data options coming soon.

## Installation
Stable release:
```
pip install exoanalyzer
```
Beta test versions:
```
pip install --index-url https://test.pypi.org/simple/ --no-deps exoanalyzer-fellis
```

## Example Code
```python
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
exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_bmasse', use_log10 = True)
exoanalyzer.plot_system_average(data, "st_met", "pl_bmasse", use_log10_main=False, use_log10_avg=True)
exoanalyzer.plot_ratio_to_greatest(data, "pl_bmasse", use_log10=True)

exoanalyzer.plot_pl_categories(data, 'pl_orbsmax', {
    "<1 AU": lambda a: a < 1,
    ">1 AU": lambda b: b > 1
})

pairs = exoanalyzer.util.get_system_pairs(data)
exoanalyzer.plot_pair_ratio(pairs, 'pl_orbeccen', use_log10 = False, max_deviations = 3)

exoanalyzer.plot_pair_comparison(pairs, 'pl_bmasse', {
    "Massive Inner": lambda a, b: a/b > 1,
    "Massive Outer": lambda a, b: a/b < 1
})
```

## Versions
### 0.0.18
#### Added:
    exoanalyzer.plot_system_average(data, main_label, avg_label, **kwargs)
        data: array
            raw data from .data.query()
        main_label: str
            data label to graph on the x-axis
        avg_label: str
            data label to graph on the y-axis (average of all planets in system)
        
        **kwargs
        use_log10_main: bool
            use log10 form for main label (x axis) (good for large values)
        use_log10_avg: bool
            use log10 form for avg label (y axis) (good for large values)
        file_path: str
            path to save the file to. defaults to './graphs/'
        file_name: str
            name of file to save. defaults to "Graph_of_{x_label}_and_{y_label}.png"

    exoanalyzer.plot_ratio_to_greatest(data, label, **kwargs)
        data: array
            raw data from .data.query()
        label: str
            data label to graph. x-axis is percentage, y is greatest.
        
        **kwargs
        use_log10: bool
            use log10 form on y axis (good for large values)
        file_path: str
            path to save the file to. defaults to './graphs/'
        file_name: str
            name of file to save. defaults to "Graph_of_{x_label}_and_{y_label}.png"

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