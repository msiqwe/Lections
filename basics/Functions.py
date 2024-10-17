# '==============================================Функции=========================================='
# #Функция - это именнованный блок кода который может принимать аргументы и возвращать результат

# def my_sum(x, y):
#     return x + y

# # print(my_sum(10, 10))
# # result = my_sum(20, 20)
# # print(result)

# def my_len(obj):
#     count = 0
#     for element in obj:
#         count += 1 
#     return count

# list1 = [1, 2, 3, 4, 5, 6, True, False, [1,2,3]]
# print(my_len(list1))
# print(my_len('hello'))

# a = 'hello'
# count = 0 
# for element in a:
#     count += 1
# print(count)

# """
# DRY - dont repeat yourself - функции соблюдают этот принцип

# """

# '=======================================Аргументы и параметры=========================================='
# # Параметры - переменные внутри функции значения которым мы задаем при определении фунции (когда пишем def название_функции(параметры))
# # аргументы - переменные которые мы передаем при вызове функции (my_len(аргументы))

# # def my_len(obj): -- obj - параметр
# #     count = 0
# #     for element in obj:
# #         count += 1 
# #     return count
# # print(my_len(list1)) -- list1 - это аргумент

# '=========================================Виды параметров===================================================='
# """
# 1) обязательные 
# 2) не обязательные
#     2.1) с дефолтным значением
#     2.2) *args (все позиционные аргументы которые не попали в обязательные и с дефолтным значением хранятся в typle)
#     2.3) **kwargs (все лишние именнованые аргументы хранятся в dict)
# """
# '=======================================Виды аргументов======================================='
# """
# 1) позиционные (по позиции)
# 2) именнованные (по названию) (параметр = значение)
# """

# def add_or_add_10(num1, num2=10):
#     """
#     Складывает 2 числа 
#     Если второе число не передать слодит с 10
#     """
#     return num1 + num2

# print(add_or_add_10(15, 15)) # Аргументы позиционные
# print(add_or_add_10(num1=22, num2=21)) # Именованные
# # print(add_or_add_10(num2=10)) TypeError
# print(add_or_add_10(num2=12, num1=12)) # 24

# "================================* и **===================================================="
# # * - list, tuple
# list1 = list(range(1, 11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list1)

# list1 = [range(1, 11)] # [range(1, 11)]
# print(list1)

# list1 = [*range(1, 11)]
# print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# dict1 = {1: 'a', 2: 'b', 3: 'c'}
# print(dict1)

# dict2 = {**dict1} # {1: 'a', 2: 'b', 3: 'c'}
# print(dict2)

# list1 = [*dict1]
# print(list1) # [1, 2, 3]

# def func(a, b=10, *args, **kwargs):
#     print('a -', a)
#     print('b -', b)
#     print('args -', args)
#     print('kwargs -', kwargs)

# func(12, 120, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, name='artem', city='bishkek', country='Kyrgyzstan')
# # a - 12
# # b - 120
# # args - (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# # kwargs - {'name': 'artem', 'city': 'bishkek', 'country': 'Kyrgyzstan'}

# '=========================================Lambda============================================'
# # lambda - Анонимная функция которая записывается в одну строку
# lambda_func = lambda x: x ** 10
# print(lambda_func(10)) # 10000000000
# '========================================Калькулятор================================================='

# calculator = {
#     '+': lambda num1, num2: num1 + num2,
#     '-': lambda num1, num2: num1 - num2,
#     '*': lambda num1, num2: num1 * num2,
#     '**': lambda num1, num2: num1 ** num2,
#     '/': lambda num1, num2: num1 / num2,
#     '//': lambda num1, num2: num1 // num2,
#     '%': lambda num1, num2: num1 % num2
# }

# def main():
#     try:
#         num1 = int(input('число1:'))
#         num2 = int(input('число2:'))
#         operation = input('Операция:')
#         func = calculator[operation]
#         result = func(num1, num2)
#         print(f'{num1} {operation} {num2} = {result}')
#     except ValueError:
#         print('Вы написали не число')
#     except KeyError:
#         print('Такой операции нет')
#     except ZeroDivisionError:
#         print('На 0 нельзя делить')

# while True:
#     main()
#     inp = input('Завершить? (yes/no)')
#     if inp.lower() == 'yes':
#         break


db = [
    {'name': 'Artem', 'password': hash('artem123')},
    {'name': 'Artem2', 'password': hash('123321')}
]

def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False

def register(name, password, password_confirm):
    if in_database(name):
        raise Exception('юзер уже такой есть')
    if password != password_confirm:
        raise Exception('Пароли не совпали')
    user = {'name': name, 'password': hash(password)}
    db.append(user)
    return 'Вы успешно зарегались'


def login(name, password):
    if not in_database(name):
        raise Exception('юзер не найден')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('Пароль не верный!')
    return 'Вы успешно вошли в систему'



def  main():
    print('Добро пожаловать!')
    while True:
        try:
            action = input('Register:1, Login:2, Quit:3')

            if action == '3':
                break
            elif action == '1':
                name = input('Введите имя: ')
                password1 = input('Введите пароль: ')
                password2 = input('Подтвердите пароль: ')
                print(register(name, password1, password2))
            elif action == '2':
                name = input('Введите имя: ')
                password = input('Введите пароль: ')
                print(login(name, password))
            else:
                print('Не корректный выбор!')
        except Exception as error:
            print(error) 
main()
