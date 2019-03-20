condition = 1
#now the pc is asking is this true or false ... each iteration
while condition < 10:
    print(condition)
    condition += 1
    #this is read as condition = condition + 1, and this

#while true:
    #print('this can crash your pc...infinite loops')
    #if you impatiently run this script you need to stop it

#another way of while loop
print('\n')
list_1 = [5,7,4,3,2,4,8,3,3,2,5,1,7]
for eachitem in list_1:
    print(eachitem)

print('\n')
list_1 = [5,7,2,33,87,999,1]
print(sorted(list_1))

print('\n')

for x in range(4, 100):
    print(x)

print('\n')
for x in range(4, 100, 10):
    print(x)


print('\n')
for x in range(1, 10):
    if x%2 == 0:
        print('EVEN')
    else:
        print('ODD')

