import pandas as pd
pd.set_option('display.expand_frame_repr', False)

science = pd.DataFrame({
    'Job': ['Math', 'Everything'],
    'Born': ['March 14, 1879', 'July 10, 1856'],
    'Died': ['April 18, 1955', 'January 7, 1943'],
    'Age': [76, 86],
    'Known': ['very good', 'good']},

    index = ['Albert Einstein', 'Nikola Tesla'],
    columns = ['Name', 'Job', 'Born', 'Died', 'Age', 'Known']
)

print(science, '\n')

ages = science['Age']
print(ages, '\n')
print('Many pandas are also seen in numpy array methods')
print(ages.mean(), '\n')
print(ages.min(), '\n')
print(ages.max(), '\n')
print(ages.std(), '\n')


data = pd.read_csv('C:\\dev\machine\\resources\\scientists.csv')
print(data.head())

print(data['Age'], '\n')
print(data['Age'].mean(), '\n')

print(data['Age'].describe(), '\n')

ages = data['Age']

print(ages[ages>ages.mean()], '\n')

print('give me an element by element vector')

print(ages + ages)

print('or maybe you want to make the ages nuts: ', '\n', ages*ages)

print('The scalar will be recycled across all the elements in the vector')

print(ages+100)

print(ages)
print(ages + pd.Series([3,9,10,44,4]))

print(ages.sort_index(ascending=False))
print(data.sort_index(ascending=False))

