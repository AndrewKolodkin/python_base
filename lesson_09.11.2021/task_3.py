# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования
# в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
print('*'* 100)
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
not_repeat_num = set()
var = set()
for elem in src:
    if elem not in var:
        not_repeat_num.add(elem)
    else:
        not_repeat_num.discard(elem)
    var.add(elem)
result = [el for el in src if el in not_repeat_num]
print(f'исходный список : {src} \nрезультат: {result}')
print('*'* 100)