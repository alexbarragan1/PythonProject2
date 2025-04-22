import pandas as pd
import matplotlib.pyplot as plt

states = pd.DataFrame({
    'state': ['California', 'Texas', 'New York', 'Florida'],
    'abbreviation': ['CA', 'TX', 'NY', 'FL']
})

areas = pd.DataFrame({
    'state': ['California', 'Texas', 'New York', 'Florida'],
    'area': [163696, 268596, 54555, 65758]
})

populations = pd.DataFrame({
    'state': ['California', 'Texas', 'New York', 'Florida'],
    'population': [39538223, 29145505, 20201249, 21538187]
})

state_data = pd.merge(pd.merge(states, populations, on='state'), areas, on='state')
print("Merged State Data:")
print(state_data)

state_data['density'] = state_data['population'] / state_data['area']
top_dense = state_data.sort_values('density', ascending=False).head(2)
print("\nTop 2 Most Dense States:")
print(top_dense[['state', 'density']])

bins = [0, 10e6, 20e6, float('inf')]
labels = ['small', 'medium', 'large']
state_data['size_category'] = pd.cut(state_data['population'], bins=bins, labels=labels)
print("\nWith Size Categories:")
print(state_data[['state', 'population', 'size_category']])

plt.figure(figsize=(8, 6))
colors = ['red' if pop > 20e6 else 'blue' for pop in state_data['population']]
plt.scatter(state_data['area'], state_data['population'], c=colors)
plt.xlabel('Area (sq miles)')
plt.ylabel('Population')
plt.title('State Population vs Area')
plt.grid(True)

for i, row in state_data.iterrows():
    plt.text(row['area'], row['population'], row['abbreviation'])

plt.show()