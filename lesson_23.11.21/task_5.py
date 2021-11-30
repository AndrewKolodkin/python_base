# Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    def __init__(self, title='Инструмент для рисования'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Для рисования выбран  {self.title} ручка!')


class Pensil(Stationery):
    def draw(self):
        print(f'Для штриха  {self.title} карандаш!')


class Handle(Stationery):
    def draw(self):
        print(f'Обводка контура  {self.title} маркер!')


brush = Stationery()
brush.draw()
brush_pen = Pen('Erich Krause')
brush_pen.draw()
brush_pensil = Pensil('TM')
brush_pensil.draw()
