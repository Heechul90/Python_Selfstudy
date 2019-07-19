## 별 찍기 - 13

# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# 입력: 3
# *
# **
# ***
# **
# *

n = int(input('1부터 100 사이의 정수를 입력: '))


for i in reversed(range(0, n)):
    for k in range(0, n - i):
        print('*', sep = '', end = '')
    print(' ' * i)

for i in range(1, n):
    for k in range(n - i):
        print('*', sep = '', end = '')
    print(' ' * i)