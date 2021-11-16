![pandas-index-alignment](assets/combined.plot.png)

## Article not published yet

# Background

This image is probably one of my favourite outputs using Python. It took 5 minutes to produce where this could have been a 2 day job using Excel.

When working with engineering time series data a common problem is that the intervals of the datasets are all different e.g.
* 30 minute readings for electrical power (kVA)
* 1 minutely readings for process variables
* Some values only update once a day, or once a week, some even once month

When you have 100,000 readings it is difficult to align all these datasets into one and quite a task in Excel.

# Solution
In the Python ecosystem the `Pandas DataFrame` takes care of time series indexes.

# Example

Lets say you have 2 datasets. The one dataset has values in 30 minute intervals and the second dataset in 1 minutely intervals.

```python
    import pandas as pd
    df_30 = pd.DataFrame()
    df_1 = pd.DataFrame()
    combined_df = df_30.append(df_1)
```

