
def fib():
    a, b = 0,1
    while True:
        yield a
        a, b = b, a+b

for index, fibonacci_number in zip(range(10), fib()):
    print('{i:3}:{f:3}'.format(i=index, f=fibonacci_number))


def fib2():
    x,y = (0,1)
    while y < 50:
        print(y)
        x, y = y, x + y
