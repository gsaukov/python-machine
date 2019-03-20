
def arr_rotation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    head = []
    tail = []

    move = 0
    for n in arr1:
        if n == arr2[move]:
            tail.append(n)
            move += 1
        else:
            head.append(n)

    tail.extend(head)
    return tail == arr2

print(arr_rotation([1, 2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 1, 2]))
print(arr_rotation([1, 2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 1, 8]))
print(arr_rotation([5, 6, 7, 1, 2, 3, 4], [3, 4, 5, 6, 7, 1, 2]))
print(arr_rotation([7, 1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 1, 2]))
print(arr_rotation([7, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7]))
print(arr_rotation([2, 3, 4, 5, 6, 7, 1], [1, 2, 3, 4, 5, 6, 7]))

def rotation(list1, list2):
    if len(list1) != len(list2):
        return 'Arrays are not even'

    key = list1[0]
    key_index = 0

    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i
            break

    if key_index == 0:
        return False

    for x in range(len(list1)):
        l2index = (key_index + x) % len(list1)

        if list1[x] != list2[l2index]:
            return False

    return True

print('----------------------------------------')
print(rotation([1,2,3,4,5,6,7], [3,4,5,6,7,1,2]))
print(rotation([1,2,3,4,5,6,7], [3,4,5,6,7,1,8]))
print(rotation([5,6,7,1,2,3,4], [3,4,5,6,7,1,2]))
print(rotation([7,1,2,3,4,5,6], [3,4,5,6,7,1,2]))
print(rotation([7,1,2,3,4,5,6], [1,2,3,4,5,6,7]))
print(rotation([2,3,4,5,6,7,1], [1,2,3,4,5,6,7]))
