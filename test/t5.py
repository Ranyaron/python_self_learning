s = 1
while True:
    for i in range(100, 6789):
        if i % s == 0:
            s += 1
        elif i % s != 0:
            s = 1