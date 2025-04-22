import pandas as pd
import numpy as np

arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]]
index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Subgroup'))
df = pd.DataFrame({'Value': [10, 20, 30, 40], 'Data': [100, 200, 300, 400]}, index=index)
print("MultiIndex DataFrame:")
print(df)

print("\nSelect ('A', 1):")
print(df.loc[('A', 1)])

print("\nStacked DataFrame:")
stacked = df.stack()
print(stacked)

print("\nUnstacked DataFrame:")
print(stacked.unstack())

print("\nCross-section of Group 'A':")
print(df.xs('A', level='Group'))

print("\nMean by Group level:")
print(df.groupby(level='Group').mean())

print("\nRenamed axis:")
df_renamed = df.rename_axis(['Category', 'Subcategory'])
print(df_renamed)

print("\nFlattened index:")
df_flat = df.reset_index()
print(df_flat)