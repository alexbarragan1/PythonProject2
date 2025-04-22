import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Original Series:")
print(s)

new_index = ['a', 'b', 'c', 'd', 'e']
print("\nReindexed with fill_value=0:")
print(s.reindex(new_index, fill_value=0))

print("\nReindexed with ffill:")
print(s.reindex(new_index, method='ffill'))

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['row1', 'row2'])
print("\nOriginal DataFrame:")
print(df)

print("\nReindexed rows:")
new_rows = ['row1', 'row2', 'row3']
print(df.reindex(new_rows))

print("\nReindexed columns:")
new_cols = ['A', 'B', 'C']
print(df.reindex(columns=new_cols))

dates = pd.date_range('2023-01-01', periods=3)
ts = pd.Series([1, np.nan, 3], index=dates)
full_dates = pd.date_range('2023-01-01', periods=5)
print("\nOriginal time series:")
print(ts)

print("\nReindexed with missing dates:")
ts_reindexed = ts.reindex(full_dates)
print(ts_reindexed)

print("\nAfter interpolation:")
print(ts_reindexed.interpolate())

def reindex_data(data, new_index, method=None, fill_value=None):
    return data.reindex(new_index, method=method, fill_value=fill_value)

print("\nUsing reindex function:")
print(reindex_data(s, new_index=['a', 'c', 'e'], fill_value=99))

data = pd.Series([30, 10, 20], index=['c', 'a', 'b'])
print("\nOriginal data:")
print(data)

print("\nAfter reindex(['a','b','c']):")
print(data.reindex(['a','b','c']))

print("\nAfter sort_index():")
print(data.sort_index())

print("\nAfter sort_values():")
print(data.sort_values())