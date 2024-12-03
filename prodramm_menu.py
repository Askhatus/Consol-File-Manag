import os
import sys
import shutil

#os.mkdir('Alina') # создали папку
# os.rmdir('Alina') # удалили папку
# shutil.copy('Salmira.py', 'Salmira_copy.py') # создали копию файла 'Salmira'
print('Cодержимое рабочей директории - ', os.listdir())


for dirpath, dirnames, filenames in os.walk('.'):
    for dirname in dirnames:
        print('Папки - ', os.path.join(dirpath, dirname)) # просмотр только папок
    for filename in filenames:
        print('Файлы - ', os.path.join(dirpath, filename))# просмотр только файлов
print('Операционная система - ', sys.platform)

# создатель программы

# играть в викторину
import victoryna

# мой банковский счёт
import Salmira

# смена рабочей директории
# os.chdir()

print('Текущая рабочая директория - ', os.getcwd())

# выход
sys.exit(0)