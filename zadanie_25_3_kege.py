array = []
# print(134689-81234)  # 53455
for i in range(81234, 134689+1):
    array.append(i)
print(array)
# print(len(array))  # 53455

for j in range(len(array)):
    if array[j] % j == 0:
