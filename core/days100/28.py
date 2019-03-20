def sum1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x
    return final_sum

print(sum1(5))

def sum2(n):
    return (n*(n+1))/2

print(sum1(17))


def Bigo(n):
    return 45*n**3 + 20*n**2 + 19

print(Bigo(168))


from math import log
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')

n = np.linspace(1, 10)
labels = ['Constant', 'Logartihmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n*np.log(n), n**2, n**3, 2**n]

plt.figure(figsize=(12, 10))
plt.ylim(0, 50)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])

plt.legend(loc = 0)
plt.ylabel('Relative runtimes')
plt.xlabel('n')

plt.show()