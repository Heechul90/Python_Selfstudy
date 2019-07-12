### 03장. 프로그램의 구조를 쌓는다! 제어문
## 03-1. If문


## if문은 왜 필요할까?
money = True
if money:
    print('택시를 타고 가라')
else:
    print('걸어 가라')


## if문의 기본 구조

# if 조건문:
#    수행할 문장1
#    수행할 문장2
#    ...
# else:
#    수행할 문장A
#    수행할 문장B
#    ...


## 들여쓰기
# 들여쓰기를 무조건 해야한다
# if 조건문:
#     수행할 문장1
#     수행할 문장2
#     수행할 문장3

# 들여쓰기를 안하면 에러가 난다
# if 조건문:
#     수행할 문장1
# 수행할 문장2
#     수행할 문장3

# 들여쓰기 너비도 똑같아야 한다
# if 조건문:
#     수행할 문장1
#     수행할 문장2
#         수행할 문장3

# 파이썬 커뮤니티에서는 들여쓰기를 할 때 공백(Spacebar) 4개를 사용하는 것을 권장한다


## 조건문이란 무엇인가?
x = 3
y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)

# "만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
if money >= 3000:
    print("택시를 타고 가라") 
else:
    print("걸어 가라")


## and, or, not
# x  or y	x와 y 둘중에 하나만 참이면 참이다
# x and y	x와 y 모두 참이어야 참이다
#   not x	x가 거짓이면 참이다

# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")



## x in s, x not in s
# x in 리스트	x not in 리스트
# x in 튜플	    x not in 튜플
# x in 문자열	x not in 문자열

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라."
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# [조건문에서 아무 일도 하지 않게 설정하고 싶다면?]
# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")


## 다양한 조건을 판단하는 elif
# "주머니에 돈이 있으면 택시를 타고, 
# 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 
# 돈도 없고 카드도 없으면 걸어 가라."
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타라")
elif card:
    print("택시를 타라")
else:
    print("걸어 가라")

# [if문을 한 줄로 작성하기]
if 'money' in pocket:
    pass 
else:
    print("카드를 꺼내라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")



## 조건부 표현식
score = 50
if score >= 60:
    message = "success"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"
