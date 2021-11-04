#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    x = 1
    while x < 3:
        if cell_is_filled():
            move_right()
            x += 1
        if not cell_is_filled():
            move_right()
            x = 1


if __name__ == '__main__':
    run_tasks()
