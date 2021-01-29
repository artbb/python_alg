"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна
вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = []
while len(matrix) < 4:
    row = [input(f'Введите 4 цифры строки матрицы через пробел: ')]
    for i in row:
        i = i.split()
        matrix.append(i)

matrix_int = []
for row in matrix:
    try:
        int_row = [int(x) for x in row]
    except Exception:
        print('Ошибка! Введите 4 числа через пробел')
    matrix_int.append(int_row)

sum_itm = []
for j in range(0, len(matrix_int[0])):
    tmp = 0
    for i in range(0, len(matrix_int)):
        try:
            tmp = tmp + matrix_int[i][j]
        except Exception:
            print('Ошибка! Введите 4 числа через пробел')
    sum_itm.append(tmp)
matrix_int.append('-'*len(matrix_int[0]))
matrix_int.append(sum_itm)

for line in matrix_int:
    for item in line:
        print(f'{item:>3}', end ='')
    print()