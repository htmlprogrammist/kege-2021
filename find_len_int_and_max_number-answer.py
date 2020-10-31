n = int(input())
count = 0
maxdigit = 0
while n!=0:
    digit = n%10
    if digit > maxdigit:
        maxdigit = digit
    count+=1
    n=n//10
print('Max Digit =', maxdigit)
print('Length =', count)
