import os
import shutil

ROOT = './'
dir_name = 'homeworks/lesson1'
dir_path = os.path.join(ROOT, dir_name)
if not os.path.exists(dir_path):
    # os.mkdir(dir_path)  # не создает путь из подпапок
    os.makedirs(dir_path)
else:
    # os.rmdir(dir_path)  # удаляет только пустую папку
    shutil.rmtree(dir_path)

# print(__file__)
# ROOT = os.path.dirname((__file__))
# print(ROOT)
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# for root, dirs, files in os.walk(ROOT):
#     # print(root)
#     # print(type(root))
#     # print(dirs)
#     # print(files)
#     for file in files:
#         # print(f'{root}/{file}')  # не кроссплатформенно
#         f_path = os.path.join(root, file)
#         print(f_path)
#         print(f_path, os.path.exists(f_path))
#         print(os.stat(f_path).st_size)
#         print(f_path, os.path.abspath(f_path))
#         print(os.path.split(f_path))  # способ разбить путь
#         f_path2, f_name = os.path.split(f_path)  # способ разбить путь
#         dirname = os.path.dirname(f_path)  # название папки из пути
#         filename = os.path.basename(f_path)  # название файла из пути
#         # print(dirname)
#         # print(filename)

# for item in os.scandir(ROOT):
#     # print(type(item))
#     print(item.name, item.is_dir())
#     print(item.name, item.is_file())
#     print(item.name, item.stat().st_size)

# files = os.listdir('./')
# for file in files:
#     print(file, os.path.isdir(file))
#     print(file, os.path.isfile(file))
#     print(type(file))
#     print(os.stat(file).st_size)
