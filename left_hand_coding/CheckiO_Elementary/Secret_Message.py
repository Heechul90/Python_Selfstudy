### Secret_Message

def secret_message(text):
    return ''.join(filter(str.isupper, text))



secret_message('How are you? Eh, ok. Low or Lower? Ohhh.')