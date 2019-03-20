from random import randint

print('Привет братишка!')
print('Реши примерчик!')


a = randint(0, 10)
b = randint(0, 10)
res = a*b
print('Сколько будет: ', a, '*', b, '= ?'  )
inp = input()

if res == int(inp):
    print('Четкий пацан вообще!')
else:
    print('Нука давай еще!')















































for i in range(3):
    a = randint(0, 10)
    b = randint(0, 10)
    res = a*b
    print('Сколько будет: ', a, '*', b, '= ?'  )
    inp = input()

    if a*b == int(inp):
        print('Четкий пацан вообще!')
        break
    else:
        print('Нука давай еще!')

    inp = input()
    if a*b == int(inp):
        print('Норм пацан!')
        break
    else:
        print('Чo тупой?')

    inp = input()
    if a*b == int(inp):
        print('Пойдет!')
        break
    else:
        print('тупой')