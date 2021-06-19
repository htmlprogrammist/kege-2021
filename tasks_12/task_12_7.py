# 20 цифр 1, 30 цифр 2, 40 цифр 3
s = '32' * 30 + '31' * 10 + '1' * 10
# print(s)
# print(s.count('1'), s.count('2'), s.count('3'))  # всё верно
while '32' in s or '31' in s:
    if '32' in s:
        s = s.replace('32', '311', 1)
    else:
        s = s.replace('31', '11', 1)

print(s.count('1'))  # 120
