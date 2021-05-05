"""
Назовём натуральное число подходящим, если у него ровно 3 различных
простых делителя. Например, число 180 подходящее (его простые делители –
2, 3 и 5), а число 12 – нет (у него только два различных простых делителя).
Определите количество подходящих чисел, принадлежащих отрезку
[10 001; 50 000], а также наименьшее из таких чисел. В ответе запишите
два целых числа: сначала количество, затем наименьшее число.
"""
counter = 0
min_i = 0

for i in range(50000, 10000, -1):
    counter_del = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            simple = True
            for k in range(2, j // 2 + 1):
                if j % k == 0:
                    simple = False
            if simple:
                counter_del += 1
                if counter_del > 4:
                    break
    if counter_del == 3:
        min_i = i
        counter += 1

print(counter, min_i)