document = open('24/24_6.txt', 'r')
print(document)
content_in_lines = document.readlines()
print(content_in_lines)
counter = 0
# a = document.read()
# arr = []
# b = document.readline()
# c = document.readlines()
# for i in range(1000):
#     string = document.readline(i)
#     arr.append(string)
for line in content_in_lines:
    counter_X = 0
    counter_S = 0
    for i in range(len(line)):
        if line[i] == 'S':
            counter_S += 1
    for i in range(len(line)):
        if line[i] == 'X':
            counter_X += 1
    if counter_S == counter_X:
        counter += 1
# print('Counter =>', counter)  - тысяча строк - совпало.
# print(b)
# print(c)
# print(arr)
print(counter)

# Тоже правильное решение, но with взят из интернета
# counter = 0
#
# with open('24/24_6.txt') as file:
#     for line in file:
#         counter_X = 0
#         counter_S = 0
#         for i in range(len(line)):
#             if line[i] == 'S':
#                 counter_S += 1
#         for i in range(len(line)):
#             if line[i] == 'X':
#                 counter_X += 1
#         if counter_S == counter_X:
#             counter += 1
#
# print(counter)  # 48
