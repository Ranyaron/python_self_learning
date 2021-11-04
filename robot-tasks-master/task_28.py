#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    x = 1
    while x < 5:
        if cell_is_filled():
            move_right()
            x += 1
        if not cell_is_filled():
            move_right()


if __name__ == '__main__':
    run_tasks()
