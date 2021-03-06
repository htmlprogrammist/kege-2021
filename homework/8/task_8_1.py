"""
№ 161
161) Сколько существует чисел, восьмеричная запись которых содержит 6 цифр, 
причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
"""
b = int('100000', 8)
n = int('777777', 8)
counter = 0

for i in range(b, n + 1):
    # oct_number = str(i)
    # if len(oct_number) < 6:
    #     oct_number = (6 - len(oct_number)) * "0" + oct_number
    if len(str(i)) == len(set(str(i))):
        for ii in range(len(str(i)) - 1):
            if str(i)[ii] % 2 == 0 and str(i)[ii + 1] % 2 != 0:
                counter += 1
            if str(i)[ii] % 2 != 0 and str(i)[ii + 1] % 2 == 0:
                counter += 1
print(counter)
