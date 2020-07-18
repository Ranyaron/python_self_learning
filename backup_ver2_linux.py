import os
import time
import zipfile

target_dir = '/home/kukuepta/Dropbox/python_self_learning/backup'  # Каталог
source = '/home/kukuepta/Dropbox/python_self_learning/stuff'  # Путь до файлов архивации

today = target_dir + os.sep + time.strftime('%Y.%m.%d')
now = time.strftime('%H:%M:%S')
os.chdir(source)

# Добавляем к имени архива комментарий
comment = input('Введите комментарий --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Создаем папку (каталог), если ее нет
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан:', today)

# Архивация файлов
my_zip = zipfile.ZipFile(target, 'w')
len_dir_path = len(source)
try:
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            my_zip.write(file_path, file_path[len_dir_path:])
    print('Резервная копия успешно создана:', target)
    my_zip.close()
except ValueError:
    print('Создание резервной копии НЕ УДАЛОСЬ')
