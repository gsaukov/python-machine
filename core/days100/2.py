def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num-1)

print('Enter int:')

num = int(input())
print(factorial(num))