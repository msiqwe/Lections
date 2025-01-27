'================================Tuple======================================'
# кортеж - неизменяемый индексируемый уопрядоченный итерируемый тип данных предназначенный для хранения любых данных в определенном порядке (по сути не отличается от списков просто он не изменяемый поэтому занимает меньше памяти)


# литералы тюпла - НЕ СКОБКИ, а запятые
tuple1 = (1, 2, 3, 3, 3, 3, 3)
print(tuple1)
print(type(tuple1)) # <class 'tuple'>
tuple2 = (4)
print(type(tuple2)) # <class 'int'>
tuple3 = (4, )
print(type(tuple3)) # <class 'tuple'>
tuple4 = 1, 2, 3 # (1, 2, 3)
print(tuple4)
print(type(tuple4)) # <class 'tuple'>
tuple6 = (1, 2, 3, 4, 5, ['hello', 1])
tuple6[-1].append('world')
print(tuple6) # (1, 2, 3, 4, 5, ['hello', 1, 'world'])

'=============================Методы tuple================================='
# count() - это метод который считает колво принятого элемента в кортеже
tuple1 = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 5, 66, 6666, 5)
print(tuple1.count(1)) # 13


# index() - возвращает индекс первого вхождения принятого элемента
tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple2.index(4)) # 3
print(tuple2.index(322423424)) # ValueError: tuple.index(x): x not in tuple