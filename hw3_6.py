"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
! Мин и макс могут быть в нескольких позициях
"""
import random

data1 = [random.randint(-5, 5) for x in range(5)]
print('Исходный ряд', data1)
data2 = sorted(data1)
ind_min = data1.index(data2[0])
ind_max = data1.index(data2[len(data2)-1])
data3 = []
for i in data1:
    if data1.index(i) != ind_min and data1.index(i) != ind_max:
        data3.append(i)
print(f'Максимальное число {data2[len(data2)-1]}\nМинимальное число {data2[0]}')
print('Сумма без экстремумов равна', sum(data3))