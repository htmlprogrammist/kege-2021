"""
записали в 7-ричной системе счисления. Сколько четных разрядов в такой записи?
При подсчете учитывать только значащие разряды.
"""
x = 5 * 7 ** 153 + 4 * 49 ** 85 - 3 * 7 ** 15
counter = 0

# number = x
# seventh = ''
# while number > 0:
#     seventh = str(number % 7) + seventh
#     number //= 7
# print(seventh)  # все разряды значащие, потому что первый из них - 4-ка
while x > 0:
    if (x % 7) % 2 == 0:
        counter += 1
    x //= 7
print(counter)
