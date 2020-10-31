N: int = 5348
count = 0
md = 10
while N > 0:
    digit = N % 10
    if digit < md:
        md = digit = 0
    count += 1
    N = N // 10
print(count)
print(md)
