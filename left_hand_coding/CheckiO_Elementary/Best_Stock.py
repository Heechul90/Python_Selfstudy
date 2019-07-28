### Best_Stock

def best_stock(data):
    max_price = 0
    answer = ''

    for s in data:
        if data[s] > max_price:
            max_price = data[s]
            answer = s

    return answer

data = {'CAC': 10, 'ATX': 390.2, 'WIG': 1.2}

best_stock(data)
