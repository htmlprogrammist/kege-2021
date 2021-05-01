document = open('24_321.txt')
a = document.read()
current_number = ''
b = []
result = 9999999

for i in range(len(a)):
    if a[i].isdigit():
        current_number += a[i]
    else:
        if current_number != '':
            if int(current_number) % 2 == 0:
                if int(current_number) < result:
                    result = int(current_number)
        current_number = ''
print(result)  # 888
