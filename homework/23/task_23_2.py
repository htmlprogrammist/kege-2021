"""
Задание 23 (№278).
У исполнителя Калькулятор две команды, которым присвоены номера:
1. прибавь 1
2. увеличь число десятков на 1
Например: при помощи команды 2 число 23 преобразуется в 33. 
Если перед выполнением команды 2 вторая с конца цифра равна 9, она не изменяется.
Сколько есть программ, которые число 10 преобразуют в число 33? 
"""

k = [0] * (33 + 1)
k[3] = 1


def increase_the_number_of_dozens(number):
    if number // 10 == 9:  # по условию
        pass  # Но, учитывая диапозон с 10 по 33, это вообще не нужно
    else:
        dozen_in = number // 10
        dozen_out = dozen_in + 1
    return dozen_out * 10 + number % 10


for n in range(10, 33 + 1):
    if n + 1 <= 33:
        k[n + 1] = k[n]
    intermediate_result = increase_the_number_of_dozens(n)
    print(intermediate_result)
    if intermediate_result <= 33:
        k[intermediate_result] = k[n]

print(k[33])  # 0 => надо пофиксить
