# Автор В.Н. Шубинкин
# видеоразбор аналогичной задачи https://youtu.be/9rxY2O-aClI

start = 55000000
end = 60000000
primes = [2]
for i in range(3, int(end**0.25) + 1, 2):
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            break
    else:
        primes.append(i)

ans = []

for el in primes[1:]:
    num = el**4
    if start <= num <= end:
        ans.append([num, num])
    else:
        while num <= end:
            if num >= start:
                ans.append([num, el**4])
            num *= 2

print(*sorted(ans), sep='\n')
