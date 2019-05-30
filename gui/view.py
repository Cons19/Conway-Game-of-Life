import tkinter as tk


class GameOfLifeView:

    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Game Of Life")
        self.window.geometry("500x500")
        self.canvas = tk.Canvas(self.window, bg='green')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.create_grid)

    def create_grid(self, event=None):
        width = self.canvas.winfo_width()  # Get current width of canvas
        height = self.canvas.winfo_height()  # Get current height of canvas

        # make 100*100 = 10.000 squares
        # for i in range(0, width, 10):
        #     for j in range(0, height, 10):
        #         self.canvas.create_rectangle(i, j, i + 10, j + 10, fill='red', width=1)

        # make 100+100 = 200 lines
        for i in range(0, width, 10):
            for j in range(0, height, 10):
                self.canvas.create_line(i, j, width, j, width=1)
                self.canvas.create_line(i, 0, i, height, width=1)

        self.canvas.create_rectangle(50, 50, 50 + 10, 50 + 10, fill='blue', width=1)


# GOL = GameOfLifeView()
