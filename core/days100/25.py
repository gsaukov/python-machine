import numpy as np

def printSize(x):
    print('type:', type(x))
    print('Size: ', x.size)
    print('Size of 1 element: ', x.itemsize)
    print('total bytes: ', x.nbytes)

x = np.array([1, 2, 3], dtype=np.float64)
printSize(x)

x = np.array([1, 2, 3], dtype=np.float32)
printSize(x)

import numpy as np
array_uno = np.array([0, 10, 20, 30, 40, 50, 60])
array_dos = np.array([0, 40, 50])

print(np.in1d(array_uno, array_dos))

array_uno = np.array([0, 20, 40, 60, 80, 100])
array_dos = np.array([10, 20, 70])

print(array_uno, '\n', array_dos, '\n', np.intersect1d(array_uno, array_dos))

x = np.array([[1, 1], [2, 3], [1, 6]])
print(np.unique(x))



