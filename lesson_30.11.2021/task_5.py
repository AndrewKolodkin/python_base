# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, num_1, num_2, *args):
        self.num_1 = num_1
        self.num_2 = num_2
        self.res = 'num_1 + nam_2 * i'

    def __add__(self, other):
        print(f'Сумма res_1 и res_2 равна')
        return f'res = {self.num_1 + other.num_1} + {self.num_2 + other.num_2} * i'

    def __mul__(self, other):
        print(f'Произведение res_1 и res_2 равно')
        return f'res = {self.num_1 * other.num_1 - (self.num_2 * other.num_2)} + {self.num_1 * other.num_1} * i'

    def __str__(self):
        return f'res = {self.num_1} + {self.num_2} * i'


res_1 = ComplexNumber(5, -4)
res_2 = ComplexNumber(10, 4)
print(res_1)
print(res_1 + res_2)
print(res_1 * res_2)