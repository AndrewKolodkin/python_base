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


if __name__ == '__main__':
    code_val = str(input('Koд валюты? '))
    print(currency_rates(code_val))
