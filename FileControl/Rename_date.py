#! python3
#Rename_date - переименовывает файлы, имена которых включают
#даты, указанные в американском формате (ММ-ДД-ГГГГ), приводя
#их в соответствие с европейским форматом дат (ДД-ММ-ГГГГ).

import shutil, os, re

os.chdir('C:\\Users\\User\\Desktop\\TestFolder')

#создание регулярного выражения, которому соответствуют имена
#файлов, содержащие даты в американском формате.
datePattern = re.compile(r"""^(.*?)     # весь текст перед датой
    ((0|1)?\d)-                         # одна или две цифры месяца 
    ((0|1|2|3)?\d)-                     # одна или две цифры числа
    ((19|20)\d\d)                       # четыре цифры года
    (.*?)$                              # весь текст после даты 
    """, re.VERBOSE)

#организация цикла по файлам в рабочем каталоге.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# Пропуск файлов с именами, не содержащим дат.
    if mo == None:
        continue

    # Получение отдельных частей имен файлов.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Формирование имен, соответствующих европейскому стилю 
    # указания дат.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Получение полных абсолютных путей к файлам.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Переименование файлов
    print('Заменяем имя "%s" именем "%s"...'
        % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)