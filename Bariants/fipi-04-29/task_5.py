"""
Задание 5 (№1285).
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи числа N, и остаток от деления суммы на 2 дописывается в конец числа (справа).
Например, запись 11100 преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы её цифр на 2.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R.
Укажите минимальное число R, которое превышает число 396 и может являться результатом работы данного алгоритма.
В ответе это число запишите в десятичной системе счисления.

402
"""
for n in range(2, 256):
    binary = bin(n)[2:]
    summa = 0
    for symbol in binary:
        summa += int(symbol)
    binary += str(summa % 2)

    summa = 0
    for symbol in binary:
        summa += int(symbol)
    binary += str(summa % 2)

    if int(binary, 2) > 396:
        # ~~print(n)~~
        print(int(binary, 2))
        break
# надо было указать минимальное число R, а не минимальное число N... ну хоть раз ты прочитай условие, а
