document = open("24.txt")
s = document.readline()
s = s.replace("XZZY", "XZZ ZZY")
a = max(s.split(), key=len)
print(len(a))

