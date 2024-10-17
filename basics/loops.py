'===============================Циклы=============================='
"""
цикл - это блок кода который отрабатывает несколько раз
for - цикл который работает с итериркемыми объектами. Цикл заканчивает свою работу когда он доходит до последнего элемента
while - цикл который работает до тех пор пока условие верное (возвращает True)
"""



# for 
list1 = ['hello', 1, 2, 3, 4, 5, None, True, False, [1, 2, 3, 4]]

for element in list1:
    print(element)



for letter in 'hello world':
        print(letter)


# while 

# a = 11
# while a < 100: 
#     print(a) # чтобы остановить бесконечный цикл ctrl + c
#     a += 1 # a = a + 1 

# n = 0
# while n:
#      print('hello')
# не сработает потому что 0 это false


"==============================Ключевые слова в циклах===================="
# break - полностью останавливает работу цикла (выйти из цикла)
# continue - перейти к следуйщей итерации (пропустить текущую)

for i in range(10):
      # print(i)
    if i == 3:
        continue
    print(i) # 0
            # 1
            # 2
            # 4
            # 5
            # 6
            # 7
            # 8
            # 9

for i in range(100):
     if i == 67:
         break
     print(i)

for i in range(100):
     print(i)
     if i == 67:
         break
     
# Дан список list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 2, 3, 4, 5, 55, 5544, 1, 1, 1], сформируйте новый список в котором не будет 1, но удалять из исходного списка нельзя
# list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 2, 3, 4, 5, 55, 5544, 1, 1, 1]
# new_list = []

# for i in list1:
#      if i != 1:
#           new_list.append(i)
#     #  if i == 1:
#     #       continue
#     #  new_list.append(i)
#      print(new_list)

# Дан список list2 удалить все единицы из списка (СОЗДАВАТЬ СПИСОК НЕЛЬЗЯ)
list2 = [1, 1, 1, 1, 1, 1, 4, 55, 32, 23]

while 1 in list2:
     list2.remove(1)
print(list2)


# for i in list2:
# if i == 1:
#      list2.remove(1)
#      print(list2)




for i in range(10):
     for j in range(10):
          print(i, j)