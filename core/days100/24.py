import numpy as np
x = np.ones((5, 5))
print('normal array: \n', x)

print('\n')

x[::] = 0
print(x, '\n')
x[2:] = 1
print(x, '\n')
x[1:-1] = 2
print(x, '\n')

x[1:-1, 1:-1] = 3
print(x, '\n')


x = np.ones((5, 5))
x[-1:1, -1:1] = 4
print(x, '\n')


x = np.ones((5, 5))
x[1:4, 1:4] = 4
print(x, '\n')





x = [10, 15, 22, 44]
x = np.append(x, [[30, 40, 50], [60, 70, 2]])
print(x)

x = np.sort(x)
print(x)


empty = np.empty([3,2])
print(empty)

empty_1 = np.empty((2,2), dtype=int)
print(empty_1)

full = np.full((2,2), 7)
print(full)

from timeit import default_timer as timer

size = 50000000

start = timer()
x = np.full(size, 7)
end = timer()
print('full:', end-start)

start = timer()
x = np.empty(size)
end = timer()
print('empty:', end-start)

start = timer()
x = np.zeros(size)
end = timer()
print('zeroes:', end-start)

