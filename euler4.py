# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

def reverse(text):
    if text == text[::-1]:
        print('Palindrom')
    else:
        print('NO')


def a(x):
    count = x
    for i in range(1, 100):
        count += i
    return count


def b(y):
    count = y
    for i in range(1, 100):
        count += i
    return count

aa = a(1)
bb = b(1)

zz = aa*bb
print(zz)