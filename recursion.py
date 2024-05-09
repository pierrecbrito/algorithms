
def sum_items(array):
    if len(array) == 0:
        return 0
    else:
        return array.pop(0) + sum_items(array)


def len_items(array):
    if len(array) == 0:
        return 0
    else:
        array.pop()
        return 1 + len_items(array)

def get_higher_item(array, index_current = 0, higher_item = None):
    if higher_item == None:
        higher_item = array[0]

    if index_current == len(array):
        return higher_item
    else:
        if array[index_current] > higher_item:
            higher_item = array[index_current]
        return get_higher_item(array, index_current + 1, higher_item)


print(get_higher_item([10,50,32,56,105,30]))