from tkinter import Button

"""
File: Cell.py
Author: Nathan Robertson
A class that represents one cell on a grid. On click the cell changes color to indicate it is on/off depending
on previous state.
"""

IS_CELL_COLOR = "#99ff99"
IS_OBSTACLE_COLOR = "#555555"


class Cell(Button):
    def __init__(self, master, pos, **kwargs):
        self.current_color = IS_CELL_COLOR
        self.pos = pos
        super().__init__(master, kwargs)
        super().configure(command=self.change_color, bg=self.current_color)

    def change_color(self):
        if self.current_color == IS_CELL_COLOR:
            self.current_color = IS_OBSTACLE_COLOR
        else:
            self.current_color = IS_CELL_COLOR
        super().configure(bg=self.current_color)

    def is_obstacle(self) -> bool:
        return self.current_color == IS_OBSTACLE_COLOR
