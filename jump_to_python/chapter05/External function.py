### 05장. 파이썬 날개날기
## 05-6. 외장함수


## sys
## sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
# 명령 행에서 인수 전달하기 - sys.argv
# argv_test.py
# import sys
# print(sys.argv)

# 강제로 스크립트 종료하기 - sys.exit
# sys.exit()

# 자신이 만든 모듈 불러와 사용하기 - sys.path
# import sys

# 형재 디렉터리
# sys.path

# 경로 추가
# sys.path.append('D:/Heechul/Python_study/jump_to_python/chapter05/mymod')



## pickle
## pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
## 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 
## 그대로 파일에 저장하는 방법을 보여 준다.
import pickle
f = open('test1.txt', 'wb')
data = {1 : 'python', 2 : 'you need'}
pickle.dump(data, f)
f.close()

# 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 예
import pickle
f = open('test1.txt', 'rb')
data = pickle.load(f)
print(data)


## os
## OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.
# 내 시스템의 환경 변수값을 알고 싶을 때 - os.environ
import os
print(os.environ)

os.environ['PATH']

# 디렉터리 위치 변경하기 - os.chdir
# os.chdir("C:\WINDOWS")

# 디렉터리 위치 돌려받기 - os.getcwd
# os.getcwd()

# 시스템 명령어 호출하기 - os.system
# os.system("dir")

# 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
# f = os.popen("dir")
#  print(f.read())


# 기타 유용한 os 관련 함수
# os.mkdir(디렉터리)	디렉터리를 생성한다.
# os.rmdir(디렉터리)	디렉터리를 삭제한다.단, 디렉터리가 비어있어야 삭제가 가능하다.
# os.unlink(파일)	파일을 지운다.
# os.rename(src, dst)	src라는 이름의 파일을 dst라는 이름으로 바꾼다.



## shutil
## shutil은 파일을 복사해 주는 파이썬 모듈이다.
# import shutil
# shutil.copy("src.txt", "dst.txt")


## glob
## 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 
## 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다. 
## 이럴 때 사용하는 모듈이 바로 glob이다.
# 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)
# mark로 시작하는 파일을 모두 찾아서 읽어오기
import glob
glob.glob("D:/Heechul/Python_study/mark*")



## tempfile
## 파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다. 
## tempfile.mktemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
import tempfile
f = tempfile.TemporaryFile()
f.close


## time
# 1) time.time
# time.time()은 UTC(Universal Time Coordinated 협정 세계 표준시)를 사용하여 
# 현재 시간을 실수 형태로 돌려주는 함수이다. 
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려준다.
import time
print(time.time())

# 2) time.localtime
# time.localtime은 time.time()이 돌려준 실수 값을 사용해서 
# 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수이다.
print(time.localtime(time.time()))

# 3) time.asctime
# 위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 
# 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.
print(time.asctime(time.localtime(time.time())))

# 4) time.ctime()
# time.asctime(time.localtime(time.time()))은 time.ctime()을 사용해 간편하게 표시할 수 있다. 
# asctime과 다른 점은 ctime은 항상 현재 시간만을 돌려준다는 점이다.
print(time.ctime())

# 5) time.strftime
# print(time.strftime('출력할 형식 포맷 코드', time.localtime(time.time())))
import time
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

# 시간에 관계된 것을 표현하는 포맷 코드
# %a	요일 줄임말	                            Mon
# %A	요일	                               Monday
# %b	달 줄임말	                             Jan
# %B	달	                                    January
# %c	날짜와 시간을 출력함          	         06/01/01 17:22:21
# %d	날(day)	                               [00,31]
# %H	시간(hour)-24시간 출력 형태	            [00,23]
# %I	시간(hour)-12시간 출력 형태             [01,12]
# %j	1년 중 누적 날짜	                    [001,366]
# %m	달	                                   [01,12]
# %M	분	                                   [01,59]
# %p	AM or PM	                           AM
# %S	초	                                   [00,61]
# %U	1년 중 누적 주-일요일을 시작으로	     [00,53]
# %w	숫자로 된 요일	                        [0(일요일),6]
# %W	1년 중 누적 주-월요일을 시작으로       	 [00,53]
# %x	현재 설정된 로케일에 기반한 날짜 출력	  06/01/01
# %X	현재 설정된 로케일에 기반한 시간 출력	  17:22:21
# %Y	년도 출력	                            2001
# %Z	시간대 출력	                            대한민국 표준시
# %%	문자	                               %
# %y	세기부분을 제외한 년도 출력	             01


# 6) time.sleep
# time.sleep 함수는 주로 루프 안에서 많이 사용한다. 
# 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다.
# sleep1.py
# import time
# for i in range(10):
#     print(i)
#     time.sleep(1)



## calendar
## calendar는 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.
## calendar.calendar(연도)로 사용하면 그해의 전체 달력을 볼 수 있다.
import calendar
print(calendar.calendar(2015))

# 1) calendar.weekday
# weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다. 
# 월요일은 0, 화요일은 1, 수요일은 2, 목요일은 3, 금요일은 4, 토요일은 5, 일요일은 6이라는 값을 돌려준다.
print(calendar.weekday(2015, 12, 31))

# 2) calendar.monthrange
# monthrange(연도, 월) 함수는 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.
print(calendar.monthrange(2015,12))


## random
## random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다.
# 0.0에서 1.0 사이의 실수 중에서 난수 값을 돌려주는 예
import random
print(random.random())

# 1에서 10 사이의 정수 중에서 난수 값
print(random.randint(1, 10))
# 1에서 55 사이의 정수 중에서 난수 값
print(random.randint(1, 55))

# random_pop.py
import random
def random_pop(data):
    number = random.randint(0, len(data)- 1)
    return data.pop(number)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

# random.choice
def random_pop1(data):
    number = random.choice(data)
    data.remove(number)
    return number
a = [1, 2, 3, 4, 5]
print(random_pop1(a))


# random.shuffle
import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)



## webbrowser
## webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다.
import webbrowser
webbrowser.open('http://google.com')

# 새로운 창으로 열기
webbrowser.open_new('http://google.com')

# [스레드를 다루는 threading 모듈]
# thread_test.py