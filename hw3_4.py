"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random

data = [random.randint(0, 5) for x in range(8)]
print('Случайный массив ', data)
data1 = []
for i in data:
    k = data.count(i)
    data1.append(k)
data2 = [i for i in data if data.count(i) == max(data1)]
print(f'Наиболее часто встречаются числа(о) {list(set(data2))} - {max(data1)} раз(а)')
