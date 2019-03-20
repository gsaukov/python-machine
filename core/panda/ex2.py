import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('C:\\dev\machine\\resources\\gapminder.tsv', sep='\t')

print(df.head, '\n')
print(df.columns, '\n')

print(df.groupby('year')['lifeExp'].mean(), '\n')

group_years_df  = df.groupby('year')
print(group_years_df, '\n')

group_LE_df  = group_years_df['lifeExp']
print(group_LE_df)

print(group_LE_df.mean())


print('Population grouped by year...')
print(df.groupby('year')['pop'].mean())

print('Population grouped by year...')
print(df.groupby('year')['gdpPercap'].max())

print(df.groupby(['year', 'continent'])[['lifeExp','gdpPercap']].mean())

print(df.groupby(['lifeExp','gdpPercap'])[['year', 'continent']].mean())



dir(df.groupby(['lifeExp','gdpPercap']))

#nununique
print(df.groupby(['continent'])['country'].nunique())

print('same but using diff method, looking at occurances of each value')
print(df.groupby(['continent'])['country'].value_counts())

life_Exp_globally_year = df.groupby('year')['lifeExp'].mean()
print(life_Exp_globally_year)
plt.plot(life_Exp_globally_year)
plt.plot(df.groupby(['year'])[['gdpPercap', 'pop']].max())
plt.show()


print('bye')





