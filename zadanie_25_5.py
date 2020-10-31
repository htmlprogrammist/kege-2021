counter1 = 0
counter2 = 0

for i in range(326496, 649632+1):
    for j in range(2, i//2):
        if i % j == 0:
            if j % 2 == 0:
                counter1 += 1
            else:
                counter2 += 1
    if counter1 == counter2 and counter1 >= 70:
        # for k in range()
        k = 1001
        while i % k != 0:
            k += 1
        print(i, k)

