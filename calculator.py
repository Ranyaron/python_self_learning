def calculator():
    what = input('Введите +, -, *, /: ')
    if what == '+' or what == '-' or what == '*' or what == '/':
        a = int(input('Введите 1-ое число: '))
        b = int(input('Введите 2-ое число: '))
        if what == '+':
            print('Result: ' + str(a + b))
        elif what == '-':
            print('Result: ' + str(a - b))
        elif what == '*':
            print('Result: ' + str(a * b))
        else:
            print('Result: ' + str(a / b))
        calculatorEnd()
    else:
        print('Попробуйте снова!')
        calculator()


def calculatorEnd():
    qwerty = input('Нужно еще что-то посчитать? (y/n): ')
    if qwerty == 'Y' or qwerty == 'y':
        calculator()
    elif qwerty == 'N' or qwerty == 'n':
        print('Программа завершена.')
    else:
        print('Попробуйте снова!')
        calculatorEnd()


while True:
    calculator()
    break
    calculatorEnd()