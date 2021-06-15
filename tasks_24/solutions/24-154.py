# Автор: А. Кабанов

f = open('24-153.txt')
s = f.readline()

c = 0
m = 1000000

flag = 0
for i in range(len(s)):
    if s[i]=='D':
        flag = 1
        if c>0:
            m = min(m, c+2)
            c = 0
    if s[i]!='D' and flag:
        c+=1
print(m)
