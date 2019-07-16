### 07장. 정규표현식
## 07-2. 정규 표현식 시작하기


## 정규 표현식의 기초, 메타 문자
## 메타 문자란 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자를 말한다.
## . ^ $ * + ? { } [ ] \ | ( )

## 1) 문자 클래스 [ ]
# [a-zA-Z] : 알파벳 모두
# [0-9]    : 숫자
# [^0-9]   : 숫자가 아닌 문자

# [자주 사용하는 문자 클래스]
# \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
# \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.


## 2) Dot(.)
# "a + 모든문자 + b"
# "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
# "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
# "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않는다.

# a[.]b = "a + Dot(.)문자 + b"



## 3) 반복 (*)
# 정규식 표현 : ca*t
# * 바로 앞에 있는 문자 a가 0부터 무한대로 반복될 수 있다는 의미
# 정규식	문자열	Match 여부	설명
# ca*t	    ct	   Yes	       "a"가 0번 반복되어 매치
# ca*t	    cat	   Yes	       "a"가 0번 이상 반복되어 매치 (1번 반복)
# ca*t	    caaat  Yes	       "a"가 0번 이상 반복되어 매치 (3번 반복)



## 4) 반복 (+)
## +는 최소 1번 이상 반복될 때 사용한다. 
## 즉 *가 반복 횟수 0부터라면 +는 반복 횟수 1부터인 것이다.
# 정규식	문자열	Match 여부	설명
# ca+t	    ct	   No	      "a"가 0번 반복되어 매치되지 않음
# ca+t	    cat	   Yes	      "a"가 1번 이상 반복되어 매치 (1번 반복)
# ca+t	    caaat  Yes	      "a"가 1번 이상 반복되어 매치 (3번 반복)



## 4) 반복 ({m,n}, ?)
## {3,}처럼 사용하면 반복 횟수가 3 이상인 경우이고 
## {,3}처럼 사용하면 반복 횟수가 3 이하를 의미
## {1,}은 +와 동일하고, {0,}은 *와 동일하다.
# 1. {m}
# 정규식	문자열	Match 여부	설명
# ca{2}t	cat	   No	      "a"가 1번만 반복되어 매치되지 않음
# ca{2}t	caat   Yes	      "a"가 2번 반복되어 매치

# 2. {m, n}
# 정규식	문자열	Match 여부	설명
# ca{2,5}t	cat	    No	      "a"가 1번만 반복되어 매치되지 않음
# ca{2,5}t	caat	Yes	      "a"가 2번 반복되어 매치
# ca{2,5}t	caaaaat	Yes	      "a"가 5번 반복되어 매치

# 3. ?
# ? 메타문자가 의미하는 것은 {0, 1} 이다.
# ab?c : "a + b(있어도 되고 없어도 된다) + c"
# 정규식	문자열	Match 여부	설명
# ab?c	    abc	   Yes	      "b"가 1번 사용되어 매치
# ab?c	    ac	   Yes	      "b"가 0번 사용되어 매치



## 파이썬에서 정규 표현식을 지원하는 re 모듈
import re
p = re.compile('ab*')


## 정규식을 이용한 문자열 검색
# Method	    목적
# match()	    문자열의 처음부터 정규식과 매치되는지 조사한다.
# search()	    문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall()	    정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
# finditer()	정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.

import re
p = re.compile('[a-z]+')

# 1) match     # 처음부터 검색
m = p.match('python')
print(m)

m = p.match('3 python')
print(m)

p = re.compile('[a-z]+')      # 정규식표현을 넣으면 됨
m = p.match( 'string goes here')
if m:
    print('Match found: ', m.group())
else:
    print('No match')

# 2) search     # 전체를 검색
m = p.search('python')
print(m)

m = p.search('3 python')
print(m)

# 3) finditer
result = p.finditer("Life is too short")
print(result)

for r in result:
    print(r)

# finditer는 findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 돌려준다. 
# 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.



## match 객체의 메서드
# 어떤 문자열이 매치되었는가?
# 매치된 문자열의 인덱스는 어디서부터 어디까지인가?
# method	목적
# group()	매치된 문자열을 돌려준다.
# start()	매치된 문자열의 시작 위치를 돌려준다.
# end()	매치된 문자열의 끝 위치를 돌려준다.
# span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

m = p.match('python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = p.search('3 python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# [모듈 단위로 수행하기]
p = re.compile('[a-z]+')
m = p.match('python')

# 위와 같은 표현
m = re.match('[a-z]+', 'python')



## 컴파일 옵션
# DOTALL(S)     - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
# IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
# MULTILINE(M)  - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
# VERBOSE(X)    - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)

# 1) DOTALL, S
# . 메타 문자는 줄바꿈 문자(\n)를 제외한 모든 문자와 매치되는 규칙이 있다.
# 만약 \n 문자도 포함하여 매치하고 싶다면
# re.DOTALL 또는 re.S 옵션을 사용해 정규식을 컴파일하면 된다.
import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)

# 2) IGNORECASE, I
# re.IGNORECASE 또는 re.I 옵션은 대소문자 구별 없이 
# 매치를 수행할 때 사용하는 옵션이다.

p = re.compile('[a-z]', re.I)
m = p.match('python')
print(m)

m = p.match('Python')
print(m)

p.match('PYTHON')
print(m)

# 3) MULTILINE, M
# ^는 문자열의 처음을 의미하고, $는 문자열의 마지막을 의미한다. 
# 정규식 ^python\s\w+은 python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 와야 한다는 의미
import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))


import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))


## VERBOSE, X
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)



## 백슬래시 문제
p = re.compile('\\section')
p = re.compile('\\\\section')
p = re.compile(r'\\section')

