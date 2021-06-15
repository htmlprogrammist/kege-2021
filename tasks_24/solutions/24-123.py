# Автор: В.Н. Шубинкин

with open('24-1.txt') as f:
    s = f.read().strip()


maxlen = 0
pos = 0
for i in range(1, len(s) - 1):
    if s[i - 1] < s[i] > s[i + 1]:
        if pos == 0:
            pos = i
        else:
            maxlen = max(maxlen, i - pos)
            pos = i
print(maxlen)
