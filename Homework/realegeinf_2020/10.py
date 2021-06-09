massive_results = []

for i in range(100000, 1000000, 5):
    number = i
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    digits.reverse()

    check_digits = set(digits)
    if len(digits) == len(check_digits):
        for j in range(1, len(digits) - 1):
            if (digits[j - 1] % 2 != digits[j] % 2) and (digits[j] % 2 != digits[j + 1] % 2):
                massive_results.append(i)
print(set(massive_results))
print(len(set(massive_results)))  # 17088
