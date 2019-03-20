from array import *

array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)

print('Access first three items individuals')
print(array_num[0])
print(array_num[1])
print(array_num[2])


print('starting array', array_num)
array_num.append(11)
print('new array', array_num)

print(array_num[::-1])


print(array_num)
array_num.insert(2,4)
print(array_num)

array_num.pop(3)
print(array_num)

new_array = array('i', [1,3,5,7,3,9,3,11])
print(new_array)

new_array.remove(3)

print(new_array)

print(type(new_array))
x = new_array.tolist()

print(type(x))