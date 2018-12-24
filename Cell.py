from tkinter import Button


class Cell(Button):
    def __init__(self, master, pos, **kwargs):
        self.FIRST_COLOR = "#99ff99"
        self.SECOND_COLOR = "#555555"
        self.current_color = self.FIRST_COLOR
        self.pos = pos
        super().__init__(master, kwargs)
        super().configure(command=self.callback, bg=self.current_color)

    def callback(self):
        if self.current_color == self.FIRST_COLOR:
            self.current_color = self.SECOND_COLOR
        else:
            self.current_color = self.FIRST_COLOR
        super().configure(bg=self.current_color)

    def is_obstacle(self) -> bool:
        return self.current_color == self.SECOND_COLOR
