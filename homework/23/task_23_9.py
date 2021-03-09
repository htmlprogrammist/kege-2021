"""
№ 586, Джобс 26.10.2020
Исполнитель Простачок преобразует число, записанное на экране.
У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 2
2. Прибавить 3
3. Умножить на 2
Первая команда увеличивает число на 2, вторая – на 3,
третья – увеличивает число вдвое.
Сколько чисел может быть результатом работы алгоритма для входного значения 10,
если известно, что в алгоритме 5 команд?

83
"""
list_of_all_numbers = []
range_tuple = 1, 2, 3
initial_number = 10


def command(number, cmd):
    if cmd == 1:
        return number + 2
    if cmd == 2:
        return number + 3
    if cmd == 3:
        return number * 2


for n1 in range_tuple:
    out1 = command(initial_number, n1)
    for n2 in range_tuple:
        out2 = command(out1, n2)
        for n3 in range_tuple:
            out3 = command(out2, n3)
            for n4 in range_tuple:
                out4 = command(out3, n4)
                for n5 in range_tuple:
                    out5 = command(out4, n5)
                    list_of_all_numbers.append(out5)


print(len(set(list_of_all_numbers)))
