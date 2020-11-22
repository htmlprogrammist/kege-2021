x = int(input())
a = 0
b = 0
while x > 0:
    a += 1
    b += (x % 10)*(x % 10)
    x = x//10
print(a, b)
