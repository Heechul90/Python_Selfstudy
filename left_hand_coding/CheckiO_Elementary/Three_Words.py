### Three_Words

def three_word(words):
    count = 0

    for word in words.split():
        if word.isalpha():
            count += 1

        else:
            count = 0

        if count >= 3:
            return True

    return False

three_word('Hello world hello')
three_word('one two 3 four')
three_word('123 123 123 123')
three_word('Hello 1 hello ho sosl')