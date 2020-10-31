A = [2, 1, 1, 2, 2, 3, 8, 9, 6, 2]
j = 9
print('A[j]=', A[j], 'A[j-1]=', A[j-1])
while A[j] + A[j-1] > 4:
    A[j], A[j-1] = A[j-1], A[j]
    j-=1
    print('A[j]=', A[j], 'A[j-1]=', A[j-1])
print(j)
print('==================')
A = [0, 7, 1, 3, 2, 1, 8, 9, 6, 3]
j = 9
print('A[j]=', A[j], 'A[j-1]=', A[j-1])
while A[j] + A[j-1] > 4:
    A[j], A[j-1] = A[j-1], A[j]
    j-=1
    print('A[j]=', A[j], 'A[j-1]=', A[j-1])
print(j)

