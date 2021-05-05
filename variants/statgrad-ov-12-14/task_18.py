"""
Дана последовательность вещественных чисел. Из неё необходимо выбрать несколько подряд идущих чисел так,
чтобы каждое следующее число отличалось от предыдущего не более чем на 8.
Какую максимальную сумму могут иметь выбранные числа?
В ответе запишите только целую часть максимально возможной суммы.
Исходная последовательность записана в виде одного столбца электронной таблицы.
"""

document = open('18-1-without-t-tabulation.txt')
content = document.read()
a = content.split('\n')
max_a = -8
for i in range(len(a) - 1):
    number1 = a[i].replace(',', '.')
    number2 = a[i + 1].replace(',', '.')
    if abs(float(number1)) - abs(float(number2)) <= 8:
        if max_a < float(number1) + float(number2):
            max_a = float(number1) + float(number2)
print(int(max_a))

