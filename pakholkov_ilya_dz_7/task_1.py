"""
Скрипт создает заготовку для проекта со следующей структурой папок:
| --my_project
    |--settings
    |--mainapp
    |--adminapp
    |--authapp
"""

import os

ROOT = os.path.dirname(__file__)  # текущая позиция

root_dir_project = 'my_project'  # корневая папка проекта
sub_dir = [os.path.join(root_dir_project, 'settings'),  # подпапки
           os.path.join(root_dir_project, 'mainapp'),
           os.path.join(root_dir_project, 'adminapp'),
           os.path.join(root_dir_project, 'authapp')]
for path_dir in sub_dir:
    os.makedirs(os.path.join(ROOT, path_dir), exist_ok=True)  # не выдает ошибку, если папки уже существуют
