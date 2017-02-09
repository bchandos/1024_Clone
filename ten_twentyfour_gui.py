import tkinter as tk
import ten_twentyfour as ten24
import math

class GameGUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        ten24.game_board_setup()
        self.cells = []
        self.grid()
        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)
        self.setup()
        self.draw()

    def setup(self):
        self.score_label = tk.Label(self.master, text='Score: {}'.format(ten24.GAME_SCORE), width=40, height=5, relief='raised')
        self.score_label.grid(row=5, columnspan = 4)
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
        self.score_label.configure(text=ten24.GAME_SCORE)
        if not ten24.GAME_OVER:
            self.after(100, self.draw)
        else:
            self.quit()

    def left_key(self, event):
        ten24.play_game('left')

    def right_key(self, event):
        ten24.play_game('right')

    def up_key(self, event):
        ten24.play_game('up')

    def down_key(self, event):
        ten24.play_game('down')

root = tk.Tk()
app = GameGUI(master=root)
app.mainloop()

print('GAME OVER!')
print(ten24.GAME_SCORE)
