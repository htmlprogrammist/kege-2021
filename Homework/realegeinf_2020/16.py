x = 16 ** 8 * 4 ** 20 - 4 ** 5 - 64
counter = 0
while x > 0:
    if x % 4 == 3:
        counter += 1
    x //= 4
print(counter)
