"============================================Числа==========================================="
# integer(int) - целые числа
# num1 = 12
# type() - фукция которая возвращает тип данных объектов
# print(type(num1)) # <class 'int'>

# num_str = '10'
# print(type(num_str)) # class 'str'>
# num2 = int(num_str)
# print(num2)
# print(type(num2))


# float - вещественные числа

# float_number = 10.5
# print(type(float_number)) #<class 'float'>

# float_str = '45.12'
# new_float = float(float_str)
# print(new_float)  # 45.12
# print(type(new_float)) # <class 'float'>

# decimal - точное вещественное(дробное) число
# чтобы использовать decimal нужно его импортировать

from decimal import Decimal
# import decimal
decimal_num = Decimal('0.1')
float_num = 0.1
print(float_num + float_num + float_num + float_num + float_num + float_num + float_num + float_num + float_num + float_num) # 0.9999999999999999

print(decimal_num + decimal_num + decimal_num + decimal_num + decimal_num + decimal_num + decimal_num + decimal_num + decimal_num + decimal_num) # 1.0


# binary(bin) - числа в двоичной системе исчесления

binaru_num = bin(255)
print(binaru_num) # 0b11111111
# hex - 16 система исчесления
hex_num = hex(255)
print(hex_num) # 0xff


"===============================================Операции над числами=================================================="
5 +  7 # сложение
7 - 5 # вычитание
2 * 5 # умножение
4 / 2 # 2.0 (деление с остатком)
4 // 2 # 2 целочисленное деление
5 % 2 # 1 получение остатка от деления
2 ** 3 # 8 возведение в степень
25 ** 0.5 # 5 нахождение квадратного корня числа

# модуль числа - перевод из отриц числа в положительное
# ABS() - находит модуль числа
negativ_num = -1000
positive_num = abs(negativ_num) #-1000
print(positive_num)  #-1000
print(negativ_num) # 1000
print(abs(-0.1)) # 0.1
print(abs(10)) # 10 
# round() - функция для округления числа
print(round(5.6)) # 6 (округление в большую сторону)
print(round(5.5)) # 6 (в меньшую сторону)
print(round(5.4)) # 5 (округлит до 6)
print(round(49.49)) # 49 (округление идет только по первой цифре после точки)

# можно указать колво цифр после запятой
print(round(10.0476, 2)) # 10.05

# sqrt() - функция для нахождения квадратного корня числа (его нужно импортировать)

from math import sqrt

print(sqrt(25)) # 5.0
print(25 ** 0.5) # 5.0
print(sqrt(1000)) # 31.622776601683793


# pow(): 
# 1) возводит число в степень
# 2) находит остаток от деления на третье число

print(pow(10, 2)) # 100 (запись аналогична: 10 ** 2)
print(pow(10, 2, 3)) # 1 (запись аналогична: 10 ** 2 % 3)

# divmod() - функция, которая возвращает 2 числа, где 1 число - целая часть от деления а второе - остаток от деления

print(divmod(5, 2)) #(2, 1)
print(divmod(1012010192019200192019, 12)) # 84334182668266682668, 3)
