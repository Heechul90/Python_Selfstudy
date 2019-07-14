### 05장. 파이썬 날개날기
## 05-5. 내장함수


# positive.py
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))