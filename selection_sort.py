
def search_minor(list):
    #print(list) - O(n)
    minor = list[0]
    minor_index = 0

    for i in range(1, len(list)):
        if list[i] < minor:
            minor = list[i]
            minor_index = i
    
    return minor_index

def order_minor_to_major(list):
    new_list = []

    for i in range(len(list)):
        minor_index = search_minor(list)
        new_list.append(list.pop(minor_index))

    return new_list


print(order_minor_to_major([5, 3, 6, 8, 1]))