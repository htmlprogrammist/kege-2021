# for c in 'Hello':
#     print(c)

items = ['foo', 'bar', 'baz']

for (index, elem) in enumerate(items):
    items[index] += elem + '!'

print(items)  # ['foofoo!', 'barbar!', 'bazbaz!']
# Должен был вернуть: ['foo!', 'bar!', 'baz!']

"""
Встроенная в Python функция enumerate() применяется для итерируемых коллекций (строки, списки, словари и др.)
 и создает объект, который генерирует кортежи, состоящие из двух элементов - индекса элемента и самого элемента.
"""
