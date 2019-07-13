### 05장. 파이썬 날개날기
## 05-2. 모듈


## 모듈 만들기
# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈이다

## 모듈 불러오기
import mod1
print(mod1.add(3,4))
print(mod1.sub(4,2))

# import의 사용 방법
# import 모듈이름
# from 모듈이름 import 모듈함수
# mod1.py
from mod1 import add
print(add(3,4))

from mod1 import add, sub     # 두 가지 함수 불러오기
from mod1 import *            # mod1의 모든 함수 불러오기


# if __name__ == "__main__": 의 의미
# __name__ 변수란?
# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다


## 클래스나 변수 등을 포함한 모듈
# mod2.py
# import mod2
# print(mod2.add(mod2.PI, 4.4))


## 다른 파일에서 모듈 불러오기
# 1) sys.path.append(모듈을 저장한 디렉터리) 사용하기
import sys
print(sys.path)

sys.path.append('D:\Heechul\Python_study\jump_to_python\chapter05\mymod')
print(sys.path)

import mod2
print(mod2.add(3, 5))