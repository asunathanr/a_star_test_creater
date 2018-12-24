from tkinter import *
from Cell import Cell

"""
File: grapher.py
Author: Nathan Robertson
Purpose:
    Make graphical test cases for A* algorithm.
"""

master = Tk()
master.configure(background="#222222")
grid = {}

rows = 20
cols = 20
indices = []
buttons = []

for x in range(0, rows):
    for y in range(0, cols):
        indices.append((x, y))

for coord in indices:
    x, y = coord
    b = Cell(master, coord, text="",  width=1, height=1)
    b.grid(row=x, column=y)
    buttons.append(b)


def capture_grid():
    obstacles = []
    for button in buttons:
        if button.is_obstacle():
            obstacles.append(button.pos)
    return obstacles


def serialize_grid():
    print(capture_grid())


Button(master, text="Capture Grid", command=serialize_grid).grid(row=rows + 1, column=cols + 1)

mainloop()
