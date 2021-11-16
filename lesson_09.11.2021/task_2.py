# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Игорь', 'Василий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen_klass():
    tutor = (elem for elem in tutors)
    klass = (elem for elem in klasses)
    for school in zip(klass, tutor):
        yield school[::-1]
    for empty in tutor:
        yield empty, None


klass_generator = gen_klass()
for i in klass_generator:
    print(i)
print(type(gen_klass()))
print('*'* 100)