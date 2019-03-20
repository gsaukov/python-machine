
def largest(array):
    if len(array) < 2:
        return print('Too small')

    previous_num = current_sum = array[0]
    max_sum = array[0] + array[1]

    for num in array[1:]:
        current_sum = max(current_sum + num,  previous_num + num)
        max_sum = max(current_sum, max_sum)
        previous_num = num

    return max_sum

print(largest([7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19]))
print(largest([-6, -19, -5, -3]))
print(largest([-6, -19, 2, -3]))