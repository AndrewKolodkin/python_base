# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0),
# например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
import os

ROOT = os.path.dirname(__file__)
data_path = os.path.join(ROOT, 'some_data')
res = {0: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0}
keys = [0, 100, 1000, 10000, 100000]
for root, dirs, files in os.walk(data_path):
    for file in files:
        stat_size = os.stat(os.path.join(root, file)).st_size
        if stat_size == 0:
            res[0] += 1
            continue
        for i, key in enumerate(keys):
            if i == len(keys) - 1:
                print('Большой файл', _file)
                break
            if key < stat_size <= keys[i + 1]:
                res[keys[i + 1]] += 1
                break
print(res)
