s = '0' + '1' * 20 + '2' * 14 + '3' * 6
print(s.count('1'))  # ?
while '01' in s or '02' in s or '03' in s:
    s = s.replace('01', '30', 1)
    s = s.replace('02', '101', 1)
    s = s.replace('03', '202', 1)
print(s)
one = s.count('1')  # 15
two = s.count('2')  # 10
three = s.count('3')  # 60
print(one, two, three)