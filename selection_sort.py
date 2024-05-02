
def order_minor_to_major(list):
    minor = list[0]
    minor_index = 0

    for i in range(1, len(list)):
        if list[i] < minor:
            minor = list[i]
            minor_index = i
    
    return minor_index

print(order_minor_to_major([5, 3, 6, 8, 1]))