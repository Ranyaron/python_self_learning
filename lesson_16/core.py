# функция для создания файла
import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть.')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print('Данный файл или папка отсутствует.')


def copy_file(name, new_name):
    try:
        if os.path.isdir(name):
            shutil.copytree(name, new_name)
        else:
            shutil.copy(name, new_name)
    except FileNotFoundError:
        print('Данный файл или папка отсутствует.')


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_dir(name):
    try:
        os.chdir(name)
        print(f'Текущая директория изменилась на {name}:', os.getcwd())
    except FileNotFoundError:
        print('Данный каталог отсутствует.')


if __name__ == '__main__':
    create_file('text.dat')
    # create_file('text.dat', 'some text')
    # create_folder('new_f')
    # get_list()
    # get_list(True)
    delete_file('text.dat')
    # delete_file('new_f')
    # copy_file('new_f', 'new_2')
    # copy_file('text.dat', 'text_2.dat')
    # save_info('asd')
    # change_dir('')
