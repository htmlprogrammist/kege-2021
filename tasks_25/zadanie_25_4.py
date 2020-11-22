# кратен 5 7 13 и не кратен хотя бы одному из квадратов этого числа, делитель не превышающий 100000
# делитель не может быть единицей или самим собой и делитель оканчивается на 19
array1 = []  # Числа из основного диапозона
i = 0
divider = 2
max_divider = 100000
array2 = []  # Числа после фильтрации по условию. Теперь с этими числами нужно работать.
array3 = []  #
# divider = 1

# for i in range(224466, 664422+1):
#     array1.append(i)
# print(array1)

for j in range(224466, 664422+1):
    if j % 5 == 0 and j % 7 == 0 and j % 13 == 0 and (j % 25 != 0 or j % 49 != 0 or j % 169 != 0):
        array1.append(j)

# print(array1)
# print(len(array1))  965
# print(len(array2)) 611
# divider = max(array1)
# while i < len(array1):
#     array2.append(array1[i] / divider)
#     i += 1
# print(array2)
while i < len(array1):
    # if divider < max_divider:
    #     result = round(array1[i] / divider)
    #     array2.append(result)
    #     divider += 1
    while divider < max_divider:
        result = round(array1[i] / divider)
        array2.append(result)
        divider += 1
    i += 1
array2 = list(set(array2))
print(max(array2))
# print(len(array2))  # 965, совпало с len(array1)

for k in range(len(array2)):
    if array2[k] % 100 == 19:
        array3.append(array2[k])
        # if k == 0:
        #     array3.append(array2[k])
        # else:
        #     if array2[k] != array3[k-1]:
        #         array3.append(array2[k])
array3 = list(set(array3))
print(array3)
