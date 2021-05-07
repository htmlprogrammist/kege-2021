f = open('../Bariants/statgrad-ov-04-29/26.txt')
n = int(f.readline())
c = []
for i in range(n):
    c.append(int(f.readline()))

k = 0
max_s = 0

c.sort()
for i in range(n - 1):
    if c[i] % 2 == 0:
        l = i + 1
        for j in range(i + 1, n):
            if c[j] % 2 != 0:
                continue
            b = (c[i] + c[j]) // 2
            while c[l] < b:
                l += 1
            if c[l] == b:
                k += 1
                max_s = b
print(k, max_s)
