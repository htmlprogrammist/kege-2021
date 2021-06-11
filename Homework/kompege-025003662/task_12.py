"""
Задание 12 (№1367).
Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки символов. заменить (v, w)
нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w.
Если цепочки v в строке нет, эта команда не изменяет строку.
Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.

На выполнение Редактору дана следующая программа:
     ПОКА нашлось(42) или нашлось(32)
           ЕСЛИ нашлось(42)
           ТО заменить(42, 51)
   ИНАЧЕ заменить(32, 61)
 КОНЕЦ ПОКА

На вход программе подана строка, содержащая только 20 двоек, 15 троек и 10 четверок. Порядок символов заранее неизвестен.
Определите максимально возможную сумму всех цифр в конечной строке.

155
"""
summa = 0
# s = 15 * '3' + 20 * '2' + '4' * 10  # 127
# s = '4' * 10 + 15 * '3' + 20 * '2'  # 127
# s = + 15 * '3' + 15 * '2' + '4' * 10 + 5 * '2'  # 127
s = '32' * 15 + '42' * 5 + '4' * 5
while '42' in s or '32' in s:
    if '42' in s:
        s = s.replace('42', '51', 1)
    else:
        s = s.replace('32', '61', 1)

for symbol in s:
    summa += int(symbol)
print(summa)
