from graphics import *

size_x = 800
size_y = 800
win = GraphWin("Физика", size_x, size_y)


# Начальное положение шарика
coordinates = Point(0, 400)

circle = Circle(coordinates, 10)
circle.draw(win)
circle.setFill('red')

# Скорость
velocity = Point(1, -2)

acceleration = Point(0, 0.1)


def add(point_1, point_2):
    new_point = Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point


def sub(point_1, point_2):
    new_point = Point(point_1.x - point_2.x, point_1.y - point_2.y)

    return new_point


def clear_window():
    rectangle = Rectangle(Point(0, 0), Point(size_x, size_y))
    rectangle.setFill('light green')
    rectangle.draw(win)


def draw_circle(coordinates):
    circle = Circle(coordinates, 10)
    circle.setFill('red')
    circle.draw(win)


def check_coordinates(coordinates, velocity):
    if coordinates.x < 0 or coordinates.x > size_x:
        velocity.x = -velocity.x

    if coordinates.y < 0 or coordinates.y > size_y:
        velocity.y = -velocity.y


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coordinates, center_coordinates):
    diff = sub(ball_coordinates, center_coordinates)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3 / 2)

    G = 2000

    return Point(-diff.x * G / distance_2, -diff.y * G / distance_2)


while True:
    # clear_window()
    circle.move(1, 1)
    acceleration = update_acceleration(coordinates, Point(400, 400))
    coordinates = add(coordinates, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coordinates(coordinates, velocity)
    time.sleep(0.01)
