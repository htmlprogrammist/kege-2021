"""
Рассматривается множество целых чисел, принадлежащих числовому отрезку [246815; 875621], 
которые удовлетворяют следующим условиям:
− третья и четвертая цифры образуют число меньшее 50;
− число, составленное из трех старших разрядов, имеет остаток от деления на 5 такой же, 
как число, составленное из младших трех разрядов.
Найдите наибольшее из таких чисел и их количество.
Для выполнения этого задания можно написать программу или воспользоваться редактором электронных таблиц. 
"""
counter = 0

for i in range(246815, 875621 + 1):
    if i % 100 < 50:
        if ((i // 1000) % 5) == ((i % 1000) % 5):
            counter += 1
            mx = i

print(mx, counter)