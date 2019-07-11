### For

# for 변수 in 컨테이너:
#    실행할 명령1
#    실행할 명령2
#

python = (1, 2, 3, 4, 5)

for num in python:
    print(num)

for my_str in '희철이의 파이썬':
    print(my_str)
    


## 중복해서 사용하기
for i in range(2, 10):
    print(i)

## 구구단 출력하기

for j in range(2,10):
    for i in range(1,10):
        print('{}x{}={}'.format(j, i, j*i))
