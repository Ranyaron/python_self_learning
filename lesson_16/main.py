import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game import game

save_info('СТАРТ')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название файла.')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except FileExistsError:
            print('Такая папка уже есть.')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except FileNotFoundError:
            print('Данный файл или папка отсутствует.')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except FileNotFoundError:
            print('Данный файл или папка отсутствует.')
        else:
            copy_file(name, new_name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')

        print('cd - изменение директории')
        print('game - игра угадайка')
    elif command == 'cd':
        try:
            name = sys.argv[2]
        except FileNotFoundError:
            print('Данный каталог отсутствует')
        else:
            change_dir(name)
    elif command == 'game':
        game()

    save_info('КОНЕЦ')
