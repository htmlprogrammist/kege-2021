"""

"""
from itertools import product
n = 0
p = product('АНДРЕЙ', repeat=7)

for x in p:
    if x[0] != 'Й' and x.count('А') == 1 and x.count('Й') == 1:
        n += 1
print(n)

# for i in product('АНДРЕЙ', repeat=7):
#     # if i[0] != 'Й' and i.count('A'):
#     print(i, i.count('A'))
#     input()
