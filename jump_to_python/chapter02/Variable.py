### 02장. 파이썬 프로그래밍의 기초, 자료형
## 02-8. 자료형의 값을 저장하는 공간, 변수


## 변수는 어떻게 만들까?
a = 1
b = "python"
c = [1,2,3]
# 변수 이름 = 변수에 저장할 값


## 변수란?
a = [1, 2, 3]
print(id(a))


## 리스트를 복사하고자 할 때
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)

a[1] = 4
print(a)
print(b)

# b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소 만들기
# 1) [:]
a = [1, 2, 3]
b = a[:]
print(id(a))
print(id(b))
a[1] = 4
print(a)
print(b)

# 2) copy 모듈 이용
from copy import copy
b = copy(a)    #  b = copy(a)는 b = a[:]과 동일
print(b is a)


## 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
print(a, b)
(a, b) = 'python', 'life'
print((a, b))
[a, b] = ['python', 'life']
print([a, b])
a = b = 'python'
print(a)
print(b)

a = 3
b = 5
a, b = b, a
print(a)
print(b)