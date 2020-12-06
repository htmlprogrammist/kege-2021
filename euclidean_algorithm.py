# Алгоритм Евклида - находим общий делитель
number1 = int(input())
number2 = int(input())

while number1 != number2:
    if number1 > number2:
        number1 = number1 - number2
    else:
        number2 -= number1
print(number1)
