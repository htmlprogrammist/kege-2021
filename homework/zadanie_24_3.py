document = open('24/24_321.txt')
a = document.read()
current_number = ''
b = []
result = 9999999

for i in range(len(a)):
    if a[i].isdigit():
        current_number += a[i]

    else:
        b.append(current_number)
        current_number = ''

print(b)
print(result)  # 888
