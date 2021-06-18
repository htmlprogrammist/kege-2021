"""
Вася составляет 4-буквенные коды из букв У, Л, Е, Й. Каждую букву нужно использовать ровно 1 раз,
при этом код не может начинаться с буквы Й и не может содержать сочетания ЕУ.
Сколько различных кодов может составить Вася?
"""
s = 'УЛЕЙ'
counter = 0

for a in s[:3]:
    for b in s:
        for c in s:
            for d in s:
                st = a + b + c + d
                flag = True
                for x in st:
                    if st.count(x) != 1:
                        flag = False
                if flag:
                    if st.count('ЕУ') == 0:
                        counter += 1
print(counter)
