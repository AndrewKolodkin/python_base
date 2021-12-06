# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class StorageEquipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_item = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            item = input(f'Введите наименование ')
            item_price = int(input(f'Введите цену за ед '))
            item_amount = int(input(f'Введите количество '))
            descript = {'Модель устройства': item, 'Цена за ед': item_price, 'Количество': item_amount}
            self.my_item.update(descript)
            self.my_store.append(self.my_item)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StorageEquipment.reception(self)


class Printer(StorageEquipment):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StorageEquipment):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StorageEquipment):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


item_1 = Printer('Samsung', 6500, 5, 10)
item_2 = Scanner('Phizer', 14000, 5, 10)
print(item_1.reception())
print(item_2.reception())
print(item_1.to_print())
print(item_2.reception())
