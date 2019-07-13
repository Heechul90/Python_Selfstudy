### 04장. 프로그램의 입력과 출력은 어떻게 해야 할까?
## 04-2. 사용자 입력과 출력


## 사용자 입력
# 1) input의 사용
# a = input()

# 2) 프롬프트를 띄워서 사용자 입력 받기
# input("질문 내용")
# number = input("숫자를 입력하세요: ")

# number = input("숫자를 입력하세요: ")
# 숫자를 입력하세요: 3
# print(number)
# 3


## print 자세히 알기
a = 123
print(a)

a = "Python"
print(a)

a = [1, 2, 3]
print(a)

# 1) 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short")
print("life"+"is"+"too short") 

# 2） 문자열 띄어쓰기는 콤마로 한다
print("life", "is", "too short")

# 3） 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end= '')

