"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
если искомый элемент(ы) встречается в массиве несколько раз, используйте один любой по вашему выбору.
"""
import random

matrix = [[random.randint(-5, 5) for _ in range(4)] for _ in range(4)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end ='')
    print()

min_l = []
for j in range(0, len(matrix[0])):
    tmp = []
    for i in range(0, len(matrix)):
        tmp.append(matrix[i][j])
    min_l.append(min(tmp))
print(f'Минимальные элементы столбцов {min_l}.\nМаксимальный элемент среди минимальных {max(min_l)}', )
