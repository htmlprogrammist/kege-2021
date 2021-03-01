N = int(input())
f = [0] * (N + 1)  # Будем игнорировать число с нулевым индексом
f[1] = f[2] = 1  # Мы знаем, что это будут первые две единицы
for i in range(3, N + 1):
    f[i] = f[i - 1] + f[i - 2]  # Рекуррентная формула
print(f[N])
