"""
Сколько существует различных символьных последовательностей длины 5
в четырёхбуквенном алфавите {A, C, G, T}, которые содержат ровно две буквы A?
"""
from itertools import product

counter = 0

for i in product('ACGT', repeat=5):
    if i.count('A') == 2:
        counter += 1

print(counter)
