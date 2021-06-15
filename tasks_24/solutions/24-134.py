# Автор: В.Н. Шубинкин

with open('24-j3.txt') as tf:
    s = tf.read().strip()

print(s.count('TIK') + s.count('TOK'))
