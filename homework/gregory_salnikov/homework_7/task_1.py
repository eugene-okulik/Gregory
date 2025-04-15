i = 5

while True:
    user_input = input('Введите любую цифру: ')
    if int(user_input) == i:
        break
    else:
        print('Эта не подходит, введите другую цифру: ')

print('Поздравляю! Вы угадали!')
