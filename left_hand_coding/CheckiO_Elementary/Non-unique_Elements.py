### Non-unique_Elements

def non_unique_elements(data):
    result = []

    for i in data:
        if data.count(i) > 1:
            result.append(i)
    return result


data = [12, 12, 10]
non_unique_elements(data)
non_unique_elements([1, 1, 1, 2, 2, 2, 3, 4, 5])


