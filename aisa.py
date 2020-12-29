"""
Формат ввода:
Вводятся два числа - n и m - количество строк в списке и количество элементов в строке.
Затем вводятся строки из m чисел через пробел.
Формат вывода:
Вывести словарь, в котором ключи - это числа, имеющиеся в матрице,
а значения - список из двух кортежей: индексы строк, в которых встречается это число,
и индексы столбцов, все в порядке возрастания без повторений.
Example:
stdin:
4
5
-1 3 7 8 0
7 8 -1 3 1
1 3 0 8 3
0 1 3 7 -1
stdout:
{-1: [(0, 1, 3), (0, 2, 4)], 3: [(0, 1, 2, 3), (1, 2, 3, 4)], 7: [(0, 1, 3), (0, 2, 3)], 8: [(0, 1, 2), (1, 3)], 0: [(0, 2, 3), (0, 2, 4)], 1: [(1, 2, 3), (0, 1, 4)]}
"""
n = int(input())  # количество строк в списке
m = int(input())  # количество элементов в строке
array = []
itie = []
jtie = []
result = []
x = 0
y = 0
for i in range(n):
    array.append([int(i) for i in input('Введите строку из {} чисел: '.format(m)).split()])
# print(array)

while y <= len(array):
    current_list_item = array[x][y]
    itie = []
    jtie = []
    result = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            # print(array[i][j])
            if array[i][j] == current_list_item:
                itie.append(i)
                jtie.append(j)
    result.append(tuple(itie))
    result.append(tuple(jtie))
    y += 1
    print({current_list_item: result})
