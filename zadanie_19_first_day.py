#A = [5, 6, 5, 8, 5, 4, 1, 2, 9, 6]
#c = 0
#for i in range(0, 9):
#    if A[i] <= A[9]:
#        c+=1
#        t = A[i]
#        A[i] = A[9]
#        A[9] = t
# print(c)

A = [8, 3, 4, 7, 2, 2, 1, 2, 3, 0]
c = 0
for i in range(1, 10):
    if A[i] <= A[0]:
        c+=1
        t = A[i]
        A[i] = A[0]
        A[0] = t
print(c)
