import pandas
import matplotlib.pyplot as plt

path = '/Users/ownos/Programming/cs241/week9/census.csv'
data = pandas.read_csv(path)
print(data.tail())
# mean = _data.income.mean()
# max = data[0].max()
col = data.columns
age = data[0].max()
print(age)