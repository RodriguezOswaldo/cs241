import pandas
import matplotlib.pyplot as plt

path = '/Users/ownos/Programming/cs241/week9/census.csv'
_data = pandas.read_csv(path)
print(_data.tail())