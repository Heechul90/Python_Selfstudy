### 02장. 파이썬 프로그래밍의 기초, 자료형
## 02-2. 문자열 자료형

print("Life is too short, You need Python")
print('a')
print('123')

## 문자열은 어떻게 만들고 사용할까?
# 1) 큰따옴표("")로 양쪽 둘러싸기
print("Hello World")

# 2) 작은따옴표('')로 양쪽 둘러싸기
print('Python is fun')

# 3) 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")

# 4) 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
print('''Life is too short, You need Pyton''')

## 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
# 1) 문자열에 작은따옴표(') 포함시키기
food = "Python's favorite food is perl"
print(food)

# 2) 문자열에 큰따옴표(") 포함시키기
say = '"Python is very easy." he says.'
print(say)

# 3) 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very seah.\" he says."
print(food)
print(say)

## 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1) 줄을 바꾸기 위한 이스케이프 코드 \n(이스케이프 문자중 하나) 삽입하기
multiline = "Life is too short\nYou need python"
print(multiline)

# 2) 연속된 작은따옴표 3개(''')또는 큰따옴표 3개("")사용하기
multiline = '''
Life is too short
You need python
'''
print(multiline)

multiline = """
Life is too short
You need python
"""
print(multiline)
# 작음 따옴표 3개나 큰 따옴표 3개나 똑같은 결과가 나온다


## 문자열 연산하기
# 1) 문자열 더해서 연결하기(Concatenation)
head = 'Python'
tail = ' is fun!'
print(head + tail)

# 2) 문자열 곱하기
a = 'Python'
print(a * 2)

# 3) 문자열 곱하기 응용
print('=' * 50)
print('My Program')
print('=' * 50)

# 4) 문자열 길이 구하기
a = 'Life is too short'
print(len(a))


## 문자열 인덱싱과 슬라이싱
# 1) 문자열 인덱싱이란?
a = 'Life is too short, You need Python'
print(a[3])

# "파이썬은 0부터 숫자를 센다"

# 2) 문자열 인덱싱 활용하기
print(a[0])
print(a[12])
print(a[-1])
print(a[-0])     # 0과 -0은 같은 값이다

# 3) 문자열 슬라이싱이란?
a = 'Life is too short, You need Python'
print(a[0:4])
print(a[0:3])

# 4) 문자열 슬라이싱하는 방법
print(a[0:5])    # 공백도 문자열에 포함된다
print(a[0:2])
print(a[5:7])
print(a[12:17])

print(a[19:])    # 19부터 끝까지 출력된다
print(a[:17])    # 처음부터 17까지 출력된다

print(a[:])      # 처음부터 끝까지 출력한다.
print(a[19:-7])  

# 4) 슬라이싱으로 문자열 나누기
a = '20010331Rainy'
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = '20010331Rainy'
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

# "Pithon"이라는 문자열을 "Python으로 바꾸려면?"
a = 'Pithon'
# a[1] = y     # 문자열은 바꿀수 없어서 오류가 난다.

print(a[:1] + 'y' + a[2:])


## 문자열 포매팅 (Formatting)
# 1) 숫자 바로 대입
'I eat %d apples.' % 3

# 2) 문자열 바로 대입
'I eat %s apples.' % 'five'

# 3) 숫자 값 나타내는 변수로 대입
number = 3
'I eat %d apples.' % number

# 4) 2개 이상의 값 넣기
number = 10
day = 'three'
'I ate %d apples. so I was sick for %s days' % (number, day)


## 포맷 코드와 숫자 함께 사용하기
# 1) 정렬과 공백
print('%10s' % 'hi')
print('%-10sjane.' % 'hi')

# 2) 소수점 표현하기
print('%0.4f' % 3.42134234)      # 소수점 4자리 까지만
print('%10.4f' % 3.42134234)     # 문자열이 10인 소수점 4자리 까지만


## format 함수를 사용한 포매팅
# 1) 숫자 바로 대입하기
print('I eat {0} apples.'.format(3))

# 2) 문자열 바로 대입하기
print('I eat {0} apples.'.format('five'))

# 3) 숫자 값을 가진 변수로 대입하기
number = 4
print('I eat {0} apples.'.format(number))

# 4) 2개 이상의 값 넣기
number = 10
day = "three"
print('I eat {0} apples. so I was sick for {1} days.'.format(number, day))

# 5) 이름으로 넣기
print('I ate {number} apples. so I was sick for {day} days.'.format(number=10, day=3))

# 6) 인덱스와 이름을 혼용해서 넣기
print('I ate {0} apples. so I was sick for {day} days.'.format(10, day=3))

# 7) 왼쪽 정렬
print('{0:<10}'.format('hi'))

# 8) 오른쪽 정렬
print('{0:>10}'.format('hi'))

# 9) 가운데 정렬
print('{0:^10}'.format('hi'))

# 10) 공백 채우기
print('{0:=^10}'.format('hi'))
print('{0:!<10}'.format('hi'))

# 11) 소수점 표현하기
y = 3.42134234
print('{0:0.4f}'.format(y))     # 소수점 4자리 까지만
print('{0:10.4f}'.format(y))     # 문자열이 10자리인 소수점 4자리 까지만

print('{{ and }}'.format())


## f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name' : '홍길동', 'age' : 30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}')     # 왼쪽 정렬
print(f'{"hi":>10}')     # 오른쪽 정렬
print(f'{"hi":^10}')     # 가운데 정렬

print(f'{"hi":=^10}')     # 가운데 정렬
print(f'{"hi":!<10}')     # 가운데 정렬

y = 3.42134234
print(f'{y:0.4f}')  # 소수점 4자리까지만 표현
print(f'{y:10.4f}')  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤

print(f'{{ and }}')


## 문자열 관련 함수들
# 1) 문자 개수 세기(count)
a = 'hobby'
print(a.count('b'))

# 2) 위치 알려주기1(find)
a = 'Python is the best choice'
print(a.find('b'))
print(a.find('k'))

# 3) 위치 알려주기2(index)
a = 'Life is too short'
print(a.index('t'))
# print(a.index('k'))     # find 함수와는 다르게 찾는 문자열이 없으면 에러난다

# 4) 문자열 삽입(join)
# ','.join('abcd')
# ",".join(['a', 'b', 'c', 'd'])

# 5) 소문자를 대문자로 바꾸기(upper)
a = 'hi'
print(a.upper())

# 6) 대문자를 소문자로 바꾸기(lower)
a = 'HI'
print(a.lower())

# 7) 왼쪽 공백 지우기(lstrip)
a = ' hi '
print(a.lstrip())

# 8) 오른쪽 공백 지우기(rstrip)
a = ' hi '
print(a.rstrip())

# 9) 양쪽 공백 지우기(strip)
a = ' hi '
print(a.strip())

# 10) 문자열 바꾸기(replace)
a = 'Life is too short'
print(a.replace('Life', 'Your leg'))

# 11) 문자열 나누기(split)
a = 'Life is too shor'
print(a.split())

b = 'a:b:c:d'
print(b.split(':'))
