### 05장. 파이썬 날개날기
## 연습문제


## Q1
## 다음은 Calculator 클래스이다.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력



## Q2
## 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자.
## 즉 다음과 같이 동작해야 한다.
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
cal = MaxLimitCalculator()
cal.add(50)                # 50 더하기
cal.add(60)                # 60 더하기

print(cal.value)           # 100 출력



## Q3
## 다음 결과를 예측해 보자.
## 하나.

print(all([1, 2, abs(-3)-3]))

# abs(-3)은 -3의 절댓값이므로 3이 되어 all([1, 2, 0])이 되고, 
# 리스트의 요솟값중 0이 있기 때문에 all 내장 함수의 결과는 False가 된다.

## 둘.

print(chr(ord('a')) == 'a')
# ord('a') 의 결과는 97이 되어 chr(97)로 치환된다. 
# chr(97)의 결과는 다시 'a'가 되므로 'a' == 'a'가 되어 True를 돌려준다.



## Q4
## filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
print(list(filter(lambda x:x > 0, [1, -2, 3, -5, 8, -3])))



## Q5
## '0xea' 라는 16진수 문자열을 10진수로 변경해 보자.
print(int('0xea', 16))



## Q6
## map과 lambda를 사용하여 
## [1, 2, 3, 4] 라는 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.
print(list(map(lambda x : x * 3, [1, 2, 3, 4])))



## Q7
## 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
## [-8, 2, 7, 5, -3, 5, 0, 1]
a = [-8, 2, 7, 5, -3, 5, 0, 1]
b = max(a)
c = min(a)
print(b + c)



## Q8
## 5.666666666666667을 소수점 4자리까지만 반올림하여 표시해 보자.
a = 17 / 3
print(round(a, 4))



## Q9
## 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트를 작성해 보자.
# myargv.py
# import sys

# numbers = sys.argv[1:]     # 파일 이름을 제외한 명령 행의 모든 입력

# result = 0
# for number in numbers:
#     result = result + int(number)
# print(result)



## Q10
## os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
import os
os.chdir('D:\Heechul\Python_study\jump_to_python')
result = os.popen('dir')
print(result.read())



## Q11
## glob 모듈을 사용하여 D:\Heechul\Python_study\jump_to_python 디렉터리의 파일 중 
## 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.
import glob
result = glob.glob('D:\Heechul\Python_study\jump_to_python\*.py')
print(result)



## Q12
## time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
## 2018/04/03 17:20:32
import time
a = time.strftime("%Y/%m/%d %H:%M:%S")
print(a)


## Q13
## random 모듈을 사용하여 
## 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(단 중복된 숫자가 있으면 안 됨).
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)     # 1부터 45까지의 난수 발생
    if num not in result:
        result.append(num)

print(result)