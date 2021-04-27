document = open("24/24.txt")
a = document.read()
k = 1
max_k = 1

for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        k += 1
    if k > max_k:
        max_k = k
        k = 1
print(max_k)
# То, что я наговнякал на ЕГЭ. Файл "task_24_1.py" - верный алгоритм. Эххх...
# Ну, надо пробник... учесть свои ошибки, всё такое
