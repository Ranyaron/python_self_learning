import turtle, math

turtle.shape('turtle')


def p(a=1):
    b = 0.1
    c = b * (180 / 3.14)
    for i in range(1000):
        d = a * b
        turtle.forward(d)
        turtle.right(c)
        b += 0.1


# p()


def p(a=5):
    b = 0.1
    for i in range(1000):
        c = a * b
        x = math.cos(b) * c
        y = math.sin(b) * c
        turtle.goto(x, y)
        b += 0.1


p()
