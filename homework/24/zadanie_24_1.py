document = open('24_322.txt')
content = document.read()
k = 0
i = 0

while i < len(content)-3:
    if content[i].isdigit():
        if not content[i+1].isdigit():
            if not content[i + 2].isdigit():
                if not content[i + 3].isdigit():
                    if not content[i + 4].isdigit():
                        if content[i + 5].isdigit():
                            k += 1
    i += 1
print(k)
