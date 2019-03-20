
def most_frequent(list):
    count = {}
    max_count = 0
    max_item = 0

    for i in list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if count[i] > max_count:
            max_count = count[i]
            max_item = i

    return max_item

print(most_frequent([1,1,2,2,2,3,3,4,4,4,1]))
