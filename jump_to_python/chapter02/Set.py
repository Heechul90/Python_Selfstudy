### 02장. 파이썬 프로그래밍의 기초, 자료형
## 02-6. 집합 자료형


## 집합 자료형은 어떻게 만들까?
s1 = set([1, 2, 3])
print(s1)

s2 = set('Hello')
print(s2)

s = set()     # 비어 있는 집합 자료형


## 집합 자료형의 특징
# 중복을 허용하지 않는다
# 순서가 없다(Unordered)
s1 = set([1,2,3])
l1 = list(s1)
print(l1)
l1[0]

t1 = tuple(s1)
print(t1)
t1[0]
# 중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다



## 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 1) 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 2) 합집합
print(s1 | s2)
print(s1.union(s2))

# 3) 차집합
print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)
print(s2.difference(s1))


## 집합 자료형 관련 함수들
# 1) 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 2) 값 여러 개 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

# 3) 특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)