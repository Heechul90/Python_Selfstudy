### Index_Power

def index_power(array, n):
    if n < len(array):
        return array[n] ** n

    else:
        return -1


index_power([1, 2, 3, 4], 2)
index_power([1, 2, 3, 4], 1)
index_power([1, 2, 3, 4], 3)
index_power([1, 2, 3, 4], 6)
