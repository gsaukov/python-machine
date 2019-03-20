

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]


print(finder([1,2,3,4,5,6,7], [3,2,1,4,6,]))


import collections

def finder2(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

print(finder2([1,2,3,4,5,6,7,7,7], [3,2,1,4,6,5,7,7]))

def finder3(arr1, arr2):
    x = set(arr2) - set(arr1)
    print(x)

print(finder3([1,2,3,4,5,6,7,7,7], [3,2,1,4,6,5,7,7,8]))



