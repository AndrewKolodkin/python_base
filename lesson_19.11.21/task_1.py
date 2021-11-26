import re


def email_parse(email_address):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')

    if re.match(pattern, email_address) is not None:
        print('Проверка пройдена')
    else:
        print(f'Error, {email_address} not valid')
    return email_address


print(email_parse('Koloandrew2012@gmail.com'))
print(email_parse('Koloandrew2012@@mail.com'))