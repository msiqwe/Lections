'========================================Exception==========================================='
# Исключения (ошиьки которые прерывают работы кода если они не обработаны)

# SyntaxError
# Исключение которое выходит когла в коде допущена синтаксическая ошибка

#( SyntaxError: unexpected EOF while parsing

#' SyntaxError: EOL while scanning string literal
# a = 

# NameError
# Исключение которое выходит когда мы обращаемся к не существующей переменной
# print(a) NameError: name 'a' is not defined

# indexError
# Исключение которое выходит когда мы обращаемся к не существующему индексу
# list1 = [1, 2, 3, 4, 5]
# print(list1[1212]) # IndexError: list index out of range

# KeyError
# Исключение которое выходит когда обращаемся по не существующему ключу
# dict1 = {1: 123, 2: 2}
# print(dict1[32]) # KeyError: 32

# ValueError
# Исключение которое возникает когда мы передаем в функцию не корректный для нее тип данных
# int('sssdsds') # ValueError: invalid literal for int() with base 10: 'sssdsds'


# Когда мы распаковываем мтерируемый объект на несколько переменных и колво переменных не совпадает с колвом элементов в итерируемом объекте
# a, b = [1] # ValueError: not enough values to unpack (expected 2, got 1)


# IndentationError
#выхолит когда мы не правильно используем отступы

    # a = 5 # IndentationError: unexpected indent

# for i in range(5):
# print(i) # IndentationError: expected an indented block

#TypeError
"""
Когда мы пытаемся передать функции больше или меньше аргументов чем принимает функция

"""

# for i in 1212: # TypeError: 'int' object is not iterable
#    ...

# '5' + 5 # TypeError: can only concatenate str (not "int") to str
# 5 + '4' # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# {[1,2,3]: 12} # TypeError: unhashable type: 'list'
# input('Введи цифру', 1) # TypeError: input expected at most 1 argument, got 2

# Exception
# Исключение которое создали чтобы его вызывать
'=================================Вызов исключений==============================='

# raise NameError('Hello world') # NameError: Hello world


'================================Обработка исключений============================='

# чтобы код не прекрашал работу мы модем использовать кон конструкцию try-except и обрабатывать вызванное исключение


# try:
#     # код который возможно вызовет ошибку
#     num = int(input('Введите число:'))
# except ValueError: # ошибка которая может возникнуть
#     print('вы ввели не число!')
# else:
#     # который отработает только если ошибка не вышла
#     print(num)
# finally:
#     # код который отработает в любом случае
#     print('до свидания!')

# try:
#     raise ValueError('ERROR')
# except (SyntaxError, NameError):
#      print('Вышла одна из указанных ошибок')

# try:
#     raise TypeError('Type')
# except Exception as error:
#     print('Ошибка:', type(error).__name__)


# Напишите код, который принимает два числа от пользователя и выводит результат их деления. Обработайте исключения ValueError и ZeroDivisionError, выводя сообщение "Произошла ошибка!".

# try: 
#     num1 = int(input('Введите первое число'))
#     num2 = int(input('Введите второе число число'))
#     print(num1/num2)
# except (ValueError, ZeroDivisionError):
#     print('Error')

# Напишите код, который принимает сумму денег от пользователя и выбрасывает исключение ValueError с сообщением "Сумма не может быть отрицательной!", если сумма меньше 0. Обработайте это исключение и выведите сообщение ошибки. Если исключение не возникло, выведите сумму.


# try: 
#     summa1 = float(input('Введите cum'))
#     if summa1 < 0:
#         raise ValueError('Сумма не может быть отриц')
# except ValueError:
#     print('Введите корректное число')
# else:
#     print(summa1)
# finally: 
#     print('Спасибо и пока!')

# Напишите код, который пытается сложить строку и число. Обработайте исключение TypeError, выводя сообщение "Unsupported option"
# num1 = 12
# str1 = 'hello'
# try:
#     num1 + str1
# except TypeError:
#     print("Unsupported option")

# Напишите код, который пытается расширить список, который не был создан. Обработайте исключение NameError, и выведите сообщение 'list does not exist'.

# try:
#     list1.extend(list2)
# except NameError:
#     print('list does not exist')

# Напишите код, который перебирает элементы списка, превышая его длину. Обработайте исключение IndexError, не выполняя никаких действий при возникновении ошибки.

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# try:
#     for i in range(0, len(list1) + 1):
#         print(list1[i])
# except IndexError:
#     print('error')


# warehouse = [
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
#     ['1', '2', '3'],
#     [1, 2, 3, 4 , 5, 6],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]
# # Напишите код, который проверяет длину хранилища и выбрасывает исключение ValueError, если длина больше 10. Также выбрасывайте исключение ValueError, если какой-либо вложенный список внутри хранилища имеет длину больше 3.


# if len(warehouse) > 10:
#     raise ValueError('длинна более 10')
# for i in warehouse: 
#     if len(i) > 3:
#         raise ValueError('длинна более 3')

# Напишите код, который уменьшает значение переменной в цикле while. Обработайте исключение KeyboardInterrupt, выводя сообщение "Nope".

# v = 110000000
# try:
#     while v > 0:
#       print(v)
#       v -= 1
# except KeyboardInterrupt:
#     print('nope')

#  Напишите код, который принимает строку, разделяет её на элементы и пытается преобразовать каждый элемент в целое число, добавляя его в список. Если элемент не является числом, выбрасывайте исключение ValueError с сообщением "Данный элемент не является числом!".


a = input().split()
list1 = []
for element in a:
    try:
        list1.append(int(element))
    except ValueError:
        print('Данный элемент не является числом!')
print(list1)