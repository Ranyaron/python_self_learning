fileName1 = input('введите дичь: ')
fileName2 = input('введите вторую дичь: ')

file1 = open(fileName1, 'r')
file2 = open(fileName2, 'w')

file2.write(file1.read())

file1.close()
file2.close()


# r - Чтение файла
# w - Перезапись файла
# a - Добавления в файл
#
# b - Binary mode
