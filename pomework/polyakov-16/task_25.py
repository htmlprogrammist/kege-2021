"""
(№ 2577) Напишите программу, которая ищет среди целых чисел,
принадлежащих числовому отрезку [1820348; 2880927], числа, имеющие ровно 5 различных делителей.
В ответе для каждого найденного числа запишите два его наибольших делителя в порядке возрастания.

50653 1874161
68921 2825761
"""
# Поскольку само число и 1 тоже делители, то максимальный делитель - само число, поэтому вывожу i
import math

answers = []

for i in range(1820348, 2880927 + 1):
    counter = 0
    max_d = 0
    pre_max_d = 0
    if math.sqrt(i).is_integer():
        counter += 1
    for j in range(1, int(math.sqrt(i))):
        if i % j == 0:
            counter += 2
        if counter > 5:
            break
    if counter == 5:
        answers.append(i)


for number in answers:
    for j in range(2, int(math.sqrt(number))):
        if number % j == 0:
            print(number // j, number)
            break
