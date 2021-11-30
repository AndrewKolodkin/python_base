# Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).А
# также методы: go, stop, turn(direction), которые должны сообщать, что
# машина поехала, остановилась, повернула(куда); опишите
# несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля; для классов TownCar и WorkCar
# переопределите метод show_speed.При значении скорости свыше 60(TownCar)
# и 40(WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.Выполните доступ
# к атрибутам, выведите результат.Вызовите методы и покажите результат.
class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Автомобиль {self.name} цвет автомобиля {self.color}')

    def go(self, speed):
        self.speed = speed
        print(f'Автомобиль {self.name} скорость автомобиля {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        if direction == 'на лево' or direction == 'на право':
            print(f'Автомобиль марки {self.name} повернул {direction}')
        else:
            print(f'Автомобиль марки {self.name} может поворачивать на лево или на право')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль марки {self.name}, вы превысили скорость разрешенную в городе, снижайте скорость')
        else:
            print(f'Скорость автомобиля {self.name}: {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль марки {self.name}, вы превысили скорость разрешенную в городе')
        else:
            print(f'Скорость автомобиля {self.name}: {self.speed}')


class PoliceCar(Car):
    is_police = True


car_town = TownCar('Audi', 'белый', 30)
car_town.go(61)
car_town.turn('на лево')
car_town.show_speed()
car_town.stop()
print('*'* 50)
work_town = WorkCar('Камаз', 'синий', 20)
work_town.go(60)
work_town.turn('на право')
work_town.show_speed()
work_town.stop()