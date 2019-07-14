### 05장. 파이썬 날개날기
## 05-5. 내장함수


# two_times.py
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)