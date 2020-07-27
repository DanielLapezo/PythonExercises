import os, shutil, send2trash

os.chdir('C:\\Users\\User\\Desktop')
for foldername, subfolders, filenames in os.walk('C:\\Users\\User\\Desktop\\THIS'):
    print ('Текущая папка - ' + foldername)

    for subfolder in subfolders:
        print('ПОДПАПКА ПАПКИ ' + foldername + ': ' + subfolder)

    for filename in filenames:
       if filename.endswith('.txt'):
           print('ФАЙЛ С РАСШИРЕНИЕМ TXT: ' + filename)

    print('')