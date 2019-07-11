### Operator


## 할당 연산자 Assign
my_int = 1

## 복합 할당 연산자
count = 0
print(count)

count = 1
print(count)

count = count + 1 # : count += 1

print(count)

count = count - 1 # : count -= 1


## 산술 연산자 Arithmetic
print(3+3)
print(6-3)
print(3*3)
print(13/3)


## 특수 연산자 (**. //, %)
# ** 제곱
# // 몫
# % 나머지

print(3**4)
print(7 / 3)
print(7 // 3)
print(7 % 3)

## 홀수 구하기
numbers = [1,2,3,4,5,6,6,7,8,9,10]

for number in numbers:
    if number % 2 == 1:
        print("홀수")
    else:
        print("짝수")
    

