for i in range(224466, 664422+1):
    if i % 5 == 0 and i % 7 == 0 and i % 13 == 0:
        if i % 25 != 0 or i % 25 != 0 or i % 169 != 0:
            for j in range(2, i):
                if i % j == 0:
                    m = j
            if m <= 100000 and m % 100 == 19:
                print(i, m)
