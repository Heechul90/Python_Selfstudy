### 06장. 파이썬 프로그래밍, 어떻게 시작해야 할까?
## 06-3. 게시판 페이징하기

# 게시물의 총 건수(m)	페이지당 보여줄 게시물 수(n)	총 페이지 수
# 5	                   10	                         1
# 15	               10	                         2
# 25		           10	                   	     3
# 30		           10		                     3

# 1) 총 페이지 구하기
def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))



## review
def getTotalPage(m, n):
    if m % n == 0:
        return (m // n)
    else:
        return (m // n) + 1
getTotalPage(5, 10)
getTotalPage(15, 10)
getTotalPage(25, 10)
getTotalPage(30, 10)



