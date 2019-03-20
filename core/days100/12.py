s = input('give me a string')
l, d = 0,0

for c in s:
    if c.isalpha():
        l=l+1
    elif c.isdigit():
        d=d+1
    else:
        pass

print('Letters', l)
print('Digits', d)

import re

p = input('enter password: ')
x = True

while x:
    if(len(p) < 6 or len(p) > 16):
        break
    elif not re.search('[a-z]', p):
        break
    elif not re.search('[0-9]', p):
        break
    elif not re.search('[A-Z]', p):
        break
    elif not re.search('[$#@]', p):
        break
    elif re.search('\s', p):
        break
    else:
        print('password check is a green light')
        x = False
        break

if x:
    print("that is a BS password - you are banned for life")

even_digits = []

for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        even_digits.append(s)

print(' $ '.join(even_digits))

letter_A = ''
for row in range(0,7):
    for column in range (0,7):
        if(((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            letter_A = letter_A + "*"
        else:
            letter_A = letter_A + ' '
    letter_A = letter_A + '\n'
print(letter_A)