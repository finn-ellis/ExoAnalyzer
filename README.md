# ExoAnalyzer
Provides tools to analyze data and graph from the NASA exoplanet archive.

## Installation
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps exoanalyzer-fellis
```

## Example Code
```python
import exoanalyzer

data = exoanalyzer.data.query()
exoanalyzer.plot_dual(data, 'pl_orbsmax', 'pl_bmasse', use_log10 = True)

pairs = exoanalyzer.util.get_system_pairs(data)
exoanalyzer.plot_pair_ratio(pairs, 'pl_orbeccen', use_log10 = False, max_deviations = 3)
```

## Versions
### 0.0.14 Added:
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
### 0.0.13: Initial stable release.
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