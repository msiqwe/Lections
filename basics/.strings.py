"============================================Строки================================================================="
# строки - это неизменяемый индексируемый итерируемый тип данных применяемый для хронения текста заключенного в одинарные или двойные кавычки

# string1 = 'строка с одинарными ковычками'
# string2 = "строка с 2 ковыками"
# error_string = 'неправильная строка"

string3 ="don't" # внутри 2 ковычек все одинарные - просто символы
string4 =' "ADA Courses' # внутри одинарных ковычек все двойные - просто символы

string5 = '''
Многострочный текст
 в одинарных ковычках
тут можно ставить "любые" 'кавычки'
'''

string5 = """
Многострочный текст
 в одинарных ковычках
тут можно ставить "любые" 'кавычки'
"""

string7 = 'hello' + ' ' + 'world' # конкатенация строк (скливание)
print(string7)

string_hello = 'hello'
string_world = 'world'
print(string_hello + ' ' + string_world) # тоже конкатенация

print(string_hello * 7) # hellohellohellohellohellohellohello

"=======================================Экранизация строк=========================================="
# \n - перенос на новую строку
print("hello\nworld") #hello
#                      world

# \t - табуляция
print('hello\tworld') # hello    world

# \' - отображение '
# \ " - отображение "

print("Don\'t")

"=======================================Форматирование строк========================================"
# product_title = input('Введите название товара:')
price = 1000
# # print('Название: product_title, цена: price') названия переменных внутри строки, не считаются пременными они считаются просто символами
# print ('Название:', product_title, 'цена: ', price)

# # 1 способ (f - строки)
# format1 = f'Название: {product_title},\nЦена: {price}'
# print(format1)
"""

Название: Iphone 15
Цена: 1000
"""


# 2 способ
format2 = 'Название: {}\nЦена: {}'
print(format2.format('Iphone 16', 1200))
print(format2.format('Молоко', 100))

# способ 3 
format3 = 'Название: %s\nЦена: %s'
print(format3 % ('Iphone15', 1200))

"=======================================Методы строк==================================================="

# методы это функции которые относятся к определенному типу данных (классу) к ним мы обращаемся через точку
# dir() - функция которая позволяет посмотреть все методы класса

print(dir(str))

# string.upper() - переводит все символы строк в верхний регистр
print('hello'.upper()) #HELLO

# string.lower() - переволит все символы строки в нижний регистр
print('HELLO'.lower()) # hello

# string.swapcase() - метод который переволит регистор символов строки в противоположный
print('hELLo'.swapcase()) # HellO

# string.title() - делает 1 букву каждого слова заглавной 
print('hello world'.title())


# string.capitallize() - делает заглавной только первую букву первого слова
print('hello world'.capitalize())

# string.count() - считает колво вхожднений заданного элемента
print('hello world, this is ADA'.count('l')) # 3
print('hello world, this is ADA'.count('hello world, this is ADA')) # 1

# string.startswith() - метод который проверяет начинается строка с заданного элемента
print('hello world'.startswith('hello')) # True

# string.endswith() - метод который проверяет заканчивается ли строка с заданного элемента
print('hello world'.endswith('hello')) # False
print('hello world'.endswith('hello world'))  # True

# string.islower() - проверяет находимтся ли вся строка в нижнем регистре
print('hello world'.islower()) # True
print('hello wOrld'.islower()) # False
# string.isupper() - проверяет находимтся ли вся строка в верхнем регистре
string_ = input('Введи строку')
print(string_.isupper()) # False тут правильно

# string.isdigit - проверяет состоит ли строка полностью из чисел
print('1234'.isdigit()) # True 
print('1x234'.isdigit()) # False
# string.isalpha() - проверяет состоит ли строка полностью из букв
print('abcd'.isalpha()) # True
print('abc2d'.isalpha()) # False 

# string.isalnum() - проверяет состоит ли строка польностью из букв и цифр
print('122hello'.isalnum()) # true
print('122 hello'.isalnum()) # false

#string.strip() - метод который полностью удаляет все пробелы с начала и с конца строки а середину не трогает
string1 = '                     hello                     '
print(len(string1.strip())) # 5
print(len(string1)) # 47

#string.rstrip() - метод который полностью удаляет все пробелы справа
print(len('hello                  '.rstrip())) # 5
print(len('hello                  ')) # 23

# string.lstrip() - метод который полностью удаляет все пробелы слева
print('                       hello'.lstrip()) 

# split() - дробит строку по разделителю на отдельные элементы и сохраняет их в списке (возвращает не str а list)
string1 = 'hello world, my name is Artem'
print(string1.split()) # если ничего не указать в скобки то по дефолту за разделитель будет считаться пробел
print(string1.split(',')) # делим строку по указанному разделителю (то есть по запятой)

# join() - принимает в список мз строк и соединяет их в одну строку
list_str = ['hello', 'ADA']
print(' '.join(list_str)) # hello ADA
'====================================Индексы==============================='

# Индекс это порядковый номер элемента в последовательности (символа в строке) (индексация всегда начинается с нуля)

'h e l l o  w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#      ...     -3 -2 -1

string = 'ADA Courses'
print(string[3])


"====================================Срезы================================"
# print(string[0:3]) #Ada
# print(string[:3]) #Ada (не обязательно указывать начальный индекс строки)
# print(string[4:11]) # Courses
# print(string[4:]) # Courses (не обязательно указывать конечный индекс строки)
# print(string[4:-1]) # course

# print(string[::-1]) # sesruoC ADA
# print(string[:8]) # ADA Cour
# print(string[:8:2]) # AACu

