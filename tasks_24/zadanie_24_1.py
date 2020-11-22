document = open("24.txt")
# print(document.read())
content = document.read()
# print(content_splitted) => success
i = 0
k = 1
max_k = 1
while i < len(content)-1:
    if content[i] == content[i+1]:
        k += 1
        if k > max_k:
            max_k = k
    else:
        k = 1
    i += 1
print('Максимальное количество подряд идущих одинаковых букв =', max_k)
