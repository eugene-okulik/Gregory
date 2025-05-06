temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

high_temperature = list(filter(lambda t: t >= 28, temperatures))
print(min(high_temperature))
print(max(high_temperature))
avg_temp = sum(high_temperature) / len(high_temperature)
print(avg_temp)
