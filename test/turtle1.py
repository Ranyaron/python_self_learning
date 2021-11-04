import turtle

turtle.speed('fastest')


def draw(l, n):
    if n == 0:
        turtle.forward(l)
        return

    x = l / 3
    draw(x, n - 1)
    turtle.left(60)
    draw(x, n - 1)
    turtle.right(120)
    draw(x, n - 1)
    turtle.left(60)
    draw(x, n - 1)


for i in range(3):
    draw(250, 4)
    turtle.right(120)
