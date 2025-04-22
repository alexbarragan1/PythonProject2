import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print("Original Series:")
print(s)

print("\nAfter np.exp():")
print(np.exp(s))

print("\nAfter np.log():")
print(np.log(s))

s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20], index=['b', 'c'])
print("\nSeries 1:")
print(s1)
print("\nSeries 2:")
print(s2)

print("\nElement-wise addition:")
print(s1 + s2)

print("\nUsing np.where():")
print(pd.Series(np.where(s > 1.5, 'high', 'low'), index=s.index))

def clean_ufunc(series, ufunc, fillna=0):
    result = ufunc(series)
    return result.fillna(fillna)

print("\nCleaned log with fillna=0:")
print(clean_ufunc(pd.Series([1, 0, -1]), np.log, 0))

arr = np.array([1, 2, 3])
print("\nNumPy array * 2:")
print(arr * 2)

print("\nPandas Series * 2:")
print(s * 2)