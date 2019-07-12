### Module


## random
import random

# random.choice
students = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(random.choice(students))

# random.sample
print(random.sample(students, 2))
print(random.sample(students, 4))

print(random.sample(range(1, 46), 6))

# random.randint()
print(random.randint(8, 10))