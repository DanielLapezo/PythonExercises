import send2trash, os
os.chdir('C:\\Users\\User\\Desktop')
baconFile = open('bacon.txt', 'a') #создаёт файл
baconFile.write('Bacon is not a vegetable')
baconFile.close()
send2trash.send2trash('bacon.txt')