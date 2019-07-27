### Correct_Sentence

def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text = text + '.'

    return text


correct_sentence('greetings, friends')
correct_sentence('Greetings, friends')
correct_sentence('Greetings, friends.')
