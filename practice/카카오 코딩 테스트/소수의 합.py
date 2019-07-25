### 소수의 합

## 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수,
# solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

## 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

## 입출력 예
# n	    result
# 10	4
# 5	    3



### 에라토스테네스의 체를 이용한 예
def solution(number):
    num = set(range(2, number + 1))

    for i in range(2, number + 1):
        if i in num:
            num -= set(range(2*i, number+1, i))

    return len(num)

solution(10)

number= 10
set(range(2, number + 1))




### 소수 인지 판별
def solution(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False

    return True


num = input('정수를 입력하세요.: ')


if solution(int(num)):
    print(num, '은 소수입니다')
else:
    print(num, '은 소수가 아닙니다')

