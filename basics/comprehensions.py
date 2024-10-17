'=============================================comprehensions=================================='
# генератор с помощью которого мы можем создавать последовательности используя цикл for в одну строку

# структура
# результат for элемент in последовательность
# i for i in list1
# результат for элемент in послндовательность if фильтр - фильтр
# i for i in list1 if i % 2 == 0

# тело1 if условие else тело2 for элемент in последовательность -- условие
# "четное" if i % 2 == 0 else 'нечетное' for i in range


comprehension = (i for i in range(1, 6))
print(comprehension) 
# генератор - итерируемый объект который не хранит в себе польностью всю последовательность данных а создает их когда требуется

# print(next(comprehension))
# print(next(comprehension))

# next () - функция которая запрашивает у генератора текущий элемент и генератор создает следующий элемент

"=================================================================================================="
list_comprehension = list((i**2 for i in range(1, 11)))
print(list_comprehension) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list_comprehension2 = [i ** 2 for i in range(1, 11)]
print(list_comprehension2) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Создайте список состоящий из нечетных чисел от 1 до 50 используя comprehension
list_comprehension3 = [i for i in range (1, 51) if i % 2 != 0] # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
print(list_comprehension3)

# list2 = []
# for i in  range(1, 51):
#     if i % 2 != 0:
#         list2.append(i)
# print(list2) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
# # создайте список состоящий из 5 строк 'hello' используя 
# list3 = list(('hello' for i in range(1, 6)))
# print(list3)

# list4 = []
# for i in range(5):
#   list4.append('hello')
# print(list4)

# # Создайте список из чисел от 1 до 10 но вместо чисел написать четное или нечетное

# list5 = ['четное' if i % 2 == 0 else 'нечетное' for i in range(1, 11)]
# print(list5)

# list5 = []
# for i in range(1, 10):
#     if i % 2 == 0:
#        list5.append('четное')
#     else:
#         list5.append('нечетное')
# print(list5)

# создайте список из существуещего списка оставив только строки

# list6 = [1, 2, 3, 4, 5, 'hello', 'world', 'ADA', 'courses']

# # list1 = [i for i in list6 if type(i) == str]
# # print(list1) # ['hello', 'world', 'ADA', 'courses']

# list1 = []
# for i in list6:
#     if type(i) == str:
#         list1.append(i)
# print(list1) # ['hello', 'world', 'ADA', 'courses']

# '==========================Dict comprehensions======================='
# dict_ = dict( (i, i ** 2) for i in range(1, 11))
# print(dict_) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# dict_ = {i: i ** 2 for i in range(1,11)}
# print(dict_) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# # Дан словарь создайте его копию при помощи comprehension
dict1 = {1: 'a', 2: 'b', 'c': 3}
# dict2 = {k:v for k, v in dict1.items()}
# print(dict2)
# print(dict1) # {1: 'a', 2: 'b', 'c': 3}

# dict2 = {}
# for key, values in dict1.items():
#     dict2[key] = values
# print(dict2)

# Дан словарь поменяйте ключи со значениями используя comprehension

dict1 = {1: 'a', 2: 'b', 3: 'c'}
# dict2 = {keys: values for values, keys in dict1.items()}
# print(dict2)

# dict2 = {}
# for key, value in dict1.items():
#     dict2[value] = key
#     print(dict2)

# дан словарь где значения - списки с числами создайте словарь где значениями будут суммы этих чисел
# dict1 = {
#      "a":[1,2,3,4],
#      "b":[10,15,16,17],
#      "c":[1,2,54]
# }
# dict2 = {k: sum(v) for k, v in dict1.items()}
# print(dict2)

'====================================Вложенные comprehension============================='
# Создайте словарь где ключами будут числа от 1 до 5 а значаниями - списки с числами от 1 до этого числа
# {1; [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

# dict1 = {}

# for i in range (1, 6):
#     key = i
#     value = [j for j in range(1, i+1)]
#     dict1[key] = value
# print(dict1)

# dict2 = {i: [j for j in range(1, i+1)] for i in range(1, 6)}
# print(dict2)
# dict3 = {i: list(range(1, i+1)) for i in range(1, 6)}
# print(dict3)

#Создать список состоящий из 10 списков в каждом из которых строка 'hello world' поаторяется по 5 раз

# list1 = []
# for i in range(10):
#     inner_list = []
#     for j in range(5):
#         inner_list.append('hello world')
#     list1.append(inner_list)
# print(list1)

# list2 = []
# list3 = [['hello' for i in range(1, 6)] for i in range(10)]
# print(list3)

# list1 = [['hello world']*5 for i in range(10)]
# print(list1)

# list1 = [['hello world']*5]*10
# print(list1)

#Создайте список из 10 списков в которых будут числа от 1 до 5

# list2 = [list(range(1, 6)) for i in range(10)]
# print(list2)


# СОздацте словарь где ключами будут числа от 1 до 5 а значениями будут словари в которых ключами будут числа от 1 до этого числа а значениями будут списки от 1 до этого числа
# dict2 = {i: {j: list(range(1, j + 1)) for j in range(1, i + 1)} for i in range(1, 6)}
# print(dict2)

# dict2 = {}
# for i in range(1, 6):
#     inner_dict = {}
#     for j in range(1, i+1):
#         list_ = []
#         for k in range(1, j+1):
#             list_.append(k)
#         inner_dict[j] = list_
#     dict2[i] = inner_dict

# print(dict2)
            
# Дан словарь:
#  dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# создайте dict2:
# - ключи должеы быть те же что и в первом словаре но каждый символ 'i' замените на ''
# - знвчением должно быть колво повторений символов 'i' в этом ключе
dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
dict2 = {key.replace('i', ''): key.count('i') for key in dict1}
print(dict2)

# Используя приведенный словарь dict_, создайте список из id, 
# которые хранятся под ключом comments. Берите только те комментарии, 
# количество которых больше 3
dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}
ids = [  comment['id'] for inner_dict in dict_.values() if len(inner_dict['comments']) > 3 for comment in inner_dict['comments']
]
print(ids)


