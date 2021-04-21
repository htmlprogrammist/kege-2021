"""
№ 107, Джобс 07.09.2020
На вход программе поступает набор чисел в диапазоне [10; 10000]. 
Необходимо узнать сколько чисел в массиве находятся в диапазоне между средним значением и медианой, 
включая совпадающие с этими показателями значения. 

Входные данные представлены в файле следующим образом. 
В первой строке записано нечетное число N – количество чисел, 
в каждой из последующих N строк число из обрабатываемой последовательности. 

В качестве ответа дать одно число – количество найденных чисел. 

Пример организации исходных данных во входном файле:  
7 
10 
47 
60 
84 
65 
47 
37 

При таких исходных результатом является число 2. Среднее значение равно 50, медиана – 47

Медианой называется такое значение, что ровно половина из оставшихся элементов больше медианы и, 
соответственно, вторая половина меньше медианы. 

340
"""
document = open("task_26_3.txt")
data = document.readlines()
n = int(data[0])
del data[0]
data = sorted(list(map(int, data)))  # данные теперь имеют целочисленный тип, всё в одной коробочке
counter = 0

average = sum(data) // n  # среднее значение
median = data[len(data) // 2]  # медиана

for number in data:
    if average < number <= median:
        counter += 1

print(counter)
