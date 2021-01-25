# Макс d, при котором выведет 46

d = int(input())
n = 8
s = 78
while s <= 1200:
    s += d
    n += 2
print(n)  # 46

stdin = 1
answer_n = 46
answers = []
while stdin < 1000:
    d = stdin
    n = 8
    s = 78
    while s <= 1200:
        s += d
        n += 2
    if n == answer_n:
        answers.append(stdin)
    stdin += 1
    print(1)

print(answers)
print(max(answers))
