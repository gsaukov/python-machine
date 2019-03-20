i_am = 'grant'
age = 38

print('let us talk about {}.'.format(i_am))

print('{1} {0}'.format('love', 'choc', 'test', 'four'))

print('{:_>10}'.format('sucker'))
print('{:_<10}'.format('sucker'))
print('{:_^10}'.format('sucker'))

x = 'elephant'
print(x[:4])

x = 9-11
print(x)

x = 11-9
print(x)

print('{:+d}'.format(x))

print('{:06.2f}'.format(3.1415954654654987984693))

data = {'first': 'Hannah', 'last': 'Yomama', 'some': 'other'}
data.keys()
print('{first} {last}'.format(**data))
