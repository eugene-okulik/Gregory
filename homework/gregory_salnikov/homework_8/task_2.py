import sys

sys.set_int_max_str_digits(1000000)


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a = b
        b = a + b

fib = fibonacci()

count = 0

targets = [5, 200, 1000, 100000]
results = {}

for num in fib:
    count += 1
    if count in targets:
        results[count] = num
        if len(results) == len(targets):
            break

print("5-е число Фибоначчи:", results[5])
print("200-е число Фибоначчи:", results[200])
print("1000-е число Фибоначчи:", results[1000])
print("100000-е число Фибоначчи:", results[100000])
