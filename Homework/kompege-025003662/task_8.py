counter = 0

for i in range(5 ** 5 + 1, 5 ** 6, 2):
    number = i
    fifth = ''
    while number > 0:
        fifth = str(number % 5) + fifth
        number //= 5
    if fifth[0] == '3':
        counter += 1
    # print(fifth)
    # input()
    # counter += 1  # всего чисел
print(counter)
