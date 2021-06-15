# Автор: В.Н. Шубинкин

with open('24-j1.txt') as tf:
    s = tf.read().strip()

max_count = 0
count = 0
word = 'КОТ'

i = 0
while i < len(s)-2:
    if s[i:i+3] == 'КОТ':
        count += 1
        max_count = max(max_count, count)
        i += 3
    else:
        count = 0
        i += 1
print(max_count)
