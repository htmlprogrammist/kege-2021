# Автор: В.Н. Шубинкин

with open('24-j2.txt') as tf:
    s = tf.read().strip()

max_count = 0
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
print(max_count)
