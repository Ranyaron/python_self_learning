#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_9_3():
    def right(x=1):
        for i in range(x):
            move_right()
            fill_cell()

    def down(x=1):
        for i in range(x):
            move_down()
            fill_cell()

    def left(x=1):
        for i in range(x):
            move_left()
            fill_cell()

    def up(x=1):
        for i in range(x):
            move_up()
            fill_cell()

    def upp(x=1):
        for i in range(x):
            right(2)
            down()
            up()
            right()

    def rightt(x=1):
        for i in range(x):
            down(2)
            left()
            right()
            down()

    def downn(x=1):
        for i in range(x):
            left(2)
            up()
            down()
            left()

    def leftt(x=1):
        for i in range(x):
            up(2)
            right()
            left()
            up()

    upp()
    a = 2
    b = 0
    z = 1

    def up_up(n=1):
        for i in range(n):
            move_left(a)
            upp()
            move_left(4)
            move_down()
            upp()

    m = 1
    while True:
        move_right()
        if wall_is_on_the_right():
            if 2 <= z:
                up_up(m)
                move_right(b)
                move_up()
                rightt()
                move_up()
                rightt()
                move_up(a)
                move_left()
                rightt()
                move_down(b)
                move_right()
                downn()
                move_right()
                downn()
                move_right(a)
                move_up()
                downn()
                move_left(b)
                move_down()
                leftt()
                move_down()
                leftt()
                move_down(a)
                move_right()
                leftt()
                move_down(a)
                move_left()
                break

            rightt()
            move_down()
            downn()
            move_left()
            leftt()
            move_down(3)
            break
        else:
            a += 1
            b += 1
            z += 1
            if a > 4:
                m += 1


if __name__ == '__main__':
    run_tasks()
