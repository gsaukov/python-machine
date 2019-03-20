empty_list = []

for i in range(2000, 3200):
    if (i%7 == 0) and (i%5 != 0):
        empty_list.append(str(i))

print(' ,'.join(empty_list))