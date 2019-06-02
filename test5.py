def powersum(power, *args):
    '''Возвращает сумму аргументов, возведённых в указанную степень.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total


powersum(2, 3, 4)
