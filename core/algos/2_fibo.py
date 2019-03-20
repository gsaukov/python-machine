
def count(num, old):
    if num == 0:
        return 1, 0
    res = num + old
    old = num
    return res, old

def fibo(end):
    num = 0
    old = 0
    res_list = []
    for i in range (0, end):
        num, old = count(num, old)
        res_list.append([old, num])
    return res_list


print('Enter int:')

end = int(input())
print(fibo(end))