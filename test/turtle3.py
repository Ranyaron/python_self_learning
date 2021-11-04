import turtle


def draw(l, n):
    if n == 0:
        turtle.forward(l)
        return

    x = l
    # y = 45*2
    turtle.left(90)
    draw(x, n - 1)
    turtle.right(90)
    draw(x, n - 1)

# for i in range(4):
draw(50, 10)
