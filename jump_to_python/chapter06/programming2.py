### 06장. 파이썬 프로그래밍, 어떻게 시작해야 할까?
## 06-2. 3과 5의 배수 합하기

## 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
## 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result = result + n
        
print(result)


## [코딩 연습을 할 수 있는 사이트]
# 프로젝트 오일러(http://projecteuler.net/archives)



## review
result = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result = result + i
print(result)