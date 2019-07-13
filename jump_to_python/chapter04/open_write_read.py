### 04장. 프로그램의 입력과 출력은 어떻게 해야 할까?
## 04-3. 파일 읽고 쓰기


## 파일 생성하기
f = open("new_file.txt", "w")
f.close()

# 파일 객체 = open(파일 이름, 파일 열기 모드)
# r	읽기모드 - 파일을 읽기만 할 때 사용
# w	쓰기모드 - 파일에 내용을 쓸 때 사용
# a	추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

f = open('D:/Heechul/Python_study/jump_to_python/chapter04/new_file.txt', 'w')
f.close


## 파일을 쓰기 모드로 열어 출력값 적기
f = open('D:/Heechul/Python_study/jump_to_python/chapter04/new_file.txt', 'w')
for i in range(1, 11):
    data = "Tise is %d line.\n" % i
    f.write(data)
f.close()


## 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
# 1) readline() 함수 이용하기
f = open('D:/Heechul/Python_study/jump_to_python/chapter04/new_file.txt', 'r')
line = f.readline()
print(line)
f.close()

f = open('D:/Heechul/Python_study/jump_to_python/chapter04/new_file.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 2) readlines 함수 사용하기
f = open('D:/Heechul/Python_study/jump_to_python/chapter04/new_file.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# 3) read 함수 사용하기
f = open('D:/Heechul/Python_study/jump_to_python/chapter04/new_file.txt', 'r')
data = f.read()
print(data)
f.close


## 파일에 새로운 내용 추가하기
f = open('D:/Heechul/Python_study/jump_to_python/chapter04/new_file.txt', 'a')
for i in range(11, 20):
    data = 'This is %d line.\n' % i
    f.write(data)
f.close


## with문과 함께 사용하기
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open('foo.txt', 'w') as f:
    f.write('Life is too short, you need python')

# [sys 모듈로 매개변수 주기]
# 명령 프롬프트 명령어 [인수1 인수2 ...]
import sys

args = sys.argv[1:]
for i in args:
    print(i)


import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')