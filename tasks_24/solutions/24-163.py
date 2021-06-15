ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open("24-s1.txt") as F:
  data = F.readlines()
  maxK = 0
  for s in data:
    k = 0
    for i in range(len(s)-1):
      if ord(s[i])+1 == ord(s[i+1]):
        #print(s[i]+s[i+1])
        k += 1
    if k >= maxK:
      maxK = k
      mi, letterMin = 10**10, ''
      for letter in ABC:
        cnt = s.count(letter)
        if cnt > 0 and cnt < mi:
          mi, letterMin = cnt, letter

print( letterMin,
       sum(s.count(letterMin) for s in data) )