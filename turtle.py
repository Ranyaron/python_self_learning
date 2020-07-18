import turtle

def move(a):
    turtle.forward(a)
    turtle.left(90)

def move(b):
    turtle.forward(b)
    turtle.left(90)

def drawSquareColor(a, b, color):
    turtle.color(color)
    turtle.begin_fill()
    move(a)
    move(b)
    move(a)
    move(b)
    turtle.end_fill()

turtle.speed(1)

drawSquareColor(200, 50, 'red')
turtle.goto(100, 70)
drawSquareColor(100, 150, 'blue')
