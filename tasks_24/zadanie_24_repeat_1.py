document = open('24/24_21.txt')
a = document.read()
k = 1
max_k = 1

for i in range(len(a)-1):
    if a[i] != a[i+1]:
        k += 1
        if max_k < k:
            max_k = k
    else:
        k = 1

print(max_k)
# Не с первого раза, забыл k = 0, а надо k = 1
