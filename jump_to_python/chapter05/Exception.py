### 05장. 파이썬 날개날기
## 05-4. 예외처리


## 오류는 어떤 때 발생하는가?

# 디렉터리 안에 없는 파일 열려고 시도했을 때
# f = open("나없는파일", 'r')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'

# 0으로 다른 숫자를 나누는 경우
# 4 / 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

# 찾는 값이 없을 때
# a = [1,2,3]
# a[4]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range


## 오류 예외 처리 기법
# try, except문
# try, except문의 기본 구조
# try:
#     ...
# except [발생 오류[as 오류 메시지 변수]]:
#     ...


# except [발생 오류 [as 오류 메시지 변수]]:

# 1) try, except만 쓰는 방법
# try:
#     ...
# except:
#     ...

# 2) 발생 오류만 포함한 except문
# try:
#     ...
# except 발생 오류:
#     ...

# 3) 발생 오류와 오류 메시지 변수까지 포함한 except문    
# try:
#     ...
# except 발생 오류 as 오류 메시지 변수:
#     ...

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)


## try .. finally
f = open('D:/Heechul/Python_study/jump_to_python/foo.txt', 'w')
# try:
#                 # 무언가를 수행한다.
# finally:
#     f.close()


## 여러개의 오류처리하기
# try:
#     ...
# except 발생 오류1:
#    ... 
# except 발생 오류2:
#    ...
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)


## 오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass


## 오류 일부러 발생시키기
# class Bird:
#     def fly(self):
#         raise NotImplementedError

# class Eagle(Bird):
#     pass

# eagle = Eagle()
# eagle.fly()
# 상속받는 클래스에서 함수를 재구현하는 것을 메서드 오버라이딩이라고 부른다

# class Eagle(Bird):
#     def fly(self):
#         print("very fast")

# eagle = Eagle()
# eagle.fly()


## 예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

print(say_nick("천사"))
# print(say_nick("바보"))

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")


try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
        