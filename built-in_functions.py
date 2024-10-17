'======================================Встроенные функции===================================================='
# map, filter, reduce, zip, enumerate

# zip - соединяет несколько последовательностей (получаем генератор в котором элементы это tuple)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [10.1, 10.2, 20.6]

zipped = list(zip(list1, list2, list3))
print(zipped) # [(1, 'a', 10.1), (2, 'b', 10.2), (3, 'c', 20.6)]

for element in zipped:
    print(element) 
# (1, 'a', 10.1)
# (2, 'b', 10.2)
# (3, 'c', 20.6)

list4 = [1, 2, 3, 4, 5]
list5 = ['a', 'b', 'c', 'd', 'e']
dict_   = dict(zip(list4, list5))
print(dict_) # 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
'=====================================Enumerate================================================================'
# enumerate - нумерует последовательность по дефолту начинает с нуля также как и с zip получаем генератор

enumerated = enumerate('hello')
for element in enumerated:
    print(element)
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

string = 'hello world'
print(list(enumerate(string))) # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'w'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd')]
'====================================map===================================================================='

# map - функция которая принимает в аргемнты функцию и последовательность, и применяет эту функцию к элементам последовательности (записывает в новую последовательность в результат функции, в которую передаются элементы последовательности)

# поменяйте тип данных элементов list_ со строк на числа
list_ = ['1', '2', '3', '4', '5']
mapped_list = list(map(int, list_))
print(mapped_list) # [1, 2, 3, 4, 5]

# создать новый список элементы которого квадратф элементов list1
list1 = [12, 13, 14, 15, 16, 17]
# mapped_list = list(map(lambda x: x**2, list1))
# print(mapped_list)

def to_2_degree(x):
    return x ** 2

print(list(map(to_2_degree, list1))) # [144, 169, 196, 225, 256, 289]
'==============================================Filter=============================================================='
# filter - возвращает генератор с элементами прошедшими фильтр (какое то условие), принимает в себя : 1) функцию, 2) последовательность

# отфильтровать элементы списка оставить только те которые больше
list1 = [1, 0, -1, -23, -55, 15, 22]
filtered = list(filter(lambda x: x > 0, list1))
print(filtered) # [1, 15, 22]

list_ = list(range(1, 51))
# отфильтровать list_ оставить только четные числа
filtered = list(filter(lambda x: x % 2 == 0, list_))
print(filtered)

users = [
    {'name': 'artem', 'age': 19},
    {'name': 'nikita', 'age': 18},
    {'name': 'maratik', 'age': 13},
]
# отфильтровать пользователей оставить только тех кому больше 18

solution1 = [i for i in users if i['age'] >= 18]
print(solution1) # [{'name': 'artem', 'age': 19}, {'name': 'nikita', 'age': 18}]

solution2 = list(filter(lambda user: user['age'] >= 18, users))
print(solution2)
'=============================================Reduce==================================================================='
from functools import reduce
# reduce - принимает функцию и последовательность возвращает 1 результат (передаваемая функция должна обязательно принимать 2 аргумента)

list1 = list(range(1, 101))
result = reduce(lambda x, y: x + y, list1)
print(result) # 5050

string = 'hello'
res = reduce(lambda x, y: x + '%' + y, string)
print(res) # h%e%l%l%o

# 1) напишите программу которая отбирает слова длина которых больше 7 из исходного списка

words = ["программирование", "Python", "разработка", "тестирование", "слово", "длинное"]
long_words = list(filter(lambda word: len(word) > 7, words))
print(long_words)

# напишите программу которая считает количество четных и нечетных чисел в списке и выводит их количество в формате строки "четные: {колич'ество}, нечетные: {количество}"

list1 = [1, 3, 5, 6, 7, 8, 9, 44, 55, 66665, 55, 2, 4, 7]
nums = len(list(filter(lambda x: x % 2 == 0, list1)))
print(nums)

nums_odd = len(list(filter(lambda x: x % 2 != 0, list1)))
print(nums)
result = f"четные: {nums}, нечетные: {nums_odd}" 
print(result)

# 3) напишите программу которая находит самое длинное имя в списке
from functools import reduce
list_name = ['artem', 'nikita', 'maks', 'tima']
longest_name = reduce(lambda x, y: x if len(x) > len(y) else y, list_name)
print(longest_name)

# Напишите програму которая меняет число на 'fizz' если оно делится на 3, и на строку 'buzz' если не делится, в диапазоне чисел от 1 до 50 включительно

list1 = list(range(1, 51))
result = list(map(lambda x: 'fizz' if x % 3 == 0 else 'buzz', list1))
print(result)

#  напишите программу которая находит минимальное значение у элемента в списке
from functools import reduce
list_name = [1, 3, 5, 6, 77, 33, 2, 5, 4, 33, 2, 4]
longest_name = reduce(lambda x, y: x if int(x) < int(y) else y, list_name)
print(longest_name)