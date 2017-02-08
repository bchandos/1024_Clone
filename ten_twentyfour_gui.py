import tkinter as tk
import ten_twentyfour as ten24

class Game(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.bind('<Left>', self.leftKey)
        self.bind('<Right>', self.rightKey)
        self.draw()

    def draw(self):
        # self.new_game = tk.Button(self, text='New Game', command=ten24.new_game())
        # self.new_game.pack(side='top')
        for row_index, row in enumerate(ten24.game_board):
            for cell_index, cell in enumerate(row):
                tk.Label(root, text=cell, width=10, height=5, relief='groove').grid(row=row_index, column=cell_index)
        # self.after(10, self.draw)

        # self.quit = tk.Button(self, text='QUIT', command=root.destroy)
        # self.quit.pack(side='bottom')

    def leftKey(event):
        ten24.move_left()

    def rightKey(event):
        ten24.move_right()

root = tk.Tk()
app = Game(master=root)
app.mainloop()
