"""
Как я понял, здесь надо найти наименьшее четное среди всего документа. Нашёл. Ответ сошёлся: 888.
29.11.2020
"""

document = open('24_321.txt')
a = document.read()
current_number = ''
b = []
result = 999999

for i in range(len(a)):
    if a[i].isdigit():
        current_number += a[i]
    else:
        if current_number != '':
            b.append(int(current_number))
            if int(current_number) < result:
                if int(current_number) % 2 == 0:
                    result = int(current_number)
        current_number = ''

print(b)
print(result)  # 888
