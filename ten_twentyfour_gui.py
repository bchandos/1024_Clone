import tkinter as tk
import ten_twentyfour as ten24
import math

class Game(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.cells = []
        self.grid()
        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)
        self.setup()
        self.draw()

    def setup(self):
        for row_index, row in enumerate(ten24.game_board):
            for cell_index, cell in enumerate(row):
                c = tk.Label(self.master, text=cell, width=10, height=5, relief='groove')
                c.grid(row=row_index, column=cell_index)
                self.cells.append(c)

    def draw(self):
        for cell_index, cell in enumerate(self.cells):
            row_index = int(math.floor(cell_index/4))
            col_index = int(cell_index - (row_index * 4))
            cell.configure(text='')
            cell.configure(text=ten24.game_board[row_index][col_index])

        # for row_index, row in enumerate(ten24.game_board):
        #     for cell_index, cell in enumerate(row):
        #         self.cells[row_index + (cell_index * len(row))].configure(text=cell)
        self.after(100, self.draw)

    def left_key(self, event):
        ten24.move_left()
        while not ten24.spawn_number():
            pass

    def right_key(self, event):
        ten24.move_right()
        while not ten24.spawn_number():
            pass

    def up_key(self, event):
        ten24.move_up()
        while not ten24.spawn_number():
            pass

    def down_key(self, event):
        ten24.move_down()
        while not ten24.spawn_number():
            pass

root = tk.Tk()
app = Game(master=root)
app.mainloop()
print(ten24.GAME_SCORE)
