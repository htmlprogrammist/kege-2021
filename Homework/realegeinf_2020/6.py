mr = 0

for n in range(3, 200):
    binary = bin(n)[2:]
    if n % 2 == 0:
        binary += '10'
    else:
        binary += '01'
    r = int(binary, 2)
    if r < 109:
        mr = r
print(mr)
