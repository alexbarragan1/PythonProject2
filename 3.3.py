import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Original Series:")
print(s)
try:
    s.index[0] = 'x'
except Exception as e:
    print(f"\nCannot modify index: {e}")

arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]]
multi_index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Subgroup'))
s_multi = pd.Series([100, 200, 300, 400], index=multi_index)
print("\nMultiIndex Series:")
print(s_multi)
print("\nAccess 'A' group:")
print(s_multi['A'])

df_multi = pd.DataFrame(np.random.randn(4, 2),
                       index=multi_index,
                       columns=['X', 'Y'])
print("\nMultiIndex DataFrame:")
print(df_multi)
print("\nAfter swaplevel():")
print(df_multi.swaplevel())
print("\nAfter sort_index():")
print(df_multi.sort_index(level=1))

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['x', 'y', 'z'])
print("\nOriginal DataFrame:")
print(df)
print("\nAfter reset_index():")
print(df.reset_index())
print("\nAfter set_index('B'):")
print(df.set_index('B'))

df1 = pd.DataFrame({'A': [1, 2]}, index=[0, 1])
df2 = pd.DataFrame({'A': [3, 4]}, index=[1, 2])
print("\nDataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
print("\nAddition result (automatic alignment):")
print(df1 + df2)