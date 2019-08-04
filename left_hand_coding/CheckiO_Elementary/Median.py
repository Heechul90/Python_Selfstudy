### Median



def median(data):
    data.sort()
    half = len(data) // 2

    return (data[half] + data[-half - 1]) / 2


data = [1, 2, 3, 4, 5, 6]

median(data)
median([1, 2, 3, 4, 5])
median([1, 2, 3, 4, 5, 7, 8, 9, 10])