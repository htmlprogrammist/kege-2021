# какая-то ошибка, не сходится ответ :(
f = open('txt/task_26_1.txt')
s, n = map(int, f.readline().split())
a = []
for _ in range(n):
    a.append(int(f.readline()))
a.sort()

summa = 0
counter = 0
mx = 0

for i in range(n):
    """
    если текущая сумма и следующий объем не превышает
    свободное место, то суммируем такой объем, запоминаем макс объем
    и считаем кол-во пользователей
    """
    if summa + a[i] <= s:
        counter += 1
        mx = a[i]
    else:
        # превысили объем, поэтому вычитаем последний учтенный объем (Max)
        summa = summa - mx + a[i]
        if s >= summa:  # запоминаем новый максимум
            mx = a[i]
print(counter, mx)
