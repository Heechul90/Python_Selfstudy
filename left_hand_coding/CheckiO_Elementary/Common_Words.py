### Common_Words



def common_words(text1, text2):
    text1_set, text2_set = set(text1.split(',')), set(text2.split(','))

    common = text1_set.intersection(text2_set)

    return ','.join(sorted(common))


text1 = 'hello,world'
text2 = 'hello,earth'

common_words(text1, text2)