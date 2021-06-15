# Автор: А. Кабанов

f = open('24-153.txt')
s = f.readline()

s = '.' + s + '.'  # добавляем граничные символы

c = 0
m = 1000000

for i in range(len(s)):
    if s[i]=='D':
        c+=1
    elif c>0:
        m = min(c,m)
        c = 0
print(m)
