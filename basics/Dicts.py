'==================================Словари==============================='
# dict - изменяемый итерируемый неупорядоченный неиндекмируемы тип данных для хранения данных в парах (ключ:значение)

user = {
    'name': 'Artem',
    'country': 'Kyrgyzstan',
}

print(user) # {'name': 'Artem', 'country': 'Kyrgyzstan'}

print(user['name']) # Artem

# Ключами в словарях могут быть только не изменяемые типы данных
# user2 = {
#     'login': 'nmusi',
#     ['password']: 'hello_world'
# }

# dict1 = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
# print(dict['a']) # 4 ( если ключи одинаковые то сохранится только последние значение)
# print(dict1['hello']) # KeyError: 'hello'

'===============================Создание словарей========================'
users = {
    'name': 'artem',
    'password': '1'   
}

#2
dict2 = {}
print(dict2) # {}
dict2['name'] = 'Artem'
print(dict2) # 'name': 'Artem'}
dict2['password'] = hash('artem123')
print(dict2) # {'name': 'Artem', 'password': -6661701021204699443}

'=================================Методы словаря==========================='
# get() - метод который возвращает значение по ключу если такого ключа не вернет None

print(dict2.get('password')) # -2851355700199630141
print(dict2.get('name')) # Artem

# pop() - удвляет пару по ключу и возвращает значение
dict4 = {'a': 1, 'b': 2}
popped = dict4.pop('b')
print(popped) # 2
print(dict4) # {'a': 1} 

# popitem() - удаляет последнюю пару и возвращает ее
dict_ = {1: 'a', 2: 'b', 'c': 'a'}
popped = dict_.popitem()
print(popped)
print(dict_)
dict_.popitem()
dict_.popitem()
print(dict_)

# print(dir(dict))

# update() - расширяет словарь парами из второго словаря
dict1 = {1: 'a', 'b': 3}
dict2 = {'name': 'artem', 'last_name': 'grebnev'}
dict1.update(dict2)
print(dict1) # {1: 'a', 'b': 3, 'name': 'artem', 'last_name': 'grebnev'}
print(dict2) # {'name': 'artem', 'last_name': 'grebnev'}

# clear() - очищает полностью словарь
dict1.clear()
dict2.clear()
print(f'dict2 {dict2}')
print(f'dict1 {dict1}')


"""
keys, values, items

keys - метод который возвращает ключи из словаря
values - метод который возвращает все значения из словаря
items - метод котрый возвращает все ключи и значения
"""
'=================================Итерирование словарей========================'

user = {
    'name': 'Artem',
    'last_name': 'Musi',
    'age': 16

}

print(user.keys()) # dict_keys(['name', 'last_name', 'age'])
print(user.values()) # dict_values(['Artem', 'Musi', 16])
print(user.items()) # dict_items([('name', 'Artem'), ('last_name', 'Musi'), ('age', 16)])

for key in user:
    print(key)
    # при итерации словаря будут приходить ключи



for key in user.keys():
   print(key)
 # при итерации dict_keys тоже приходят ключи


for value in user.values():
    print(value)
    # при итерации  dict_values приходят только значения

# key, value = ('name', 'Artem')

for key, value in user.items():
    print(f'Ключ: {key}, значение: {value}')





# вам дан словарь
dict1 = {"a":1, "b":2, "c":3}
# создайте новый словарь, поменяв ключи со значениями
# {1:"a", 2:"b", 3:"c"}
dict2 = {}

for key, value in dict1.items():
    dict2[value] = key
    print(dict2)
    