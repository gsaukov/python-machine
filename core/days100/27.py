# DOT PRODUCT
import numpy as np
from datetime import datetime as dt

a = np.array([1,3])
b = np.array([2,4])

x1 = np.dot(a, b)
print(x1)


a = np.random.randn(100)
b = np.random.randn(100)
print(a)
print(b)
T = 100000

def slow_dot_product(a, b):
    result = 0
    for e, f in zip(a, b):
        result += e*f
    return result


t0 = dt.now()
for t in range(T):
     rs = slow_dot_product(a, b)
dt1 = dt.now() - t0
print(rs)

t0 = dt.now()
for t in range(T):
    a.dot(b)
dt2 = dt.now() - t0

print('dt1/dt2 total seconds', dt1.total_seconds(), dt2.total_seconds())
