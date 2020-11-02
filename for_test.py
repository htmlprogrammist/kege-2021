# i = 30
# counter1 = 0
# counter2 = 0
# even = []
# odd = []
# for j in range(2, i):
#     if i % j == 0:
#         if j % 2 == 0:
#             counter1 += 1
#             even.append(j)
#         else:
#             counter2 += 1
#             odd.append(j)
# print('Четный', counter1, even)
# print('Нечетный', counter2, odd)
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)