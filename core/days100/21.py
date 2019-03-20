

def max_of_two(x, y):
    if x > y:
        return x
    return y

def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))

print(max_of_three(3, 6, -5))

def sum_it(numbers):
    start = 0
    for num in numbers:
        start += num
    return start

print(sum_it((4,12,45,7,3,6,65,546,657,758,45.23,7,65,56,8)))

def multiply_it(numbers):
    start = 1
    for num in numbers:
        start *= num
    return start


print(multiply_it((87,987,87,7,5,5.23,8498,7.12345,3,12)))

def back_it_up(string):
    x = ""
    count = len(string)
    while count > 0:
        x += string[count - 1]
        count -= 1
    return x

print(back_it_up('love it'))