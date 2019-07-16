### 07장. 정규표현식
## 07-1. 정규 표현식 살펴보기


## 정규 표현식은 왜 필요한가?

# 정규식을 모를 때
data = """
part 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split('\n'):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + '-' + '******'
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))


# 정규식을 알 때
import re 

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))