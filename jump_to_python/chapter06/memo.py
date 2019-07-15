### 06장. 파이썬 프로그래밍, 어떻게 시작해야 할까?
## 06-4. 간단한 메모장 만들기



import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)