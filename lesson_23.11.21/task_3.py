class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def name_surname(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


worker = Position('Иван', 'Иванов', 'Учитель', 9500, 19000)
print(worker.name_surname())
print(worker.position)
print(worker.get_total_income())
