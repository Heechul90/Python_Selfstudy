### 05장. 파이썬 날개날기
## 연습문제


## Q9
## 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트를 작성해 보자.
import sys

numbers = sys.argv[1:]     # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result = result + int(number)
print(result)

