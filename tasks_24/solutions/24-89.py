# Автор: В.Н. Шубинкин

with open('24-1.txt') as inp:
    s = inp.read().strip()

strnum = '' # strnum накапливает строковое представление числа
maxim = 0 # максимальное чётное число
for sym in s:
    if sym.isdigit(): # проверка на цифру, иначе '0' <= sym <= '9'
        strnum += sym # добавляем очередную цифру в число
    elif strnum: # если встретилась не цифра, а strnum не пустая строка...
        num = int(strnum)
        # ... проверяем на чётность и сравниваем с максимумом
        if num % 2 == 0 and num > maxim:
            maxim = num
        strnum = '' # сбрасываем на начальное значение, чтобы накапливать новое число
# проверка на случай, если самое большое чётное в самом конце строки
if s[-1].isdigit() and num % 2 == 0 and num > maxim:
    maxim = num
print(maxim)
