def find_four_movements(a, b):
    answers = []
    y1, y2, y3, y4 = [], [], [], []
    x1 = 4 * a
    y1.append(x1)
    y1.append(b)
    z1 = tuple(y1)
    x2 = a + 1
    y2.append(x2)
    y2.append(b)
    z2 = tuple(y2)
    x3 = 4 * b
    y3.append(a)
    y3.append(x3)
    z3 = tuple(y3)
    x4 = b + 1
    y4.append(a)
    y4.append(x4)
    z4 = tuple(y4)
    answers.append(z2)
    answers.append(z1)
    answers.append(z4)
    answers.append(z3)
    return answers


print(find_four_movements(3, 14))
