# 1부터 10까지 숫자의 합계를 구하는 프로그램
s = 0                            # 합계를 구하는 변수 s, 처음 값은 0을 입력합니다.
for x in range(1, 10+1):         # 1,2,...,10까지 10번 반복합니다(11은 제외).
    s = s + x                    # 현재의 s값에 x를 더합니다.
    print("x:", x, " sum:", s)   # 현재의 x값과 s값을 출력합니다.
