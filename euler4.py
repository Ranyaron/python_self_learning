# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

def reverse(text):
    if text == text[::-1]:
        print('Palindrom {}'.format(text))
    # else:
    #     print('NO')
#
#
# reverse('9009')

# y = 10
# for x in range(10, 100):
#     z = x * y
#     z = str(z)
#     reverse(z)
#     if x == 100:
#         y += 1

def qwerty():
    y = 10
    for x in range(10, 100):
        z = x * y
        z = str(z)
        reverse(z)
        if x == 100:
            y += 1

while True:
    qwerty()

# for y in range(10, 100):
#     y = y + 0
#
# z = x * y
# z1 = str(z)
# while True:
#     if z == z[::-1]:
#         print('Palindrom')