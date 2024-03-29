from zipfile import ZipFile
from os import mkdir

line = '------------------------------'


def generator(string):
    for word in string:
        passwd = word.replace('\n', '')
        archive.setpassword(passwd.encode())
        try:
            archive.extractall(directory)
        except:
            yield '[False]: ' + passwd
        else:
            yield line + '\n[True]: ' + passwd
            return


directory = 'extract_archive'
try:
    mkdir(directory)
except FileExistsError:
    pass

print(line)

with open(input('Dictionary: '), errors='ignore') as dictionary:
    with ZipFile(input('Archive: ')) as archive:
        print(line)
        for password in generator(dictionary):
            print(password)

print(line)
