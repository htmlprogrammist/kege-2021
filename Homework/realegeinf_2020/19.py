A = [5, 43, 20, 7, 13, 7, 29, 13, 2, 33, 15, 5]
s = 0
for i in range(1, 12):
    if A[i - 1] // A[i] < 2:
        s += A[i]
    else:
        A[i] = A[i] * i
print(s)
