def next_simple(simple_list):
    for number in range(simple_list[-1], simple_list[-1]+1000000, 2):
        for div in simple_list:
            if number % div == 0:
                break
        else:
            return number


n = int(input())
simple = [2, 3]
ds = []
d = 2
while d <= n:
    if n % d == 0:
        ds += [d]
        n //= d
    else:
        d += 1
ds.sort()

x = 1
pows = []
while len(ds) > 0:
    cur_pow = ds.pop()
    p = [simple[i]**(pows[i]*(cur_pow-1)) for i in range(len(pows))]
    p += [simple[len(pows)]**(cur_pow-1)]
    ind = p.index(min(p))
    x *= p[ind]
    if ind == len(pows):
        pows += [cur_pow]
    else:
        pows[ind] *= cur_pow
    if len(simple) == len(pows):
        simple += [next_simple(simple)]
print(x, simple[len(pows) - 1])