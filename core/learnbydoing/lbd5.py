import random
print('i will flip a coin 1000 time. Guess how many times it will come upheads.')
input()

turns = 10000000

flips = 0
heads = 0


while flips < turns:
    if random .randint(0, 1) == 1:
        heads += 1
    flips += 1
    if flips == 9000000:
        print('900000 flips and there have been ' + str(heads) + ' heads.')
    if flips == 1000000:
        print('At 100000 tosses, heads has come up ' + str(heads) + ' times so far.')
    if flips == 5000000:
        print('Halfway done, and heads has come up ' + str(heads) + ' times.')

print()
print('Out of 1000 coin tosses: ')
print('\t', 'Heads came up: ', heads)
tails = (turns - int(heads))
print('\t', 'Tails came up: ', tails, '\n')
print('Where you close? ')
