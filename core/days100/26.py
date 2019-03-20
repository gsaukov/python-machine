import numpy as np



L = [1,2,3]
A = np.array([1,2,3])
print(L)
print(A)

L.append(4)
# A.append(4)

L = L + [5]
# A = A + [4, 5]

L2 = []
for e in L:
    L2.append(e+e)

print(L2)


A2 = A+A
A3 = 2*A
print(A2)
print(A3)

L = 2*L
print(L)

L3 = []
for e in L:
    L3.append(e*e)
print(L3)

L4 = []
for e in L:
    L4.append(e**3)
print(L4)


A4 = A**2
print(A4)

A5 = np.sqrt(A)
print(A5)

A6 = np.log(A)
print(A6)

A7 = np.exp(A)
print(A7)


