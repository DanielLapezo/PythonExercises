import zipfile, os 

os.chdir('C:\\Users\\User\\Desktop')
exampleZip = zipfile.ZipFile('exzip.zip')
print(exampleZip.namelist())
