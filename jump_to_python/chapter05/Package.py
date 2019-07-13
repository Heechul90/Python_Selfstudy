### 05장. 파이썬 날개날기
## 05-3. 패키지


## 패키지란 무엇인가?
# 패키지(Packages)는 도트(.)를 사용하여 
# 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다
#  예를 들어 모듈 이름이 A.B인 경우에 
# A는 패키지 이름이 되고 B는 A 패키지의 B모듈이 된다

# 가상의 game 패키지 예
# game/
#     __init__.py
#     sound/
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py


## 패키지 만들기
# 패키지 기본 구성 요소 준비하기

## 패키지 안의 함수 실행하기
import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()

# 점프 투 파이썬에서 안된다고 하는데 여기서 된다
import game
game.sound.echo.echo_test()

# import game.sound.echo.echo_test # import에서 마지막항목이 반드시 모듈 또는 패키지여야 한다


## __init__.py 의 용도
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다
#  만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 
# __init__.py 파일이 없다면 패키지로 인식되지 않는다

# 점프 투 파이썬에서 안된다고 하는데 여기서 된다
from game.sound import *
echo.echo_test()

from game.sound import *
echo.echo_test()



## relative 패키지
from game.graphic.render import render_test
render_test()

# .. – 부모 디렉터리
# .  – 현재 디렉터리
# ..과 같은 relative한 접근자는 render.py처럼 모듈 안에서만 사용해야 한다
