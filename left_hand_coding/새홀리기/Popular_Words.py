### Popular_Words

def popular_words(text, words):
    text = text.lower()
    splitted_word = text.split()
    answer = {}

    for word in words:
        answer[word] = splitted_word.count(word)

    return answer

popular_words(""" 
When I was One
I had just begun
When I was Two
I was nearly new
""", ['i', 'was', 'three', 'near'])