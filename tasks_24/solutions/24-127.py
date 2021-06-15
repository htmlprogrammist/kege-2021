# Автор: А.Н. Носкин

with open("24-5.txt") as Fin:
  s = Fin.readline()

c = '('
while c in s: # ищем "(", потом "((" и т.д
  c += '('
print(len(c)-1 )
# минус 1, чтобы убрать лишнюю добавленную "("





