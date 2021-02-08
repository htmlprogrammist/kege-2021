s = '>' + '1' * 10 + '2' * 20 + '3' * 30
a = []
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>')
    elif '>2' in s:
        s = s.replace('>2', '2>')
    else:
        s = s.replace('>3', '1>')

for i in range(len(s) - 1):
    a.append(int(s[i]))

print(sum(a))
