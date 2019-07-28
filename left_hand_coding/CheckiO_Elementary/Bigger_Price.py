### Bigger_Price

def bigger_price(limit, data):
    return sorted(data, key= lambda x: x['price'], reverse = True)[:limit]





limit = 2

data = [{'price': 138, 'name': 'wine'},
        {'price': 25, 'name': 'milk'},
        {'price': 10, 'name': 'bread'},
        {'price': 15, 'name': 'meat'}]
type(data)
bigger_price(limit, data)