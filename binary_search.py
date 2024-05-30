import math

def search_in(item, array):
    lower = 0
    higher = len(array) - 1

    while(lower <= higher):
        middle = math.floor((lower + higher) / 2)
        try_this = array[middle]

        if try_this == item:
            return middle
        
        if try_this > item:
            higher = middle - 1
        else:
            lower = middle + 1
    
    return None

list = list(range(1, 100000, 1))

print(search_in(10000, list)) #Return Position
