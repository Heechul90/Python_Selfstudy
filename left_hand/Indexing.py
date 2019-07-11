### Indexing (주소)
## 문자열 안에도 주소가 있음

# 0 1 2 3 4 5  <- index  (0부터 시작)
# p y t h o n  <- [2] = t


my_name = '이희철의 코딩코딩'
print(my_name)

# 0 1 2 3 4 5 6 7 8
# 이희철의  코딩코딩
print(my_name[4])    # 빈칸을 데려옴
print(my_name[1])    # '이'를 데려옴

## -는 뒤에서부터 시작함
# -6 -5 -4 -3 -2 -1
#  p  y  t  h  o  n
my_name1 = 'python'
print(my_name1[-1])  # 'n'을 데려옴


animals = []
animals.append('코알라')
animals.append('하이에나')
animals.append('바다소')
animals.append('다람쥐')
print(animals)

print(animals[3])

del animals[1]

print(animals)