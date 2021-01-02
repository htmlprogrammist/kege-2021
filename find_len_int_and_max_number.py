# Сколько знаков и максимальную цифру
number = int(input())
A = []
count = 0
while number > 0:
    last_number = number % 10
    A.append(last_number)
    number = number//10
print(A)
print(max(A))
print(len(A))
