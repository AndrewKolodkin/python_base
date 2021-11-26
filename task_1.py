# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
import os

root_file = os.path.dirname(__file__)
dir_path = os.path.join('my_project')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
path_file = [os.path.join(dir_path, 'settings'), os.path.join(dir_path, 'mainapp'),
             os.path.join(dir_path, 'adminapp'), os.path.join(dir_path, 'authapp')]
for path in path_file:
    os.makedirs(os.path.join(root_file, path))
