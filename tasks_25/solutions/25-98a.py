# Автор: teru

cubes = []
for i in range(3,70,2):
    cubes.append(i**3)
for i in range(228224, 531135+1):
   k=0
   maxx = 0
   for j in cubes:
       if i%j==0 and i!=j:
           k+=1
           maxx = j
   if k>=4:
       print(i,k,maxx)