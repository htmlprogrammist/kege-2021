document = open('homework/24/24_324.txt')
a = document.read()
max_k = 0
current_word = ''

for i in range(len(a)):
    if a[i].isdigit():
        if current_word != '':
            if len(current_word) > max_k:
                max_k = len(current_word)
        current_word = ''
    else:
        current_word += a[i]

print(max_k)  # 587
