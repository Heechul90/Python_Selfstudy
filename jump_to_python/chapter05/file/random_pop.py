### 05장. 파이썬 날개날기
## 05-6. 외장함수


## random
# random_pop.py
import random
def random_pop(data):
    number = random.randint(0, len(data)- 1)
    return data.pop(number)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))