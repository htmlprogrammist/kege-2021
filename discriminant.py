import math

a = int(input('Nx^2 + bx + c: '))
b = int(input('{0}x^2 + Nx + c: '.format(a)))
c = int(input('{0}x^2 + {1}x + N: '.format(a, b)))

d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print('x1: {0}, x2: {1}'.format(x1, x2))
elif d == 0:
    x = -b/(2*a)
    print('x0 = ', x)
else:
    print('D < 0')
