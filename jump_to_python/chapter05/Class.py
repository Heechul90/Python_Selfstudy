### 05장. 파이썬 날개날기
## 05-1. 클래스


## 클래스는 왜 필요한가?
# 계산기
result = 0

def add(num):
    global result
    result = result + num
    return result

print(add(3))
print(add(4))

# 계산기가 2개 필요할 경우
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# class
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


# 빈 클래스
class Cookie:
    pass


## 사칙연산 클래스 만들기
# 클래스를 어떻게 만들지 먼저 구상하기
# a = FourCal()
# a.setdata(4, 2)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

# 클래스 구조 만들기
class FourCal:
    pass
# pass는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 사용한다
# a = FourCal()
# print(type(a))

# 객체에 숫자 지정할 수 있게 만들기
#a.setdata(4, 2)

# 클래스 내부의 함수는 메서드(Method)
# class FourCal:
#     def setdata(self, first, second):  # ① 메서드의 매개변수
#         self.first = first             # ② 메서드의 수행문
#         self.second = second           # ② 메서드의 수행문

# 1) setdata 메서드의 매개변수
# a = FourCal()
# a.setdata(4, 2)

# 메서드의 첫 번째 매개변수 self를 명시적으로 구현하는 것은 
# 파이썬만의 독특한 특징이다
# 예를 들어 자바 같은 언어는 첫 번째 매개변수 self가 필요없다

# 2) setdata 메서드의 수행문
# def setdata(self, first, second):   # ① 메서드의 매개변수
#     self.first = first              # ② 메서드의 수행문
#     self.second = second            # ② 메서드의 수행문

# a = FourCal()
# a.setdata(4, 2)
# print(a.first)
# print(a.second)


# a = FourCal()
# b = FourCal()

# a.setdata(4, 2)
# print(a.first)

# b.setdata(3, 7)
# print(b.first)
# print(a.first)

# a = FourCal()
# b = FourCal()
# a.setdata(4, 2)
# b.setdata(3, 7)
# id(a.first)   # a의 first 주소값을 확인
# id(b.first)   # b의 first 주소값을 확인


a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,8)
print(a.add())



## 생성자 (Constructor)
a = FourCal()
a.add()



# __init__ 메서드의 init 앞뒤로 붙은 __는 언더스코어(_) 두 개를 붙여 쓴 것
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result



## 클래스의 상속
class MoreFourCal(FourCal):
    pass

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


## 메서드 오버라이딩
a = FourCal(4, 0)
a.div()

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second


## 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)
