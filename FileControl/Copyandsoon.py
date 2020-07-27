import shutil, os
os.chdir('C:\\Users\\User\\Downloads')
for filename in os.listdir():
    if filename.endswith('.torrent'):
        #os.unlink(filename)
        print(filename)
