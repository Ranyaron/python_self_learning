import turtle

turtle.speed('fastest')

def draw(l, n):
    if n == 0:
        turtle.forward(l)
        return

    x = l
    turtle.left(90)
    draw(x, n - 1)
    turtle.left(90)
    draw(x, n - 1)
    turtle.left(90)
    draw(x, n - 1)
    turtle.right(90)
    draw(x, n - 1)

# for i in range(4):
draw(5, 5)
