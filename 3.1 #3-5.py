import pandas as pd
import csv

data = [
    ['Date', 'Temperature', 'Humidity'],
    ['2023-01-01', 72, 45],
    ['2023-01-02', 68, 50],
    ['2023-01-03', 75, 42],
    ['2023-01-04', 80, 38],
    ['2023-01-05', 77, 40],
    ['2023-01-06', 82, 35],
    ['2023-01-07', 85, 30],
    ['2023-01-08', 79, 45],
    ['2023-01-09', 74, 50],
    ['2023-01-10', 71, 55]
]

with open('weather.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

weather = pd.read_csv('weather.csv')
print("\nWeather DataFrame:")
print(weather)

print("\nFirst 5 rows:")
print(weather.head())
print("\nLast 5 rows:")
print(weather.tail())

print("\nDataFrame info:")
print(weather.info())
print("\nDescriptive statistics:")
print(weather.describe())

weather['Date'] = pd.to_datetime(weather['Date'])

temp_series = weather.set_index('Date')['Temperature']
print("\nTemperature Series with datetime index:")
print(temp_series)

print("\nTemperatures from Jan 3 to Jan 7:")
print(temp_series['2023-01-03':'2023-01-07'])

morning_temps = pd.Series([68, 70, 72],
                         index=pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
                         name='Morning')

evening_temps = pd.Series([65, 68],
                         index=pd.to_datetime(['2023-01-02', '2023-01-03']),
                         name='Evening')

print("\nMorning Temperatures:")
print(morning_temps)
print("\nEvening Temperatures:")
print(evening_temps)

temp_diff = morning_temps - evening_temps
print("\nTemperature Difference (Morning - Evening):")
print(temp_diff)
