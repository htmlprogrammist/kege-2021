# Автор: В.Н. Шубинкин

with open('24-1.txt') as inp:
    s = inp.read().strip()

strnum = '' # strnum накапливает строковое представление числа
maxim = 0 # максимальное подходящее число
evens = {str(2 * i) for i in range(4)} # множество символов, являющихся чётными цифрами
# evens = {'0', '2', '4', '6', '8'}
for sym in s:
    if sym.isdigit(): # проверка на цифру, иначе '0' <= sym <= '9'
        strnum += sym # добавляем очередную цифру в число
    elif strnum: # если встретилась не цифра, а strnum не пустая строка...
        num = int(strnum)
        # чтобы проверить, что в числе все цифры нечётные,
        # рассмотрим пересечение множества чётных цифр и цифр числа
        if not bool(evens & set(strnum)) and num > maxim:
            maxim = num
        strnum = '' # сбрасываем на начальное значение, чтобы накапливать новое число
# проверка на случай, если самое большое подходящее число в самом конце строки
if s[-1].isdigit() and bool(evens & set(strnum)) and num > maxim:
    maxim = num
print(maxim)
