import pandas as pd
pd.set_option('display.expand_frame_repr', False)

s = pd.Series(['banana', 42])
print(s, '\n')

s = pd.Series(['Big Daddy', 'Master of Uniniverse'], index=['Person', 'Who'])
print(s, '\n')

s = pd.Series({'person': 'Bigger Daddy', 'who': 'Master of Universe'})
print(s, '\n')


s_new = pd.Series({'some new': 'Person', 'And even newer': 'Guy'})
s = s.append(s_new)
print(s, '\n')


s = pd.Series([['Big Daddy', '23'], ['Master of Uniniverse', '40'], ['and more', '22']], index=['Person', 'Who', 'try'])
print(s, '\n')


science = pd.DataFrame({
    'Name': ['Albert Einstein', 'Nikola Tesla'],
    'Job': ['Math', 'Everything'],
    'Born': ['March 14, 1879', 'July 10, 1856'],
    'Died': ['April 18, 1955', 'January 7, 1943'],
    'Age': [76, 86]
})
print(science, '\n')

science1 = pd.DataFrame({
    'Name': ['Albert Einstein', 'Nikola Tesla'],
    'Job': ['Math', 'Everything'],
    'Born': ['March 14, 1879', 'July 10, 1856'],
    'Died': ['April 18, 1955', 'January 7, 1943'],
    'Died1': ['April 18, 1955', 'January 7, 1943'],
    'Died2': ['April 18, 1955', 'January 7, 1943'],
    'Died3': ['April 18, 1955', 'January 7, 1943'],
    'Known': ['very good', 'good']},


    index = [76, 86],
    columns = ['Name', 'Job', 'Born', 'Died', 'Died1', 'Died2', 'Died3', 'Known']
)

print(science1, '\n')

row_i_want = science1.loc[86]
print(type(row_i_want))
print(row_i_want, '\n')

print(row_i_want.index)
print(row_i_want.values, '\n')

print(science.index)
print(science.values, '\n')

print(science.keys())
print(row_i_want.keys())
print(science1.keys(), '\n')

print(row_i_want.index[1])
print(row_i_want.keys()[1])
