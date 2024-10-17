'===============================Области видимости==========================================='
# LEGB - local Enclosed Global Built-in

'===============================Built-in===================================================='
# Встроенная область видимости (list, sum, dict, print, input)


'================================Global====================================================='
# Все переменные которые мы создали внутри одного файла
# чтобы посмотреть все глобальные переменные можно использовать функцию globals()

# a = 10
# b = 12
# print(globals())
'================================Local======================================================='
# Локальное пространство имен - те переменные которые были созданы внутри функции

# abc = 10

# def func(a, b):
#     print('GLOBALS', globals())
#     hello = 'hello'
#     print('LOCALS', locals())
#     print(a, b, hello)
#     print(abc)

# func(5, 7)
# print(hello) # NameError: name 'hello' is not defined

'===============================Enclosed======================================================'
# Замкнутое пространство имен - локальное пространство у которого есть внутреннее локальное пространство

# var = 'global'

# def func():
#     # Локальное пространство имен для глобального пространства
#     # замкнутое пространство (потому что есть более локальное пространство)
#     var = 'enclosed'
#     def inner_func():
#         # Локальное пространство имен для пространства func
#         var = 'local'
#         print(var)
#     print(var)
#     inner_func()

# print(var)
# func()


# count = 1 

# def increase_count():
#     global count
#     print(count)
#     count += 1

# increase_count()
# print(count)

# def count(i):
#     counter = 0

#     def increase_counter():
#         nonlocal counter # доступ на изменение переменной замкнутого пространства
#         print(counter)
#         counter += 1
#     for _ in range(i):
#         increase_counter()

# count(5)

# count = 0 

# for i in range(1000):
#     print(count)
#     count += 1
#     print(globals())