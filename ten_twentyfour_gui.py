import tkinter as tk
import ten_twentyfour as ten24


class Game(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.bind('<Left>', self.leftKey)
        self.bind('<Right>', self.rightKey)
        self.bind('<Up>', self.upKey)
        self.bind('<Down>', self.downKey)
        self.bind('<Button-1>', self.callback)
        self.draw()

    def draw(self):
        for row_index, row in enumerate(ten24.game_board):
            for cell_index, cell in enumerate(row):
                tk.Label(root, text=cell, width=10, height=5, relief='groove').grid(row=row_index, column=cell_index)
        self.master.after(100, self.draw)

    def callback(self, event):
        self.focus_set()
        print("clicked at", event.x, event.y)

    def leftKey(event):
        ten24.move_left()

    def rightKey(event):
        ten24.move_right()

    def upKey(event):
        ten24.move_up()

    def downKey(event):
        ten24.move_down()

root = tk.Tk()
app = Game(master=root)

app.mainloop()
