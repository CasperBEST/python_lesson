import os
import shutil

root_dir = os.path.join(os.path.dirname(__file__), 'my_new_project')  # папка проекта
new_dir = os.path.join(os.path.dirname(__file__), 'my_new_project', 'templates')  # новая папка 'templates'

if not os.path.exists(new_dir):  # если папки нет - создаем новую папку
    os.mkdir(new_dir)

for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for d_ir in dirs:  # если находим папку 'templates'
            if not os.path.exists(os.path.join(new_dir, d_ir)):  # копируем подпапку в новую папку
                os.makedirs(os.path.join(new_dir, d_ir))
        for file in files:
            path_file = os.path.join(root, file)  # путь файла
            new_path_file = os.path.join(new_dir, os.path.basename(root))  # путь для копии файла
            if not os.path.dirname(path_file) == new_path_file:  # если файла нет - копируем
                shutil.copy(path_file, new_path_file)
