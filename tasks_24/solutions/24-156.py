# Автор: А. Кабанов

f = open('24-153.txt')
s = f.readline()

k = 0
for j in range(7,10+1):
    for i in range(j-1,len(s)):
        if s[i]=='F' and s[i-(j-1)]=='A':
            k+=1
        
print(k)
