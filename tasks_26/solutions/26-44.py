with open("26-44_.txt") as F:
   N = int(F.readline())
   data = []
   for i in range(N):
     data.append( int(F.readline()) )

data.sort()
last = 500
ma = 0
discount = 0
while data:
  chunk = [x for x in data if x <= last]
  if chunk:
    mid = len(chunk)//2
    if mid > 0:
      discount += sum(chunk[:mid])*0.5
      costMax = chunk[mid-1]*0.5
    data = data[len(chunk):]
  last+= 500

print( int(discount), int(costMax) )
