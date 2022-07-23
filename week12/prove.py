import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plot
import os


player = pd.read_csv("/Users/ownos/Programming/cs241/week12/basketball_players.csv")
# print(player.columns)
master = pd.read_csv('/Users/ownos/Programming/cs241/week12/basketball_master.csv')
nba = pd.merge(player, master, how="left", left_on="playerID", right_on="bioID")
print('Merged: ')
# print(nba.columns)

# part 1. question  1
mean = nba['points'].mean()
median = nba['points'].median()
min = nba['points'].min()
max = nba['points'].max()

print("==========================")
print(f'Min: {min}')
print(f'Max: {max}')
print(f'Mean: {mean}')
print(f'Median: {median}')

# part 1. question  2
sort = nba[["year", "useFirst", "lastName", "tmID", "points"]].sort_values("points", ascending=False).head(10).max()
print("==========================")
print('Best player: ')
# print(sort)
print("==========================")


# part 1. question  3
nba["reboundsPerGame"] = nba["points"] / nba["GP"]
# sns.boxplot(data=nba.reboundsPerGame)
# plot.show()

# sns.boxplot(data=nba[["rebounds", "assists","points"]])
# plot.show()

nba["total_points"] = nba["points"] + nba["PostPoints"]
nba["total_assists"] = nba["assists"] + nba["PostAssists"]
nba["total_rebounds"] = nba["rebounds"] + nba["PostRebounds"]

# sns.boxplot(data=nba[["total_points", "total_assists", "total_rebounds"]])
# plot.show()


# part 1. question  4

nba_grouped_year = nba.groupby("year").median()["points"].reset_index()
# sns.regplot(data=nba_grouped_year, x="year", y="points").set_title("Points Per Year")
# plot.show(f'{nba_grouped_year}')


print('Grouped by Year')
# print(nba_grouped_year.head(10))


# part 2, question 1

nba_grouped_year = nba[["reboundsPerGame", "year"]].groupby("year").median()
# print('me')
# print(nba_grouped_year)
print('Me')

print(nba.columns)
# print(nba['points'].head(10))


nba['sum_attempted'] = (nba['fgAttempted'] + nba['ftAttempted'] + nba['threeAttempted'] + nba['PostthreeAttempted'] + nba['PostftAttempted'] + nba['PostfgAttempted'])
especifico = nba[['firstName', 'lastName', "playerID", 'sum_attempted', 'points']].sort_values("sum_attempted", ascending=False).head(10)
print('especifico: ')
print(especifico)


