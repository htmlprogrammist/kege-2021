# Автор: В.Н. Шубинкин

with open('24-j5.txt') as tf:
    s = tf.read().strip()

print(s.count('OCK') - s.count('STOCK'))

"""
count = 0
for i in range(len(s)):
  if s[i:i+5] != "STOCK" and s[i+2:i+5] == "OCK":
    count += 1

print( count )
"""