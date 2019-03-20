row_num = int(input('how many rows:'))
col_num = int(input('how many columns:'))

list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        list[row][col] = row*col


print(str(list).replace('], [',']\n['), '\n')

lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break

for l in lines:
    print(l)

def dividable_binary():
    s = input('Enter the binaries i.e. 0101, 0001, 0100 : ')
    l = s.split(',')
    for i in l:
        if int(str(i), 2) % 5 == 0:
            print('Output: ', i, int(str(i), 2))

dividable_binary()



