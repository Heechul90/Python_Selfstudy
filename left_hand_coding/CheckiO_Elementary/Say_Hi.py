### Say_HI

def say_hi(name, age):
    print('Hi, My name is', name, 'and I\'m', age, 'years old')


say_hi('heechul', 30)



###

def say_hi2(name: str, age: int) -> str:
    return "Hi. My name is {0} and I'm {1} years old".format(name, age)

say_hi2('heechul', 30)