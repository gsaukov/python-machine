import numpy as np

print(np.__version__)

list = [12, 998, 45.73, 9, 7, 21, 0.6]

print('Starting list: ', list)

one_d_array = np.array(list, dtype = int)
print('My first 1 Dimensional array', one_d_array)

x = np.arange(2, 66).reshape(8, 8)
print(x)

print()

y = np.arange(2, 30, 8)
print(y, '\n')

x = np.zeros(10)
print(x, '\n')
x[[3, 6]] = 21
x[1] = 8
print(x, '\n')

x = np.arange(7, 21)
print(x, '\n')

x = x[::3]
print(x, '\n')

x = x[::-1]
print(x, '\n')

x = np.arange(0, 100).reshape(10, 10)
x = x[::2, ::-3]
print(x, '\n')

x = np.arange(0, 100).reshape(10, 5, 2)
x = x[::2, ::-3]
print(x, '\n')

x = range(0, 10)
x = x[1::]
print(x, '\n')