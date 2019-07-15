### 06장. 파이썬 프로그래밍, 어떻게 시작해야 할까?
## 06-1. 내가 프로그램을 만들 수 있을까?


def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i += 1
    return(result)

print(gugu(2))

print(gugu(4))