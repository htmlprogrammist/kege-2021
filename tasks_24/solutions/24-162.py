ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open("24-s1.txt") as F:
  data = F.readlines()
  minK = 10**10
  for s in data:
    k = 0
    for i in range(len(s)-1):
      if ord(s[i])+1 == ord(s[i+1]):
        #print(s[i]+s[i+1])
        k += 1
    if k > 0 and k < minK:
      minK = k
      ma, letterMax = 0, ''
      for letter in ABC:
        cnt = s.count(letter)
        if cnt >= ma:
          ma, letterMax = cnt, letter

print( letterMax,
       sum(s.count(letterMax) for s in data) )

