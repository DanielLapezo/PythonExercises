#! python3
#! backUpToZip.py - Копирует папку вмесет со всем её содержимым
# в ZIP - файле с инкреминтируемым номером копии в имени файла.

import zipfile, os

def backuptozip(folder):
    # Создание резервной копии всего содержимого папки "folder"
    # в виде ZIP - файла.

    folder = os.path.abspath(folder) # убедиться в том, что
                                     # задан абсолютный путь
                                     # к файлу
    
    # Определить, какое имя файла должен использовать этот код,
    # исходя из имен уже существующих файлов.

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1 
    
    # Создание ZIP - файла.
    print('Создаётся файл %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Обход всего дерева папки и сжатие файлов, содержащихся
    # в каждой папке.
    for foldername, subfolders, filenames in os.walk(folder):
        print ('Добавление файлов из папки %s...' % (foldername))
        # Добавить в ZIP-файл текущую папку.
        backupZip.write(foldername)
        # Добавить в ZIP-файл все файлы из данной папки.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith('.zip') and filename.endswith('.zip'):
                continue # не создавать резервные копии
            backupZip.close()
            print('Готово')   

backuptozip('C:\\Users\\User\\Desktop\\TestFolder')          
                    