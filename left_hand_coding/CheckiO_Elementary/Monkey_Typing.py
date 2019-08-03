### Monkey_Typing




def monkey_typing(text, set):
    result = 0

    for word in set:
        if word in text.lower():
            result += 1

    return result

set = {'how', 'are', 'you'}


monkey_typing('How arenkdjhfihjef you', set)
monkey_typing('How arenkdjhfihjefarejijefiyou', set)