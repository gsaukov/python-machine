print('give me some integers... type 0 to exit')

count = 0
sum = 0.0
number = 1

while number != 0:
    number = int(input(''))
    sum = sum + number
    count += 1

if count == 0:
    print('give me some numbers')
else:
    print('sum and average of the above number are:', sum, sum/(count-1))

chosen = int(input('give me the chosen number: '))
for i in range(13):
    print(chosen, 'x', i, '=', chosen*i)

for i in range(10):
    print(str(i) * i)