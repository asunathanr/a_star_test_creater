from tkinter import Button


class Cell(Button):
    def __init__(self, master, pos, **kwargs):
        self.IS_CELL_COLOR = "#99ff99"
        self.IS_OBSTACLE_COLOR = "#555555"
        self.current_color = self.IS_CELL_COLOR
        self.pos = pos
        super().__init__(master, kwargs)
        super().configure(command=self.callback, bg=self.current_color)

    def callback(self):
        if self.current_color == self.IS_CELL_COLOR:
            self.current_color = self.IS_OBSTACLE_COLOR
        else:
            self.current_color = self.IS_CELL_COLOR
        super().configure(bg=self.current_color)

    def is_obstacle(self) -> bool:
        return self.current_color == self.IS_OBSTACLE_COLOR
