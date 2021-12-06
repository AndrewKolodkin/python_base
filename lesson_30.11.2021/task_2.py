# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class Exception:
    def __init__(self, divisible, divider):
        self.divisible = divisible
        self.divider = divider

    @staticmethod
    def division_by_zero(divisible, divider):
        try:
            return (divisible / divider)
        except:
            return (f'На ноль делить нельзя')


div = Exception(10, 100)
print(div.division_by_zero(16, 0))
print(div.division_by_zero(8, 0.1))
print(div.division_by_zero(50, 0))
