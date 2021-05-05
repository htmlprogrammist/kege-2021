counter = 0
min_i = 0

for i in range(90000, 50001 - 1, -1):
    counter_del = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            simple = True
            for k in range(2, j // 2 + 1):
                if j % k == 0:
                    simple = False
            if simple:
                counter_del += 1
    if counter_del == 3:
        min_i = i
        counter += 1

print(counter, min_i)
