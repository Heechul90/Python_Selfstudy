### 02장. 파이썬 프로그래밍의 기초, 자료형
## 02-3. 리스트 자료형

## 리스트는 어떻게 만들고 사용할까?
odd = [1,3,5,7,9]
a = []           # a = list() 이렇게 생성할 수도 있다.
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]


## 리스트의 인덱싱과 슬라이싱
# 리스트
a = [1, 2, 3]
print(a[0])
print(a[0] + a[2])
print(a[-1])

# 이중 리스트
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])

print(a[-1][0])

# 삼중 리스트
a =  [1, 2, 3, ['a', 'b', 'c', ['Life', 'is']]]
print(a[-1])
print(a[-1][-1])
print(a[-1][-1][0])


## 리스트의 슬라이싱
a = list(range(1, 6))
print(a)
print(a[0:2])

b = a[:2]
c = a[2:]
print(b)
print(c)


# 리스트 연산하기
a = [1, 2, 3]
b = [4, 5, 6]

# 리스트 더하기
print(a+b)

# 리스트 반복하기
print(a * 3)

# 리스트 길이구하기
print(len(a))


## 리스트의 수정과 삭제
# 리스트에서 값 수정하기
a = list(range(1,4))
print(a)
a[2] = 4
print(a)

# del 함수 사용해 리스트 요소 삭제하기
a = list(range(1,4))
print(a)
del a[1]
print(a)

a = list(range(1,6))
del a[2:]
print(a)


## 리스트 관려 함수들
# 리스트에 요소 추가(append)
a = list(range(1,4))
a.append(4)
print(a)

a.append([5, 6])
print(a)

# 리스트 정렬(sort)
a = [1, 4, 5, 2, 3]
a.sort()
print(a)

a = ['b', 'c', 'a', 'd']
a.sort()
print(a)

# 리스트 뒤집기(reverse)
a = ['b', 'c', 'a', 'd']   # 역정렬이 아닌 현재 리스트 그대로 거꾸로 뒤집음
a.reverse()
print(a)

# 위치 반환(index)
a = list(range(1,4))
print(a.index(3))          # x의 값의 위치를 알려준다
print(a.index(1))

# 리스트에 요소 삽입(insert)
# insert(a, b) : a위치에 b를 삽입

a = [1, 2, 3]
a.insert(0, 5)
print(a)

a.insert(1, 6)
print(a)

# 리스트 요소 제거(remove)
a = list(range(1,4)) * 2
print(a)
a.remove(3)       # 첫번째 3이 제거된다
print(a)
a.remove(3)       # 두번째 3이 제거된다
print(a)


## 리스트 요소 끄집어내기(pop)
# 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다
a = [1, 2, 3]
a.pop()
print(a)

a = [1, 2, 3]
a.pop(1)
print(a)


## 리스트에 포함된 요소 x의 개수 세개(count)
a = [1, 2, 3, 1]
print(a.count(1))


## 리스트 확장(extend)
a = [1, 2, 3]
a.extend([4, 5])
print(a)

b = [6, 7]
a.extend(b)
print(a)