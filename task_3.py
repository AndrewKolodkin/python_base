# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

for i in range(1, 101):
    if i % 10 == 1 and i != 11:
        print(i, 'процент')
    elif (i % 10 == 2 and i != 12) or (i % 10 == 3 and i != 13) or (i % 10 == 4 and i != 14):
        print(i, 'процента')
    else:
        print(i, 'процентов')