### 05장. 파이썬 날개날기
## 05-5. 내장함수


# filter1.py
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))