from graphics import *

win = GraphWin("Практика: графические примитивы", 800, 600)
win.setBackground('light green')

upBackground = Rectangle(Point(800, 0), Point(0, 300))
upBackground.setFill('light blue')
upBackground.setWidth(0)
upBackground.draw(win)


def draw_sun(x=650, y=100, r=60, color='yellow', width=5, outline='light yellow'):
    '''Солнце.'''
    sun = Circle(Point(x, y), r)
    sun.setFill(color)
    sun.setWidth(width)
    sun.setOutline(outline)
    sun.draw(win)


def draw_house(x1=200, y1=200, x2=400, y2=400, color_house='grey', width_house=0, outline_house='grey',
               color_window='yellow', width_window=2, outline_window='brown', width_jumper=3,
               outline_jumper='brown', color_roof='brown', width_roof=3, outline_roof='brown'):
    '''Дом с окном и рамами, а также с крышей.'''
    house = Rectangle(Point(x1, y1), Point(x2, y2))
    house.setFill(color_house)
    house.setWidth(width_house)
    house.setOutline(outline_house)
    house.draw(win)

    window = Rectangle(Point(x1 + 50, y1 + 50), Point(x2 - 50, y2 - 50))
    window.setFill(color_window)
    window.setWidth(width_window)
    window.setOutline(outline_window)
    window.draw(win)

    jumper1 = Line(Point(x1 + 100, y1 + 50), Point(x2 - 100, y2 - 50))
    jumper1.setWidth(width_jumper)
    jumper1.setOutline(outline_jumper)
    jumper1.draw(win)

    jumper2 = Line(Point(x1 + 50, y1 + 100), Point(x2 - 50, y2 - 100))
    jumper2.setWidth(width_jumper)
    jumper2.setOutline(outline_jumper)
    jumper2.draw(win)

    roof = Polygon(Point(x1 - 25, y1), Point(x1 + 100, y1 - 125), Point(x2 + 25, y2 - 200))
    roof.setFill(color_roof)
    roof.setWidth(width_roof)
    roof.setOutline(outline_roof)
    roof.draw(win)


def draw_tree(x1=450, y1=450, x2=575, y2=325, x3=700, y3=450, color='green', width=1, outline='brown',
              color_trunk='brown', width_trunk=0, outline_trunk='brown'):
    '''Елка.'''
    tree = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    tree.setFill(color)
    tree.setWidth(width)
    tree.setOutline(outline)
    tree.draw(win)

    tree = Polygon(Point(x1 + 25, y1 - 50), Point(x2, y2 - 25), Point(x3 - 25, y3 - 50))
    tree.setFill(color)
    tree.setWidth(width)
    tree.setOutline(outline)
    tree.draw(win)

    tree = Polygon(Point(x1 + 50, y1 - 100), Point(x2, y2 - 50), Point(x3 - 50, y3 - 100))
    tree.setFill(color)
    tree.setWidth(width)
    tree.setOutline(outline)
    tree.draw(win)

    tree = Polygon(Point(x1 + 75, y1 - 145), Point(x2, y2 - 70), Point(x3 - 75, y3 - 145))
    tree.setFill(color)
    tree.setWidth(width)
    tree.setOutline(outline)
    tree.draw(win)

    trunk = Rectangle(Point(x1 + 100, y1), Point(x2 + 25, y2 + 150))
    trunk.setFill(color_trunk)
    trunk.setWidth(width_trunk)
    trunk.setOutline(outline_trunk)
    trunk.draw(win)


draw_sun()
draw_house(x1=175, y1=225, x2=375, y2=425)
draw_tree()

win.getMouse()
win.close()
