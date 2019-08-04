### Conversion_into_CamelCase



def conversion_into_camelcase(words):
    words = words.title().replace('_', '')

    return words

words = 'This_are_man'


conversion_into_camelcase(words)
conversion_into_camelcase('i_phone')