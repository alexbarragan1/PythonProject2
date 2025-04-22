import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

print("Vertical concatenation:")
print(pd.concat([df1, df2]))

print("\nHorizontal concatenation:")
print(pd.concat([df1, df2], axis=1))

print("\nConcatenation with keys:")
result = pd.concat([df1, df2], keys=['first', 'second'])
print(result)

print("\nAppend alternative using concat:")
print(pd.concat([df1, df2]))

df3 = pd.DataFrame({'A': [7, 8], 'C': [9, 10]})
print("\nConcatenate different columns:")
print(pd.concat([df1, df3]))

def clean_combine(df_list):
    combined = pd.concat(df_list)
    return combined.reset_index(drop=True)

print("\nClean combined result:")
print(clean_combine([df1, df2, df3]))