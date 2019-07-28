### Even_The_Last

def even_the_last(array):
    if not array:
        return 0

    return sum(array[::2]) * array[-1]


even_the_last([0, 1, 2, 3, 4, 5])
even_the_last([1, 3, 5])
even_the_last([6])
even_the_last([])

