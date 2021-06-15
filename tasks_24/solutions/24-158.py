with open('24-157.txt') as F:
  s = F.read().strip()

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = [0]*len(ABC)
for i in range(1,len(s)-1):
  if s[i] == s[i+1]:
    k = ABC.find( s[i-1] )
    count[k] += 1

maxCount = max(count)
ind = count.index(maxCount)
print( ABC[ind], maxCount )

