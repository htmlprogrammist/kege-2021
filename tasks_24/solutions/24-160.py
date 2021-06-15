ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open("24-s1.txt") as F:
  data = F.readlines()
  minK = 10**10
  for s in data:
    k = s.count('A')
    if k < minK:
      minK = k
      ma, letterMax = 0, ''
      for letter in ABC:
        cnt = s.count(letter)
        if cnt >= ma:
          ma, letterMax = cnt, letter

print( letterMax,
       sum(s.count(letterMax) for s in data) )