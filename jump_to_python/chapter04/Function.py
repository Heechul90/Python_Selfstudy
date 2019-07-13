### 04장. 프로그램의 입력과 출력은 어떻게 해야 할까?
## 04-1. 함수


## 함수란 무엇인가?

## 함수를 사용하는 이유는 무엇일까?

## 파이썬 함수의 구조
# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>
#     ...

# "이 함수의 이름(함수 이름)은 add이고
#  입력으로 2개의 값을 받으며
#  결괏값은 2개의 입력값을 더한 값이다."
def add(a, b):
    return a + b
a = 3
b = 4
c = add(a, b)
print(c)


## 매개변수와 인수
def add(a, b):       # a, b 는 매개변수
    return a + b

print(add(3, 4))     # 3, 4는 인수


## 입력값과 결괏값에 따른 함수의 형태
# 입력값 ---> 함수 ----> 결괏값
# 1) 일반적인 함수
# def 함수이름(매개변수):
#     <수행할 문장>
#     ...
#     return 결과값

def add(a, b):
    result = a + b
    return result

print(add(3, 5))
# 결괏값을 받을 변수 = 함수이름(입력인수1, 입력인수2, ...)


# 2) 입력값이 없는 함수
def say(): 
    return 'Hi'
a = say()
print(a)
# 결괏값을 받을 변수 = 함수이름()

# 3) 결괏값이 없는 함수
def add(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
print(add(3, 4))
# 함수이름(입력인수1, 입력인수2, ...)


# 4) 입력값도 결괏값도 없는 함수
def say():
    print('Hi')
print(say())


## 매개변수 지정하여 호출하기
def add(a, b):
    return a + b

result = add(a= 3, b= 7)
print(result)

result = add(b= 7, a= 3)
print(result)


## 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
# def 함수이름(*매개변수): 
#     <수행할 문장>
#     ...

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4,5,6))
print(add_many(1,2,3,4,5,6,8,9))


def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul('add', 1,2,3,4,5,6,7,8,9,10))
print(add_mul('mul', 1,2,3,4,5,6,7,8,9,10))

# 키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a = 1)
print_kwargs(name='foo', age=3)


## 함수의 결괏값은 언제나 하나이다
def add_and_mul(a, b):
    return a + b, a * b

print(add_and_mul(3, 4))


# 결과값을 받으면 함수를 빠져 나간다
def add_and_mul(a, b):
    return a + b
    return a * b

print(add_and_mul(3, 4))

# return을 단독으로 써서 함수 빠져 나가기
def say_nick(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s 입니다' % nick)
print(say_nick('바보'))


## 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man = True):
    print('나의 이름은 %s 입니다' % name)
    print('나의 나이는 %d 입니다' % old)
    if man:
        print('남자입니다')
    else:
        print('여자입니다')

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용", 27, False)

# 매개변수는 항상 맨 마지막에 둔다
# def say_myself(name, man=True, old): 
#     print("나의 이름은 %s 입니다." % name) 
#     print("나이는 %d살입니다." % old) 
#     if man: 
#         print("남자입니다.") 
#     else: 
#         print("여자입니다.")


## 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1
print(vartest(a))
print(a)


def vartest(hello):
    hello = hello + 1

def vartest(a):
    a = a + 1

print(vartest(3))
print(a)


## 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1) return 사용하기
a = 1 
def vartest(a): 
    a = a +1 
    return a
print(vartest(a))

# 2) global 명령어 사용하기(사용안하는게 좋다)
a = 1
def vartest():
    global a
    a = a + 1
print(vartest())
print(a)


## lambda
# lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
add = lambda a, b: a+b
result = add(3, 4)
print(result)

def add(a, b):
    return a + b
result = add(3, 4)
print(result)

# lamda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다