'==================================Set================================'
# Множество(set) - изменяемый неупорядоченный итерируемый неиндексируемый тип данных предназначенный для хранения уникальных значений. Множества могут хранить в себе только не изменяемые типы данных



set = {1, 2, 3, 4}
set2 = {1, 2, 2, 2, 2, 2, 2}
print(set2) # {1, 2}



set3 = {(1, 2, 3), 1, 2, 3}
print(set3) # {1, 2, 3, (1, 2, 3)}
set4 = {1, 2, 1, 1, True, False, 0}
print(set4) # {False, 1, 2}
'============================FIFO / LIFO==============================='

# FIFO - First in first out
# LIFO - last in first out


'============================Методы set================================'
# print(dir(set2))

# add() - добавляет элементы в set
set1 = {1, 2, 3, 4, 5}
set1.add(None)
set1.add(10)
print(set1) # {1, 2, 3, 4, 5, None, 10}

# pop() - удаляет и возвращает случайный элемент из set (но есть принцип FIFO)
set1 = {1, 2, 3}
popped = set1.pop()
set1.pop()
print(set1, popped)

# remove() - удаляет элемент из set по значению если указанного элемента нет в set то выдаст error
set3 = {1, 2, 3}
set3.remove(2)
set3.remove(3)
# set3.remove(5) # Key error
print(set3)

# difference() (-) - находит отличия в двух множествах
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.difference(set2)) # {1, 2}
print(set1 - set2) # {1, 2}

# symmetric_difference() - возвращает элементы уникальные для друг друга (set1 и set2)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2)) # {1, 2, 4, 5}

#intersection() - (&) -  находит пересечения в двух множеставх
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {6, 7, 8, 9, 10, 11, 12}
print(set1.intersection(set2)) # {8, 9, 6, 7}
print(set1 & set2) # {8, 9, 6, 7}

print(dir(set1))