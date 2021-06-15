# Автор: А. Кабанов

f = open('24-153.txt')
s = f.readline()

c = 0
m = 1000000

flag = 0

for i in range(len(s)-1):
    if s[i]=='A':
        c = 0
        for j in range(i+1,len(s)):
            if s[j]!='F': c+=1
            elif c==0: c+=1
            else:
                m = min(c+2,m)
                break

print(m)
            
