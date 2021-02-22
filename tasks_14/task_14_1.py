x = 81**5 + 3**30 - 27
counter = 0

while x > 0:
    if x % 9 == 8:
        counter += 1
    x //= 9

print(counter)
