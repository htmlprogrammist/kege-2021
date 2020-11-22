import math

dividers = []

for i in range(135790, 163228 + 1):
    dividers = []
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)
    if sum(dividers) > 460000:
        print(len(dividers), sum(dividers))
