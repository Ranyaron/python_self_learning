'''Создайте собственную программу «Адресная книга», работающую из командной
строки и позволяющую просматривать, добавлять, изменять, удалять
или искать контактные данные ваших знакомых. Кроме того, эта информация
также должна сохраняться на диске для последующего доступа.'''

class ab:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        print('Создан контакт: {} - {}'.format(self.name, self.number))

f = open('ab.txt', 'a')
x = input('Введите имя: ')
y = input('Введите номер телефона: ')
z = '\n' + x + ' - ' + y
f.write(z)
f.close()
ab(x, y)

# ab = {  # ab - address book
#     'name': 'Илья',
#     'age': '26'
# }

# del ab['name']  # Удаление пары ключ-значение
#
# print('{}'.format(len(ab)))
#
# for name, address in ab.items():
#     print('{} {}'.format(name, address))
#
# ab['family'] = 'Чечулин'   # Добавление пары ключ-значение
#
# if 'family' in ab:
#     print(ab['family'])

# x = input('Что Вы хотите сделать (введите №)?: \n1. Просмотреть\n2. Добавить\n3. Изменить\n4. Удалить\n5. Найти')
# x = '2'
#
# if x == '2':
#     # y = input('Введите категорию: ')
#     y = 'qwe'
#     # z = input('Введите наименование: ')
#     z = 'asd'
#     ab[y] = z

'''Подсказка
Создайте класс для хранения персональных данных.
Объекты визитных карточек храните в словаре, в котором имена контактов будут служить ключами.
Для длительного хранения этих объектов на жёстком диске воспользуйтесь модулем pickle.
Для добавления, изменения или удаления контактов применяйте встроенные методы словаря.'''
