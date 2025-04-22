import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}, index=['row1', 'row2', 'row3'])

print("Original DataFrame:")
print(df)

print("\nAdd 5 to all elements:")
print(df + 5)

print("\nMultiply column A by 2:")
print(df['A'] * 2)

df2 = pd.DataFrame({
    'A': [10, 20],
    'B': [30, 40]
}, index=['row1', 'row2'])

print("\nSafe addition with fill_value=0:")
print(df.add(df2, fill_value=0))

print("\nColumn means:")
print(df.mean())

print("\nRow sums:")
print(df.sum(axis=1))

print("\nAggregate functions:")
print(df.agg(['mean', 'sum', 'std']))

print("\nColumn normalization (z-score):")
print((df - df.mean()) / df.std())

print("\nRow normalization:")
print(df.div(df.sum(axis=1), axis=0))

def standardize(df):
    return (df - df.mean()) / df.std()

print("\nStandardized DataFrame:")
print(standardize(df))