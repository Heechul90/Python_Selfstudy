### Logical 논리연산자


## and : 둘다
## or : 둘중 하나
## not : 둘다 아님

# and
print(True and True)
print(True and False)
print(False and False)

# and 둘다 만족해야 함
height = 120
age = 8
print(height > 140 and age > 10)

height = 190
age = 9
print(height > 140 and age > 10)

height = 150
age = 32
print(height > 140 and age > 10)


# or
print(True or True)
print(True or False)
print(False or False)

# or 하나만 만족해도 됨
height = 120
age = 8
print(height > 140 or age > 10)

height = 190
age = 9
print(height > 140 or age > 10)

height = 150
age = 32
print(height > 140 or age > 10)



