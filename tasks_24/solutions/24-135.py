# Автор: В.Н. Шубинкин

with open('24-j4.txt') as tf:
    s = tf.read().strip()

print(s.count('BOSS') - s.count('JBOSS') - s.count('BOSSJ') + s.count('JBOSSJ'))
