### 02장. 파이썬 프로그래밍의 기초, 자료형
## 02-1. 문자열 자료형

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
