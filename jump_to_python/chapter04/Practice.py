### 04장. 프로그램의 입력과 출력은 어떻게 해야 할까?
## 연습문제


## Q1
## 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(number):
    if number % 2 == 1:     # 2로 나우었을 때 나머지가 1이면 홀수이다.
        return True
    else:
        return False

print(is_odd(3))
print(is_odd(4))



## Q2
## 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
def avg_numbers(*args):    # 입력 개수에 상관없이 사용하기 위해 *args를 사용
    result = 0
    for i in args:
        result = result + i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4))



## Q3
## 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 
## 이 프로그램의 오류를 수정해 보자.
# input1 = input("첫 번째 숫자를 입력하세요:")
#input2 = input("두 번째 숫자를 입력하세요:")

# total = int(input1) + int(input2)      # 입력은 항상 문자열이므로 숫자로 바꾸어 주어야 한다.
# print("두수의 합은 %s 입니다" % total)


## Q4
## 다음 중 출력 결과가 다른 것 한 개를 고르시오.
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")   # 콤마가 있는 경우 공백이 삽입되어 더해진다.
print("".join(["you", "need", "python"]))



## Q5
## 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 
## 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.
f1 = open('test.txt', 'w')
f1.write('Life is too short!')
f1.colse       # 열린 객체를 닫는다.

f2 = open('test.txt', 'r')
print(f2.read())
f2.close()

with open("test.txt", 'w') as f1:
    f1.write("Life is too short! ")
with open("test.txt", 'r') as f2:
    print(f2.read())



## Q6
## 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
user_input = input('저장할 내용을 입력하세요:')
f = open('test.txt', 'a')  # 내용을 추가하기 위해서 'a'를 사용
f.write(user_input)
f.write('\n')              # 입력된 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.close()



## Q7
## 다음과 같은 내용을 지닌 파일 test.txt가 있다.
## 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()