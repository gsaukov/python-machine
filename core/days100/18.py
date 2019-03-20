x = 'blue,red, green'.split(',')

print(x)
print(type(x))

A,B,C = x

print(A,B,C)

words = 'this is random text we are going to split apart'.split(' ')

print(words)

print(input('write me a sentence: ').split(' '))

dict = {1: 'tree', '2': 'apple', 'key': 'this is a value'}

print('this is the length of dict: ', str(len(dict)))
print(list(dict.keys()))
print(list(dict.values()), '\n')

for k in dict:
    print('did this print the keys? ', k)
for k in dict:
    print('did this print the value? ', dict[k])

dict2 = {'2': 'apple', 'key':'this is a value', 1: 'tree'}
print('order is different but are they equal? ', dict == dict2)

list = ['tree', 'apple', 1, 'love']
list2 = ['apple', 1, 'tree', 'love']
print('order is different but are they equal? ', list == list2)

import random
x=random.choice(dict2)
y=random.choice(list2)

print('when calling to chose something from dict2', x)
print('when calling to chose something from list2', y, '\n')

x = random.choice([dict2])
y = random.choice([list2])

print('when calling physical dictionary', x)
print('when calling physical list',  y, '\n')

x = random.choice(['one', 'two', 'three', 2])
print('passing a local list: ', x)


