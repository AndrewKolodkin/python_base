# Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_num_1 = (elem for elem in src)
list_num_2 = (elem for elem in src)
next(list_num_2)
result = (el for el_1, el in zip(list_num_1, list_num_2) if el_1 < el)
print('*'* 100)
print('result =', *result)
