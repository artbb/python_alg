"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в
диапазоне от 2 до 9. Примечание: 8 разных ответов.
"""
data = [2, 3, 4, 5, 6, 7, 8, 9]
data_k = []
for i in data:
    k = 0
    for n in range(2, 100):
        if n % i == 0:
            k += 1
    data_k.append(k)

for i in data:
    print(f'от 2 до 99 кратны {i} - {data_k[data.index(i)]}')
