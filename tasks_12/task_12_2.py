"""
638
"""
s = '8' * 75
# while '222' in s or '888' in s:
while s.find('222') >= 0 or s.find('888') >= 0:
    if '222' in s:
        s = s.replace('222', '8', 1)
    else:
        s = s.replace('888', '2', 1)
print(s)
