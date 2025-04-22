import pandas as pd
import numpy as np

data = {
    'A': [1, np.nan, 3, 4],
    'B': [5, 6, np.nan, 8],
    'C': [9, 10, 11, np.nan]
}
df = pd.DataFrame(data)
print("Original DataFrame with NaN:")
print(df)

print("\nLocate NaN with isnull():")
print(df.isnull())

print("\nLocate non-NaN with notnull():")
print(df.notnull())

print("\nDrop rows with any NaN:")
print(df.dropna())

print("\nDrop columns with any NaN:")
print(df.dropna(axis=1))

print("\nDrop rows with all NaN:")
print(df.dropna(how='all'))

print("\nFill NaN with 0:")
print(df.fillna(0))

print("\nForward fill:")
print(df.fillna(method='ffill'))

print("\nBackward fill:")
print(df.fillna(method='bfill'))

dates = pd.date_range('2023-01-01', periods=4)
ts = pd.Series([1, np.nan, np.nan, 4], index=dates)
print("\nTime series with NaN:")
print(ts)

print("\nAfter interpolation:")
print(ts.interpolate())

def clean_data(df, strategy='ffill', fill_value=None):
    """Handle missing values with specified strategy"""
    if strategy == 'fill':
        return df.fillna(fill_value)
    elif strategy == 'ffill':
        return df.fillna(method='ffill')
    elif strategy == 'bfill':
        return df.fillna(method='bfill')
    elif strategy == 'interpolate':
        return df.interpolate()
    else:
        return df.dropna()

print("\nCleaned with forward fill:")
print(clean_data(df.copy(), 'ffill'))

print("\nCleaned with fill value 99:")
print(clean_data(df.copy(), 'fill', 99))