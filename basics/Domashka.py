# list1 = [10, 20, 30, [40, 50, 60], 'hello', None, True] 
# print(list1[3]) # [40, 50, 60]
# print(list1[0]) # 10
# print(list1[-1]) # True

# list2 = list()
# age = 16
# name = 'Artem'
# year = 2024
# list2.append(age)
# list2.append(name)
# list2.append(year)
# print(list2) # [16, 'Artem', 2024]

# list1 = [5, 10, 15, 20, 25]
# popped = list1.pop(2)
# print(list1) # 5, 10, 20, 25]
# print(popped) # 15


# list2 = ['apple', 'banana', 'orange', 'grape', 'banana']
# popped = list2.pop(1)
# print(list2) # ['apple', 'orange', 'grape', 'banana']
# print(popped) # banana


# list3 = [2, 4, 4, 6, 4, 8, 4]
# print(list3.count(4)) # 4 



# list4 = ['python', 100, False, 3.14, 'python']
# print(list4.index('python')) # 0

# list5 = ['a', 'b', 'd', 'e']
# list5.insert(3, 'c')
# print(list5) # ['a', 'b', 'd', 'c', 'e']


# list6 = [1, 2, 3]
# list7 = [4, 5, 6]
# list6.extend(list7)
# print(list6) # [1, 2, 3, 4, 5, 6]

# list8 = ['h', 'e', 'l', 'l', 'o']
# list8.reverse()
# print(list8) # o', 'l', 'l', 'e', 'h']

# list9 = [9, 2, 7, 3, 5]
# list10 = ['banana', 'apple', 'cherry']
# list9.sort() # [2, 3, 5, 7, 9]
# print(list9)
# list10.sort() # ['apple', 'banana', 'cherry']
# print(list10)


# Используя приведенный словарь dict_, создайте список из id, 
# которые хранятся под ключом comments. Берите только те комментарии, 
# количество которых больше 3
# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }
# 'Задача 1'
# try: ...
# except: ...
# else: ...
# finally: ... 

# 'Задача 2'
# try:
#     print(not error)
# except NameError: 
#     print('Такой переменной не существует!')
# 'Задача 3'
# try:
#     num1 = float(input('Введите число 1'))
#     num2 = float(input('Введите число 2'))
#     result = num1 / num2
#     print(result)
# except ZeroDivisionError:
#     print('Все пизда')

# 'Задача 4'
# try:
#     str1 = input('Число блеат')
#     str2 = input('Число сцука')
#     result = int(str1) +  int(str2)
#     print(result)
# except ValueError:
#     print('Все хуйня ты баран введи число!')


#'Задача 5'
# dict1 = {'a': 1, 'b': 2, 'c': 3}

# key = input("Введите ключ: ")
# try:
#     value = dict1[key]
#     print("Хуйня в словаре:", value)
# except KeyError:
#     print("Нет такого дебил!")


#'Задача 6'
# listsuk = [1, 2, 3, 4, 5]

# index = int(input("Введите индекс: "))
# try:
#     element = listsuk[index]
#     print("Тема по индексу:", element)
# except IndexError:
#     print("Нет такого элемента баран!")

#'Задача 7'

# try:
#     age1 = int(input('Возраст?'))
#     if age1 < 18:
#         raise ValueError
# except ValueError:
#     print('Пока родной')
# else :
#     print('заходи ')
# finally:
#     print('До встречи')

# while True:
#     try:
#         num1 = int(input('Введи первое число: '))
#         num2 = int(input('Введи второе число: '))
#         operation = input('Введи операцию: ')
#         if operation == '+':
#             result = num1 + num2 
#             print(f'Ответ: {result}')
#         elif operation == '-':
#             result = num1 - num2
#             print(f'Ответ: {result}')
#         elif operation == '/':
#             result = num1 / num2
# #             print(f'Ответ: {result}')
# #         elif operation == '*':
# #             result = num1 * num2
# #             print(f'Ответ: {result}')
# #         elif operation == '**':
# #             result = num1 ** num2
# #             print(f'Ответ: {result}')
# #         elif operation == '//':
# #             result = num1 // num2
# #             print(f'Ответ: {result}')
# #         else:
# #             print("Данной операции нет в системе!")
# #     except (ZeroDivisionError, ValueError):
# #         print('Вы ввели не число, либо вы делите на 0!')
# #     continue_calc = input('Вы хотите продолжить (y/n) ?')
# #     if continue_calc != 'y':
# #         print('Пока!')
# #         break


# def smallest():
#     numbers = set()
#     for _ in range(5):
#         num = int(input('Введите число: '))
#         numbers.add(num)
#     print('smallest: ', min(numbers))

# smallest()

# def credit():
#     zaim = float(input("Введите сумму займа (не менее 100000): "))
#     if zaim < 100000:
#         print("Сумма займа должна быть не менее 100000.")
#         return
#     procent = 7.89
#     total_return = zaim + (zaim * (procent / 100))
#     print("Сумма к возврату:", round(total_return, 2))

# credit()

# def perdigits():
#     text = input('Введите текст: ')
    



# def days_month():
#     years = int(input('Введите колво лет: '))
#     month = int(input('Введите колво месяцев: '))
#     tot_days = years * 365 + month * 30
#     print('Колво дней: ', tot_days)

# days_month()

# def cube():
#     cube_dict = {i: i**3 for i in range(1, 11)}
#     return cube_dict
# print(cube())


def sum_num():
    return(sum(range(1, 51)))

print(sum_num())


while True:
    try:
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите ыторое число: '))
        operation = input('Введите операцию: ')
        if operation == '+':
            result = num1 + num2 
            print(f'Ответ: {result}')
        elif operation == '-':
            result = num1 - num2 
            print(f'Ответ: {result}')
        elif operation == '/':
            result = num1 / num2 
            print(f'Ответ: {result}')
        elif operation == '*':
            result = num1 * num2 
            print(f'Ответ: {result}')
        elif operation == '**':
            result = num1 ** num2 
            print(f'Ответ: {result}')
        elif operation == '//':
            result = num1 // num2 
            print(f'Ответ: {result}')
    except (ZeroDivisionError, ValueError):
         print('Вы ввели не число, либо вы делите на 0!')
    continue_calc = input('Вы хотите продолжить (y/n) ?')
    if continue_calc != 'y':
        print('Пока!')
        break