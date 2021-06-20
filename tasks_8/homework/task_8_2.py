"""
Маша составляет 5-буквенные коды из букв В, У, А, Л, Ь. Каждую букву нужно использовать ровно 1 раз,
при этом код буква Ь не может стоять на первом месте и перед гласной. Сколько различных кодов может составить Маша?
"""
from itertools import product

p = product('ВУАЛЬ', repeat=5)
s = map(lambda x: "".join(x), p)
counter = 0

for i in s:
    if len(set(i)) == 5:
    # if i.count('В') == 1 and i.count('У') == 1 and i.count('А') == 1 and i.count('Л') == 1 and i.count('Ь') == 1:
        if i[0] != 'Ь' and i.count('ЬА') == 0 and i.count('ЬУ') == 0:
            counter += 1
print(counter)
