lst_employee = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                'директор аэлита']

for i in range(len(lst_employee)):
    name_lst = ''.join(lst_employee[i])
    name = name_lst.rpartition(' ')[-1]
    print('Привет', name.capitalize())
