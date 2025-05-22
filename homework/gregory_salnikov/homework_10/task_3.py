def operation_selector(func):
    def wrapper(first, second, operation=None):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '/'

        return func(first, second, operation)

    return wrapper


@operation_selector
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second if second != 0 else "Ошибка: деление на ноль"
    else:
        return "Неизвестная операция"


try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result = calc(num1, num2)
    print(f"Результат: {result}")

except ValueError:
    print("Ошибка: введите числа корректно")
