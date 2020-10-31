document = open('24/24_324.txt')
a = document.read()
k = 0
max_k = 0
current_word = ''
b = []

for i in range(len(a)):
    if a[i].isdigit():
        if current_word != '':
            k = len(current_word)
            if max_k < k:
                max_k = k
            b.append(current_word)
        current_word = ''
    else:
        current_word += a[i]
print(max_k)  # 587
print(b)
