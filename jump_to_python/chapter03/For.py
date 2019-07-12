### 03장. 프로그램의 구조를 쌓는다! 제어문
## 03-3. For문


## for문의 기본 구조
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     ...

## 예제를 통해 for문 이해라기
# 1) 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 2) 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

# 3) for문의 응용
# "총 5명의 학생이 시험을 보았는데 
# 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 
# 합격인지 불합격인지 결과를 보여 주시오."
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print('%d번 학생은 합격입니다.' % number)
    else:
        print('%d번 학생은 불합격입니다.' % number)


## for문과 continue
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    else:
        print("%d번 학생 축하합니다. 합격입니다" % number)


## for문과 함께 자주 사용하는 range 함수
a = range(10)
print(a)
a = range(1, 11)
print(a)

# range 함수의 예시 살펴보기
sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


## for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'x', j, '=', i * j)


## 리스트 내포 사용하기
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
    print(result)

a = [1, 2, 3, 4]
result = []
for num in a:
    if num % 2 == 0:
        result.append(num * 3)
        print(result)

# 위와 같다
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2,10)               
              for y in range(1,10)]
print(result)