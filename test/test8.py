import turtle, math

turtle.shape('turtle')


def p(x=3):
    z = 100
    a = 15
    b = 0
    for i in range(10):
        y = 360 / x
        for i in range(x):
            turtle.forward(z)
            turtle.left(y)
        # turtle.goto(a, b)
        x += 1
        # a += 15


def pp(x=5):
    z = 100
    a = 15
    b = 0
    for i in range(10):
        n = 360 / x
        j = 180 / x
        l = math.radians(j)
        m = math.sin(l)
        y = z / (2 * m)
        t = math.cos(l)
        r = z / (2 * t)
        for i in range(x):
            turtle.goto(r, y)
        #  * c
        x += 1


# while True:
pp()
