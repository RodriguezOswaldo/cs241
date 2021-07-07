import matplotlib.pyplot as plt
import pandas
from datetime import datetime

data = pandas.read_csv('/Users/ownos/Programming/cs241/week12/weather_year.csv')
# print(data)
# print(len(data))
# print(data.columns)
# print()
# print(data["EDT"])
# print()
# print(data[["EDT", "Mean TemperatureF"]])
# print()
# print(data.EDT)
# print('head')
# print(data.EDT.head())
# print(data.EDT.head(10))
# print(data["Mean TemperatureF"].head())
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]
# print(data.mean_temp.tail())
# print(data.mean_temp.head())
# print(data.cloud_cover.std())
# print(data.mean_temp.hist())
# print(data.date.head())
first_date = data.date.values[0]
# print(first_date)

datetime.strptime(first_date, "%Y-%m-%d")
# print(first_date)
# data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
# print(data.date.head())
#
# data.index = data.date
# print(data.head())
# data.ix[datetime(2012, 8, 19)]
# print(me)
# check for empty data
# empty = data.apply(lambda col: pandas.isnull(col))
# print(empty)
# print(empty.events.head(10))
# print(data.dropna(subset=["events"]))
# fill the empty data with a "0"
data.events = data.events.fillna("0")
# print(data.events.head(10))
# accessing individual row using iloc[] instead of irow()
# print(data.iloc[365])

num_rain = 0
for idx, row in data.iterrows():
    if "Rain" in row["events"]:
        num_rain += 1
# print("Days with rain: {0}".format(num_rain))

# freezing_days = data[data.max_temp <= 32]

# print(freezing_days)
#
# print(freezing_days[freezing_days.min_temp >= 20])

# print(data[(data.max_temp <= 32) & (data.min_temp >= 20)])

temp_max = data.max_temp <= 32
# print(type(temp_max))
# print(data[temp_max])
temp_min = data.min_temp >= 20
# print(temp_min)
print('uh')
temp_both = temp_min & temp_max
# print(temp_both.any())

try:
    data["Rain" in data.events]
except:
    pass # "KeyError: no item named False"

# print(data[data.events.apply(lambda e: "Rain" in e)])

cover_temps = {}
for cover, cover_data in data.groupby("cloud_cover"):
    cover_temps[cover] = cover_data.mean_temp.mean()  # The mean mean temp!
# print(cover_temps)

# for (cover, events), group_data in data.groupby(["cloud_cover", "events"]):
    # print("Cover: {0}, Events: {1}, Count: {2}".format(cover, events, len(group_data)))
# print(data.events.unique()
for event_kind in ["Rain", "Thunderstorm", "Fog", "Snow"]:
    col_name = event_kind.lower()  # Turn "Rain" into "rain", etc.
    data[col_name] = data.events.apply(lambda e: event_kind in e)
print(data.fog.sum())


#Plotting