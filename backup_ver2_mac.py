import os
import time
import zipfile

target_dir = r'/Users/evgenia/Dropbox/python/backup'  # Путь в каталог
source = r'/Users/evgenia/Dropbox/python/stuff'  # Путь до файлов архивации

today = target_dir + os.sep + time.strftime('%Y.%m.%d')
now = time.strftime('%H.%M.%S')
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
    print('Каталог успешно создан', today)

# Архивация файлов
zip = zipfile.ZipFile(target, 'w')
try:
    for x in os.listdir():
        zip.write(x, compress_type=zipfile.ZIP_DEFLATED)
    print('Резервная копия успешно создана в', target)
    zip.close()
except:
    print('Создание резервной копии НЕ УДАЛОСЬ')
