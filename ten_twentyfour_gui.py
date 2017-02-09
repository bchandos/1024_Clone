import tkinter as tk
import ten_twentyfour as ten24


class Game(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.master.bind('<Left>', self.leftKey)
        self.master.bind('<Right>', self.rightKey)
        self.master.bind('<Up>', self.upKey)
        self.master.bind('<Down>', self.downKey)
        self.draw()

    def draw(self):
        for row_index, row in enumerate(ten24.game_board):
            for cell_index, cell in enumerate(row):
                tk.Label(root, text=cell, width=10, height=5, relief='groove').grid(row=row_index, column=cell_index)
        self.master.after(100, self.draw)

    def leftKey(self, event):
        ten24.move_left()
        ten24.spawn_number()

    def rightKey(self, event):
        ten24.move_right()
        ten24.spawn_number()

    def upKey(self, event):
        ten24.move_up()
        ten24.spawn_number()

    def downKey(self, event):
        ten24.move_down()
        ten24.spawn_number()

root = tk.Tk()
app = Game(master=root)
app.mainloop()
