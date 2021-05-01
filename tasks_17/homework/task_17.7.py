"""
Рассматривается множество целых чисел, принадлежащих числовому отрезку [1000; 9999],
запись которых в пятеричной системе имеет не менее 6 цифр и заканчивается на 21 или 23.
Найдите количество таких чисел и минимальное из них.
"""
counter = 0

for i in range(9999, 1000 + 1, -1):
    number = i
    fivefold = ''
    while number > 0:
        fivefold = str(number % 5) + fivefold
        number //= 5
    if len(fivefold) >= 6:
        if (fivefold[-1] == '1' or fivefold[-1] == '3') and fivefold[-2] == '2':
            counter += 1
            mx = i

print(counter, mx)
