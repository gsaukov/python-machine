x = 5
y = 8

if x > y:
    print ('x is greater than y')

if x < y:
    print ('x is LESS than y\n')

while x < y:
    print('x is LESS than y')
    x = x + 1

print ('\n')
x = 5
y = 8
z = 3

if z < x < y:
    print ('now we are comparing 3 variables\n')

if x > y | x < 20:
    print ('x is greater than y')
elif x < 100:
    print ('x is not greater than 100')
else:
    print('x is not greater')
