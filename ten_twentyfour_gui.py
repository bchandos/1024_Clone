import tkinter as tk
from tkinter import messagebox
import ten_twentyfour as ten24
from math import floor


class GameGUI(tk.Frame):
    """ Creates 1024 game UI and define keybindings
        Game logic is handled in ten_twentyfour.py
        Extends the tkinter Frame object """

    def __init__(self, master=None):
        # initialize the tk.Frame object with same root
        super().__init__(master)
        ten24.game_board_setup()
        # one-dimensional list containing tk.Lable widgets
        self.cells = []
        self.score_label = None
        self.grid()
        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)
        self.setup()
        self.draw()

    def setup(self):
        # Setup the window by creating a 4x4 grid, and adding each tile as tk.Label
        # to list, while populating with initial values of game_board.
        for row_index, row in enumerate(ten24.game_board):
            for cell_index, cell in enumerate(row):
                c = tk.Label(self.master, text=cell, width=10, height=5, relief='groove')
                c.grid(row=row_index, column=cell_index)
                self.cells.append(c)
        self.score_label = tk.Label(self.master, text='Score: {}'.format(ten24.GAME_SCORE),
                                    width=40, height=5, relief='raised')
        self.score_label.grid(row=5, columnspan=4)

    def draw(self):
        # Main drawing loop. Iterates over list of labels,
        # clears current values, looks up new value in game_board
        for cell_index, cell in enumerate(self.cells):
            row_index = int(floor(cell_index / 4))
            col_index = int(cell_index - (row_index * 4))
            cell.configure(text='')
            cell.configure(text=ten24.game_board[row_index][col_index])
        self.score_label.configure(text=ten24.GAME_SCORE)
        if not ten24.GAME_OVER:
            self.after(100, self.draw)
        else:
            messagebox.showinfo('Game Over!', 'Your game has ended and you are something of a failure. '
                                              f'Your final score was {ten24.GAME_SCORE}!')
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
root.title('Totally Not 2048')
app = GameGUI(master=root)
app.mainloop()
