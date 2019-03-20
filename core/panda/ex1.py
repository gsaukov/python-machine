import pandas as pd

df = pd.read_csv('C:\\dev\machine\\resources\\gapminder.tsv', sep='\t')

print(df.head, '\n')

print(df.shape, '\n')

print(df.columns, '\n')
print(df.dtypes, '\n')

print(df.info(), '\n')

country_df = df['country']
print(country_df.head())
print(country_df.head())

country_df_dot = df.country
print(country_df_dot.head())

subset = df[['country', 'continent', 'year']]
print(subset.head())
print(subset.tail(3))

subset = df[[1]]
print(subset.head())

subset = df[[0, -1]]
print(subset.head())

subset = df.iloc[1]
print(subset.head())

subset = df.iloc[[0, -1]]
print(subset)

small_range = list(range(6))
subset = df.iloc[small_range]
print(subset.head())

print(df.iloc[1200:1205])

print(df.iloc[1315:1325, 2])


print(df.loc[1200:1205])
print(df.loc[0])
print(df.loc[99])
print(df.loc[0, 99, 999])

print(df.iloc[-1])
print(df.tail(1))

print(type(df.iloc[-1]))
print(type(df.tail(1)))


print(df.ix[42, 'country'])
print(df.loc[42, 'country'])
print(df.iloc[42, 0])
print(df.ix[42, 0])

print(df.ix[[56, 1200, 1456], [0, 3, 5]])
print(df.ix[[56, 1200, 1456], ['country', 'lifeExp', 'gdpPercap']])


