"""
(№ 2217) Значение арифметического выражения: 9^8 + 3^24 – 18
записали в системе счисления с основанием 3. Сколько цифр «2» содержится в этой записи?

13
"""
x = 9 ** 8 + 3 ** 24 - 18
counter = 0

while x > 0:
    if x % 3 == 2:
        counter += 1
    x //= 3

print(counter)