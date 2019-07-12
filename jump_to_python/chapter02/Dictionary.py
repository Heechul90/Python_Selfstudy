### 02장. 파이썬 프로그래밍의 기초, 자료형
## 02-5. 딕션너리 자료형


## 딕셔너리는 어떻게 만들까?
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# Key에는 변하지 않는 값을 사용하고, Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)
a = {1: 'hi'}
print(a)
a = { 'a': [1,2,3]}
print(a)


## 딕셔너리 쌍 추가, 삭제하기
# 1) 딕셔너리 쌍 추가하기
a = {1: 'a'}

a[2] = 'b'
print(a)

a['name'] = 'Heechul'
print(a)

a[3] = [1, 2, 3]
print(a)

# 2) 딕셔너리 요소 삭제하기
del a[1]
print(a)


## 딕셔너리를 사용하는 방법
# 1) 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {1:'a', 2:'b'}
print(a[1])     # 두번째 요소를 뜻하는게 아니라 key에 해당하는 1을 의미
print(a[2])     # 세번째 요소를 뜻하는게 아니라 key에 해당하는 2을 의미

a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

# 2) 딕셔너리 만들 때 주의할 사항
# key값이 두개가 되면 하나를 제외한 나머지 것들이 모두 무시된다
a = {1:'a', 1:'b'}
print(a)

# Key에 리스트는 쓸 수 없다
# a = {[1,2] : 'hi'}     # 에러가 난다


## 딕셔너리 관련 함수들
# 1) Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())
print(list(a.keys()))

for k in a.keys():
    print(k)

# 2) Value 리스트 만들기(values)
print(a.values())

# 3) Key, Value 쌍 얻기(items)
print(a.items())

# 4) Key: Value 쌍 모두 지우기(clear)
print(a.clear())

# 5) Key로 Value얻기(get)
# a[]에서 key값이 없으면 오류가 났는데 get은 None을 돌려준다
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('nokey'))
# print(a['nokey'])     # 에러가 난다

# a 딕셔너리에는 'foo'에 해당하는 값이 없으면 디폴트 값인 'bar'를 돌려준다
print(a.get('foo', 'bar'))

# 6) 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
print('email' in a)