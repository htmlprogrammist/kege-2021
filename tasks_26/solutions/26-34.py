with open("26-j6.txt") as F:
  n = int(F.readline())
  data = []
  for i in range(n):
    data.append( int(F.readline()) )

V = sum(data)*0.9

# не сжимаем самые маленькие файлы

data.sort()
sum0 = 0
sumCompressed = sum(data)
last0 = -1
max0 = -1
for i in range(n):
  if (sum0+data[i]) + (sumCompressed-data[i])*0.8 <= V:
    last0 = i
    sum0 += data[i]
    max0 = data[i]
    sumCompressed -= data[i]

# пробуем заменить последний файл на бОльший

sum0 -= data[last0]
sumCompressed += data[last0]
i = last0
while i < len(data) and (sum0+data[i]) + (sumCompressed-data[i])*0.8 <= V:
  max0 = data[i]
  i += 1

print( last0+1, max0 )

