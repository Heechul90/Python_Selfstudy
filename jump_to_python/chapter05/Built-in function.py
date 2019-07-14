### 05장. 파이썬 날개날기
## 05-5. 내장함수


## abs
## abs(x)는 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수이다
print(abs(3))
print(abs(-3))
print(abs(-1.2))


## all
## all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며
## 이 x가 모두 참이면 True,
## 거짓이 하나라도 있으면 False를 돌려준다.
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))     # 0은 False이다


## any
## any(x)는 x 중 하나라도 참이 있으면 True를 돌려주고,
## x가 모두 거짓일 때에만 False를 돌려준다.
## all(x)의 반대이다.
print(any([1, 2, 3, 0]))
print(any([0, ""]))


## chr
## chr(i)는 아스키(ASCII) 코드 값을 입력받아
## 그 코드에 해당하는 문자를 출력하는 함수이다.
# 아스키 코드란 0에서 127 사이의 숫자를 각각 하나의 문자 또는 기호에 대응시켜 놓은 것이다
print(chr(97))
print(chr(48))


## dir
## dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다. 
## 다음 예는 리스트와 딕셔너리 객체 관련 함수(메서드)를 보여 주는 예이다. 
## 우리가 02장에서 살펴본 자료형 관련 함수를 만나 볼 수 있다.
print(dir([1, 2, 3]))
print(dir({'1':'a'}))


## divmod
## divmod(a, b)는 2개의 숫자를 입력으로 받는다.
## 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
print(divmod(7, 3))
print(7 // 3)
print(7 % 3)


## enumerate
## enumerate는 "열거하다"라는 뜻이다. 
## 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 
## 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)


## eval
## eval(expression )은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 
## 문자열을 실행한 결괏값을 돌려주는 함수이다.
print(eval('1 + 2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))


## filter
## filter 함수는 첫 번째 인수로 함수 이름을, 
## 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 
## 그리고 두 번째 인수인 반복 가능한 자료형 요소가 
## 첫 번째 인수인 함수에 입력되었을 때 
## 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.
# positive.py
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result
print(positive([1,-3,2,0,-5,6]))

# filter함수 이용
# filter1.py
def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# lambda 함수 이용
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))


## hex
## hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.
print(hex(234))
print(hex(3))


## id
## id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
print(id(4))


## input
## input([prompt])은 사용자 입력을 받는 함수이다. 
## 매개변수로 문자열을 주면 다음 세 번째 예에서 볼 수 있듯이 
## 그 문자열은 프롬프트가 된다.
# [ ] 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법임을 기억하자.
# >>> a = input()
# hi
# >>> a
# 'hi'
# >>> b = input("Enter: ")
# Enter: hi
# >>> b
# 'hi'


## int
## int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 
## 정수를 입력으로 받으면 그대로 돌려준다.
print(int('3'))
print(int(4.3))

# int(x, radix)         # radix는 진수(기본으로 10진수)
print(int('11', 2))     # 2진수로 표현
print(int('1A', 16))    # 16진수로 표현


## isinstance
## isinstance(object, class )는 첫 번째 인수로 인스턴스, 
## 두 번째 인수로 클래스 이름을 받는다. 
## 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 
## 거짓이면 False를 돌려준다.
class Person: pass
a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b, Person))


## len
## len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
print(len('python'))
print(len([1, 2, 3]))
print(len((1, 'a')))



## list
## list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
print(list('python'))
print(list((1, 2, 3)))

a = [1, 2, 3]
b = list(a)
print(b)


## map
## map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
## map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
# two_times.py

def two_times(x):
    return x * 2

print(list(map(two_times, [1, 2, 3, 4])))

# lamda 함수 이용
print(list(map(lambda a: a * 2, [1, 2, 3, 4])))


## max
## max(iterable)는 인수로 반복 가능한 자료형을 입력받아
## 그 최댓값을 돌려주는 함수이다.
print(max([1, 2, 3]))
print(max('python'))


## min
## min(iterable)은 max 함수와 반대로, 
## 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수이다.
print(min([1, 2, 3]))
print(min('python'))


## oct
## oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
print(oct(34))
print(oct(12345))



## open
## open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 
## 파일 객체를 돌려주는 함수이다. 
## 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
# w	쓰기 모드로 파일 열기
# r	읽기 모드로 파일 열기
# a	추가 모드로 파일 열기
# b	바이너리 모드로 파일 열기

# rb는 "바이너리 읽기 모드"
# f = open("binary_file", "rb")

# r과 생략은 읽기 모드
# fread = open("read_mode.txt", 'r')
# fread2 = open("read_mode.txt")

# a는 추가 모드
# fappend = open("append_mode.txt", 'a')



## ord
## ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.
print(ord('a'))
print(ord('0'))


## pow
## pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수이다.
print(pow(2, 4))
print(pow(3, 3))


## range
## range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수이다. 
## 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.
# 1) 인수가 하나일 경우
print(list(range(5)))

# 2) 인수가 2개일 경우
print(list(range(5, 10)))

# 3) 인수가 3개일 경우
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))


## round
## round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
# [, ndigits]는 ndigits가 있을 수도 있고 없을 수도 있다는 의미이다.
print(round(4.6))
print(round(4.2))

print(round(5.2154, 2))


## sorted
## sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted('zero'))
print(sorted((3, 2, 1)))


## str
## str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.
print(str(3))
print(str('hi'))
print(str('hi'.upper()))


## sum
## sum(iterable) 은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.
print(sum([1, 2, 3]))
print(sum((1, 2, 3)))


## tuple
## tuple(iterable)은 반복 가능한 자료형을 입력받아 
## 튜플 형태로 바꾸어 돌려주는 함수이다. 
## 만약 튜플이 입력으로 들어오면 그대로 돌려준다.
print(tuple('abc'))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))



## type
## type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.
print(type('abc'))
print(type([]))
print(type(open('test', 'w')))


## zip
## zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
# 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))
