# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
import requests


def currency_rates(val):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding='Windows-1251')
    res = None
    if val not in content:
        return res
    else:

        for el in content.split('<Name>')[1:]:
            # print(el)
            for el_1 in el.split('</Value>')[:1]:
                res = round(float(el_1.split('<Value>')[1].replace(',', '.')), 2)
                return f'Курс валют: {res} руб'
                # print(f'Курс валют: {res} руб')


if __name__ == '__main__':
    code_val = str(input('Koд валюты? '))
    print(currency_rates(code_val))
