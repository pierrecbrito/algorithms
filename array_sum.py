
def sum_items(array):
    if len(array) == 1:
        return array[0]
    elif len(array) == 0:
        return 0
    else:
        return array.pop(0) + sum_items(array)


print(sum_items([]))