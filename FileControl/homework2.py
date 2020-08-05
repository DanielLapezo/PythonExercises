#! python3
# Программа обходит дерево папок 
# выводит размер файлов и их абсолютные пути

import os, shutil

os.chdir('C:\\Users\\User\\Downloads\\Telegram_Desktop')
#print(os.getcwd())
for foldername, subfolders, filenames in os.walk('C:\\Users\\User\\Downloads\\Telegram_Desktop'):
    print('Текущая папка: ' + foldername )
    for subfolder in subfolders:
        print('Подпапка папки ' + foldername + ': ' + subfolder)
    for filename in filenames:
        print('Файл: ' + str(os.path.abspath(filename)) + '  Размер файла: ' + str(os.path.getsize(filename)) + 'B')