"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
Пожелание преподавателя: без использования мин и макс
"""
import random

data1 = [random.randint(-50, 50) for x in range(10)]
print('Исходный ряд', data1)
data2 = sorted(data1)
ind_min = data1.index(data2[0])
ind_max = data1.index(data2[len(data2) - 1])
data3 = []
for i in data1:
    if data1.index(i) != ind_min and data1.index(i) != ind_max:
        data3.append(i)
    elif data1.index(i) == ind_min:
        data3.append(data2[len(data2) - 1])
    elif data1.index(i) == ind_max:
        data3.append(data2[0])
print(f'Минимальное число: {data2[0]}\nМаксимальное число: {data2[len(data2) - 1]}')
print('Ряд с заменой', data3)
