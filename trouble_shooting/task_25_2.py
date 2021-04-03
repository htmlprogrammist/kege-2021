"""
Задание 25 (№224).
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [228224; 531135], 
числа, среди делителей которых есть хотя бы 4 различных куба натуральных нечетных чисел. 
Для каждого найденного числа запишите количество таких делителей и наибольший из них. 
В качестве делителей не рассматривать число 1. Так, например, для числа 8 учитываются только делители 2 и 4.
Например, для числа 54 имеем следующие делители 2, 3, 6, 9, 18, 27. 
Следовательно для него необходимо вывести два числа: 1 27

5 250047
5 91125
5 91125
5 421875
5 91125
5 250047
"""
import math

for i in range(228224, 531135 + 1):
    dividers = []
    # counter = 0  счётчик количества делителей, потому что вообще не понятно, что не так (1)
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            cube_j1 = j ** (1/3)
            cube_j2 = (i // j) ** (1/3)
            # print(cube_j1, cube_j2)
            # if j % 2 != 0 and (i // j) % 2 != 0:
            #     if cube_j1.is_integer() and cube_j2.is_integer():
            #         dividers.append(j)
            #         dividers.append(i // j)
            if j % 2 != 0:
                if cube_j1.is_integer():
                    dividers.append(j)
                    # counter += 1
            if (i // j) % 2 != 0:
                if cube_j2.is_integer():
                    dividers.append(i // j)
                    # counter += 1
    # if counter > 2:  (1) выдаёт он в итоге только либо 1, либо 2
    #     print(counter)
    if len(dividers) >= 4:
        print(len(dividers), max(dividers))