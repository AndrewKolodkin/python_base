# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число(вещественные не трогаем) кавычками(
# добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём
# до двух целочисленных разрядов:

str_msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_msg = []

for i in range(len(str_msg)):
    if str_msg[i].isdigit() or not str_msg[i].isalnum():
        if len(str_msg[i]) == 1:
            a = f'{int(str_msg[i]):02d}'
            list_msg.append(a)
        elif str_msg[i].isdigit() or not str_msg[i].isalnum():
            list_msg.append(str_msg[i])
        else:
            list_msg.append(str_msg[i])
print(list_msg)
