document = open('22.txt')
a = document.readlines()
string_indexes = []
dictionary_a = {}
list_of_n = []
index = 0
alphabet = [0] * 26
min_k = 100
min_k_index = 100


for i in range(len(a)):
    # a[i] = string
    counter_n = a[i].count('N')
    dictionary_a[i] = counter_n
# print(dictionary_a)
for key in dictionary_a:
    list_of_n.append(dictionary_a[key])
# print(list_of_n)
min_amount_of_n = min(list_of_n)
# print(min_amount_of_n)  # 23

for key in dictionary_a:
    if dictionary_a[key] == min_amount_of_n:
        index = key
        break
# print(index)  # 764
# print(string_indexes)  # [764, 849, 909], а после break мы имеем 764
print(a[index])  # Строчка, с которой я сейчас работаю
for i in range(len(a[index])):
    symbol = ord(a[index][i])
    s_index = symbol - 65
    try:
        alphabet[s_index] += 1
    except IndexError:  # chr(10) ==> '\n', его надо обойти
        # print(symbol, a[index][i], s_index)
        pass

# print(alphabet)

for i in range(len(alphabet)):
    if min_k > alphabet[i]:
        min_k = alphabet[i]
        min_k_index = i
print(min_k_index)
print(min_k, min(alphabet))
min_k = min(alphabet)
print(min_k)
print(chr(min_k_index + 65))
