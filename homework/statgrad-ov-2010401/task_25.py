def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


for i in range(35000000, 40000000 + 1):
    a = i
    while a % 2 == 0:
        a //= 2
    if a ** 0.25 == int(a ** 0.25):
        if is_prime(a ** 0.25):
            print(i)
