### Loop


## 1) while
# while 조건:
#     실행할 명령1
#     실행할 명령2
# 조건을 검사해서 T 면 실행 후 다시 돌아와 검사

count = 0
while count < 3:
    print('횟수', count )
    count += 1   # : count = count + 1

### continue
### break
count = 0
while count < 10:
    count += 1   # : count = count + 1
    if count < 4:
        continue    
    print('count', count )
    if count == 8:
        break