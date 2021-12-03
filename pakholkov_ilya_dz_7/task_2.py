"""
Скрипт создает из config.json стартер со следующей структурой:
    |--my_project
       |--settings
       |  |--__init__.py
       |  |--dev.py
       |  |--prod.py
       |--mainapp
       |  |--__init__.py
       |  |--models.py
       |  |--views.py
       |  |--templates
       |     |--mainapp
       |        |--base.html
       |        |--index.html
       |--authapp
       |  |--__init__.py
       |  |--models.py
       |  |--views.py
       |  |--templates
       |     |--authapp
       |        |--base.html
       |        |--index.html

в config.json данный стартер записан в виде словаря:

    {'my_new_project/settings/': ['__init__.py', 'dev.py', 'prod.py'],
    'my_new_project/mainapp/': ['__init__.py', 'models.py', 'views.py'],
    'my_new_project/mainapp/templates/mainapp/': ['base.html', 'index.html'],
    'my_new_project/authapp/': ['__init__.py', 'models.py', 'views.py'],
    'my_new_project/authapp/templates/authapp/': ['base.html', 'index.html']}
"""

import json
import os

ROOT = os.path.dirname(__file__)  # текущая позиция

with open('config.json', encoding='UTF-8') as f:  # читаем файл config.json и сохраняем словарь в переменную
    config = json.load(f)

for dir_path in config:  # создаем папки и файлы согласно заданной структуре
    full_path = os.path.join(ROOT, dir_path)
    os.makedirs(full_path, exist_ok=True)
    for file in config[dir_path]:
        with open(os.path.join(full_path, file), 'x', encoding='UTF-8'):
            pass
