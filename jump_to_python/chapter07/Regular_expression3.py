### 07장. 정규표현식
## 07-3. 강력한 정규 표현식의 세계로


## 메타문자
# 1) |
# A|B라는 정규식이 있다면 A 또는 B라는 의미가 된다.
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

# 2) ^
# ^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다.
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

# 3) $
# $ 메타 문자는 ^ 메타 문자와 반대의 경우이다. 즉 $는 문자열의 끝과 매치함을 의미한다.
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))
# ^ 또는 $ 문자를 메타 문자가 아닌 문자 그 자체로 매치하고 싶은 경우에는
# [^], [$]처럼 사용하거나 \^, \$ 로 사용하면 된다.

# 4) \A
# \A는 문자열의 처음과 매치됨을 의미한다.

# 5) \Z
# \Z는 문자열의 끝과 매치됨을 의미한다.

# 6) \b
# \b는 단어 구분자(Word boundary)이다. 
# 보통 단어는 whitespace에 의해 구분된다.
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))  
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

# 7) \B
# \B 메타 문자는 \b 메타 문자와 반대의 경우이다. 
# 즉 whitespace로 구분된 단어가 아닌 경우에만 매치된다.
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))



## 그루핑
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())

# \w+\s+\d+[-]\d+[-]\d+은 이름 + " " + 전화번호 형태의 문자열을 찾는 정규식
# group(인덱스)	설명
# group(0)	    매치된 전체 문자열
# group(1)	    첫 번째 그룹에 해당되는 문자열
# group(2)	    두 번째 그룹에 해당되는 문자열
# group(n)	    n 번째 그룹에 해당되는 문자열
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")

# 이름만 뽑고 싶을 때
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))

# 번호만 뽑고 싶을 때
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))

# 국번만 뽑고 싶을 때
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))

# 1) 그루핑된 문자열 재참조하기
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())

# 정규식 (\b\w+)\s+\1은 (그룹) + " " + 그룹과 동일한 단어와 매치됨을 의미한다.
# 두 번째 그룹을 참조하려면 \2를 사용하면 된다

# 2) 그루핑된 문자열에 이름 붙이기
# (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
# (\w+) --> (?P<name>\w+)
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))



## 전방 탐색
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
# 전방 탐색에는 긍정(Positive)과 부정(Negative)의 2종류
# 긍정형 전방 탐색((?=...)) : 
# ... 에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# 부정형 전방 탐색((?!...)) : 
# ...에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

# 1) 긍정형 전방 탐색
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

# .*[.].*$
# 이 정규식은 파일 이름 + . + 확장자를 나타내는 정규식이다. 
# 이 정규식은 foo.bar, autoexec.bat, sendmail.cf 같은 형식의 파일과 매치될 것이다.

# .*[.][^b].*$
# 이 정규식은 확장자가 b라는 문자로 시작하면 안 된다는 의미이다. 
# 하지만 이 정규식은 foo.bar라는 파일마저 걸러 낸다.
# .*[.]([^b]..|.[^a].|..[^t])$
# 이 정규식은 | 메타 문자를 사용하여 확장자의
# 첫 번째 문자가 b가 아니거나 
# 두 번째 문자가 a가 아니거나 세 번째 문자가 t가 아닌 경우를 의미한다. 
# .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$

# 2) 부정형 전방 탐색
# .*[.](?!bat$).*$
# 확장자가 bat가 아닌 경우에만 통과된다는 의미이다.
# .*[.](?!bat$|exe$).*$
# exe 도 제외 하라는 의미이다.



## 문자열 바꾸기
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))

print(p.sub('colour', 'blue socks and red shoes', count=1))

# [sub 메서드와 유사한 subn 메서드]
# ubn 역시 sub와 동일한 기능을 하지만 반환 결과를 튜플로 돌려준다는 차이가 있다. 
# 돌려준 튜플의 첫 번째 요소는 변경된 문자열이고, 
# 두 번째 요소는 바꾸기가 발생한 횟수이다.
p = re.compile('(blue|white|red)')
print(p.subn( 'colour', 'blue socks and red shoes'))

# 1) sub 메서드 사용 시 참조 구문 사용하기
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))

# 2) sub 메서드의 매개변수로 함수 넣기
def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))




## Greedy vs Non-Greedy
s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())
print(re.match('<.*?>', s).group())