document = open('24_314.txt')
content = document.read()
k = 0
i = 0

# Уточнить у Савра Владимировича, почему тут не важно, ставишь 2, или 3,
# или 4, всё равно нет ошибки, что выходит за диапозон
while i < len(content) - 2:
    if content[i] != 'S' and content[i + 1] != 'T' and content[i + 2] == 'O' and content[i + 3] == 'C' and content[
        i + 4] == 'K':
        k += 1
    i += 1
print(k)  # 5088 => 7626
