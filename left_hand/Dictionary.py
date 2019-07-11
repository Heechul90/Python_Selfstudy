### Dictionary

## 검색하면 값이 나온다
my_dict = {'헤흐': '남', 'Meta' : '남', '이희철' : '여'}
my_dict['이희철']


my_dict1 = {}

# 값을 넣기
my_dict1[0] = 'a'
my_dict1['b'] = 2
my_dict1['학생'] = '이희철'
my_dict1['student'] = 'Heechul Lee'

print(my_dict1)

# 검색하기
print(my_dict1['student'])
print(my_dict1['b'])


# 지우기
del my_dict1[0]
print(my_dict1)


### dict.values() : dict에서 값만 뽑아 오는것
my_dict2 = {'student1' : 'a', 'student2' : 'b', 'student3' : 'c'}
print(my_dict2)

for std in my_dict2.values():
    print(std)


### dict.keys()   : dict에서 키만 뽑아 오는것

for std in my_dict2.keys():
    print(std)


### dick.items()  : dict에서 값과 키를 다 뽑아 오는것
for key, val in my_dict2.items():
    print(key, val)