def divide_binary():
    s = '10, 0010, 00, 1000'
    l = s.split((','))
    for i in l:
        if int(str(i)) % 5 == 0:
            print('Output: ', i)

divide_binary()

#base powers
print(int('1111', 2))
print(int('2222', 3))
print(int('0000', 4))
print(int('0000', 5))
print(int('0000', 6))
print(int('0000', 7))
print(int('0000', 8))
print(int('0000', 9))
print(int('0000', 10))
print(int('0000', 16))
print(int('0000', 36))


x,y = (0,1)
while y < 50:
    print(y)
    x, y = y, x + y


x[1:-1, 1:-1]
