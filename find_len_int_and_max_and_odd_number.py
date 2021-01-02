n = int(input())
count = 0
maxdigit = 0
summa = 0
while n != 0:
    digit = n % 10
    if digit > maxdigit:
        maxdigit = digit
    if digit % 2 != 0:
        summa += digit
    n = n//10
# print('Max Digit =', maxdigit)
# print('Length even numbers =', count)
print('Summa odd elements', summa)
