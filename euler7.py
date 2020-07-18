'''Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?'''

lis = []
n = 2
for i in range(2, 1000000000):
    x = 2
    if i % x == 0 and i > 2:
        continue
    x += 1
    if i % x == 0 and i > 5:
        continue
    x += 2
    if i % x == 0 and i > 9:
        continue
    x += 2
    if i % x == 0 and i > 13:
        continue
    lis.append(i)

print(lis[100])
