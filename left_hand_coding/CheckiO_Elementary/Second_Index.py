### Second_Index

def second_index(text, symbol):
    if text.count(symbol) < 2:
        return None

    first = text.find(symbol)

    return text.find(symbol, first + 1)

second_index('sims', 's')
second_index('find the river', 'e')
second_index('hi', 'i')
second_index('hi mayor', ' ')
second_index('I', 'z')
