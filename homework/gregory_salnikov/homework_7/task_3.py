results = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат: 2'
]

def add_10(text):
    index = text.index(':')
    number = int(text[index + 1:])
    return number + 10

for res in results:
    print(add_10(res))
