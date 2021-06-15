# Автор: В.Н. Шубинкин

with open('24-3.txt') as tf:
    s = tf.read().strip()

k = 1
maxim = 0
w = s[0]
maxw = ''
for i in range(1, len(s)):
    if s[i] < s[i - 1]:
        k += 1
        w += s[i]
        if k > maxim:
            maxim = k
            maxw = w
    else:
        k = 1
        w = s[i]
print(maxw)
