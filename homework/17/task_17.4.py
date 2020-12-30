"""
Рассматривается множество целых чисел, принадлежащих числовому отрезку [8800; 55535], которые удовлетворяют следующим условиям:
− произведение разрядов больше 35;
− один из разрядов равен 7.
Найдите наибольшее из таких чисел и их количество.
Для выполнения этого задания можно написать программу или воспользоваться редактором электронных таблиц. 
"""
counter = 0

for i in range(8800, 55535 + 1):
    number = i
    seven = False
    multiplication = 1
    while number > 0:
        number_last = number % 10
        if number_last == 7:
            seven = True
        multiplication *= number_last
        number //= 10
    if seven and multiplication > 35:
        counter += 1
        mx = i
print(mx, counter)
