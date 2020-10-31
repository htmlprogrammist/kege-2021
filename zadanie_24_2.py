document = open("24_2.txt")
content = document.read()
i = 0
k = 0
while i < len(content)-1:
    if content[i] == 'T' and content[i+1] == 'O' and content[i+2] == 'K':
        k += 1
        # print(content[i], content[i+1], content[i+2])
    if content[i] == 'T' and content[i+1] == 'I' and content[i+2] == 'K':
        k += 1
    i += 1
print(k)
