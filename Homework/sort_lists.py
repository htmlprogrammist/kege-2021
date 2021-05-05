# Сортировка происходит в алфавитном порядке, судя только по ПЕРВОМУ элементу,
# остальные элементы в строке игнорируются
list_1 = ['a', 'b', 'd', 'c', 'frtererttyurtyurtyuirtyiu', 'e123']
list_1.sort()
print('1-й список', list_1)

# Сортировка чисел происходит от меньшего к большему
list_2 = [1, 4, 5, 3, 10, 2]
list_2.sort()
print('2-й список', list_2)
# Здесь Питон меня порадовал, потому что JavaScript отсортировал бы так: [1, 10, 2, 3, 4, 5]

# Можно поменять, используя ключевое слово(?) reverse
list_3 = [1, 4, 5, 3, 10, 2]
list_3.sort(reverse=True)
# По умолчанию reverse=False
print('3-й список', list_3)

# Сортировка по длине каждого элемента массива
list_4 = ['123', '123456789', '123456']
list_4.sort(key=len)
print('4-й список', list_4)

# list_5 = list_2.sort() Выдаёт None
list_5 = sorted(list_2)
print('5-й список', list_5)

list_6 = [1, 2, True, None]
# list_6.sort()
# TypeError: '<' not supported between instances of 'NoneType' and 'bool'
# print(list_6)

list_7 = [1, 2, 'Строка', 3, 'И ещё строка', None, True]
# list_7.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'
# print(list_7)
