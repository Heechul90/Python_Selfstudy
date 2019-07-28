### First_Word

def first_word(text):
    # 쉼표와 점을 공백으로 바꾸고, strip()으로 처음과 끝의 공백을 없애준다
    text = text.replace('.', '').replace(',', '').strip()
    text = text.split()

    return text[0]

first_word('Hello world')
first_word('a world')
first_word('don\'t touch me')
first_word('hello. world')
