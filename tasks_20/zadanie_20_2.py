x = int(input())
a = 0
b = 10

while x > 0:
    d = x % 9
    if d > a:
        a = d
    if d < b:
        b = d
    x = x // 9
print(a * b)