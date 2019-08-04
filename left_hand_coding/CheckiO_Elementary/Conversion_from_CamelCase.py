### Conversion_from_CamelCase



def conversion_from_camelcase(words):
    for word in words:
        if word.isupper():
            words = words.replace(word, '_' + word.lower())

    return words.strip('_')


words = 'IPhone'

conversion_from_camelcase(words)
conversion_from_camelcase('IIIIIIIPhone')