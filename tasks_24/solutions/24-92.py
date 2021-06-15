# Автор: В.Н. Шубинкин

with open('24-1.txt') as inp:
    s = inp.read().strip()

strnum = '' # strnum накапливает строковое представление числа
maxim = 0 # максимальное подходящее число
odds = {str(2 * i + 1) for i in range(4)} # множество символов, являющихся нечётными цифрами
# odds = {'1', '3', '5', '7', '9'}
for sym in s:
    if sym.isdigit(): # проверка на цифру, иначе '0' <= sym <= '9'
        strnum += sym # добавляем очередную цифру в число
    elif strnum: # если встретилась не цифра, а strnum не пустая строка
        num = int(strnum)
        print(num)
        # чтобы проверить, что в числе все цифры чётные,
        # рассмотрим пересечение множества нечётных цифр и цифр числа
        if not bool(odds & set(strnum)) and num > maxim:
            maxim = num
        strnum = '' # сбрасываем на начальное значение, чтобы накапливать новое число
# проверка на случай, если самое большое подходящее число в самом конце строки
if s[-1].isdigit() and bool(odds & set(strnum)) and num > maxim:
    maxim = num
print(maxim)
