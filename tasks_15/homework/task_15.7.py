def F(x, y, A):
    return ((x**2 + x - 20 >= 0) or check_set_A_X()) and ((x**2 - 3*x - 18 <= 0) or check_set_A_X())


def check_set_A_X(set_x, A):
    if not set_x ^ A:  # Если между ними нет разницы, но это неправильно.
        pass
        # Чего-то не хватает...
