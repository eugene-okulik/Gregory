import random

salary = int(input('Введите число '))
bonus = bool(random.randint(0, 1))

if bonus:
    salary = salary + int(random.randint(1, 1000))

print(f'${salary}')
