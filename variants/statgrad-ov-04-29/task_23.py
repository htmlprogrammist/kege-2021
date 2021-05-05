"""
Исполнитель преобразует число на экране.
У исполнителя есть две команды, которым присвоены номера:
 1. Удвоить
 2. Удвоить и прибавить
Первая команда умножает число на экране на 2, вторая – умножает его на 2, а затем прибавляет 1.

Программа для исполнителя – это последовательность команд.
Например, программа 121 при исходном числе 3 последовательно получит числа 6, 13 и 26.
Результатом программы будет число 26.
Сколько различных результатов можно получить из исходного числа 1 после выполнения программы,
содержащей ровно 9 команд?
"""
list_of_all_number = []
range_tuple = 1, 2
initial_number = 1


def command(number, cmd):
    if cmd == 1:
        return number * 2
    if cmd == 2:
        return number * 2 + 1


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
                    for n6 in range_tuple:
                        out6 = command(out5, n6)
                        for n7 in range_tuple:
                            out7 = command(out6, n7)
                            for n8 in range_tuple:
                                out8 = command(out7, n8)
                                for n9 in range_tuple:
                                    out9 = command(out8, n9)
                                    list_of_all_number.append(out9)
# for n1 in range_tuple:
#     out1 = command(initial_number, n1)
#     print(initial_number, n1, command(initial_number, n1), out1)
#     list_of_all_number.append(out1)

print(len(set(list_of_all_number)))
