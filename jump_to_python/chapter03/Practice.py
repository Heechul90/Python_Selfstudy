### 03장. 프로그램의 구조를 쌓는다! 제어문
## 연습문제


## Q1
## 다음 코드의 결괏값은 무엇일까?
a = "Life is too short, you need python"

if 'wife' in a: print('wife')
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a: print('shirt')
elif "need" in a: print("need")
else: print('none')



## Q2
## while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
result = 0
num = 1
while num <= 1000:
    if num % 3 == 0:
        result = result + num
    num = num + 1
print(result)



## Q3
## while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
star = 1
while star <= 5:
    print('*' * star)
    star = star + 1

i = 0
while True: 
    i += 1             # while문 수행 시 1씩 증가
    if i > 5: break    # i 값이 5이상이면 while문을 벗어난다.
    print ('*' * i)    # i 값 개수만큼 *를 출력한다.


## Q4
## for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
number = []
for num in range(1, 101):
    number.append(num)
print(number)



## Q5
## A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
## [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
## for문을 사용하여 A 학급의 평균 점수를 구해 보자.
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for mean in range(len(a)):
    result = result + a[mean]
print(result/len(a))


## Q6
## 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
numbers = [1, 2, 3, 4, 5]
result = []
for num in numbers:
    if num % 2 == 1:
        result.append(num * 2) 
print(result)