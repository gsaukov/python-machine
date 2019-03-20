for i in range(1500, 1550):
    if i%7 == 0 and i%5 == 0:
        print(i)

import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('guess a number'))
print('game over')

count = 0

for num in range(7):
    count += 1
    print('*' * count)

for num in range(6):
    count -= 1
    print('*' * count)