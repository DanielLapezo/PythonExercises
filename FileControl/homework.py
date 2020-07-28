#! python3
# Программа ищет файлы с расширением '.jpg' и перемещает их в отдельную папку

import os, shutil

os.chdir('C:\\Users\\User\\Downloads')
#print(os.getcwd())
#os.mkdir('C:\\Users\\User\\Downloads\\документы')

for foldername, subfolders, filenames in os.walk('C:\\Users\\User\\Downloads'):
    print('Текущая папка: ' + foldername )
    for subfolder in subfolders:
        print('Подпапка папки ' + foldername + ': ' + subfolder)
    for filename in filenames:
        if (filename.endswith('.rar')) or (filename.endswith('.djvu')) or (filename.endswith('.ppsx')):
            print('Файл с расширением ".jpg": ' + filename)
  #shutil.move(filename, 'C:\\Users\\User\\Downloads\\документы')
    
