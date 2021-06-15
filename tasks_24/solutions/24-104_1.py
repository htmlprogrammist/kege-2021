# Автор: В.Н. Шубинкин

with open('24-1.txt') as tf:
    s = tf.read().strip()

k = 1
maxim = 0
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        k += 1
        if k > maxim:
            maxim = k
            pos = i
    else:
        k = 1
print(pos + 1 - maxim + 1)
