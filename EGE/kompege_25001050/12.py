"""
Задание 12 (№877).
Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки символов.
заменить (v, w)
нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w.
Если цепочки v в строке нет, эта команда не изменяет строку.
Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для Редактора:
Известно, что исходная строка содержала более 100 единиц
и не содержала других цифр.
Укажите минимально возможную длину исходной строки,
при которой в результате работы этой программы получится строка,
содержащая минимально возможное количество единиц.
"""

array = []
min_len = 1000
min_len_index = 0

for i in range(100, 1000):
    s = i * '1'
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('2222', '333', 1)
        s = s.replace('33', '1', 1)
    array.append(s.count('1'))

for j in range(len(array)):
    if array[j] < min_len:
        min_len = array[j]
        min_len_index = j
print(min_len_index + 100)
