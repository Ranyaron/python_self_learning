def is_simple_number(x):
    '''Определяет является ли число простым
    x - целое положительное число
    Если простое, то возвращает True,
    а иначе - False'''
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


print(is_simple_number(9))


def factorize_number(x):
    '''Раскладывает число на множетели.
    Печатает их на экран.
    x - целое положительное число.'''
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1


print(factorize_number(1024))
