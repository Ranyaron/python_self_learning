#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    for i in range(1):
        if not wall_is_on_the_right():
            move_right()
        elif not wall_is_on_the_left():
            move_left()
        elif not wall_is_above():
            move_up()
        else:
            move_down()


if __name__ == '__main__':
    run_tasks()
