### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# duration = int(input('Введите количество секунд: '))
seconds = 0
hours = 0
minutes = 0
days = 0
flag = 10
while flag != 0:
    duration = int(input('Введите количество секунд: '))
    days = duration // 86400
    hours = (duration - (days * 86400)) // 3600
    minutes = (duration - ((days * 86400) + (hours * 3600))) // 60
    seconds = duration - ((days * 86400) + (hours * 3600) + (minutes * 60))
    if days == 0 and hours == 0 and minutes == 0:
        print(seconds, 'сек.')
    elif days == 0 and hours == 0:
        print(minutes, 'мин.', seconds, 'сек.')
    elif days == 0:
        print(hours, 'час.', minutes, 'мин.', seconds, 'сек.')
    else:
        print(days, 'дн.', hours, 'час.', minutes, 'мин.', seconds, 'сек.')
    flag -= 1