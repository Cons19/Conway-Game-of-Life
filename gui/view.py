import tkinter as tk


class GameOfLifeView:

    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Game Of Life")
        self.window.geometry("500x500")
        self.canvas = tk.Canvas(self.window, bg='white', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.draw_grid)
        self.canvas.bind('<Button-1>', self.draw_square)

    def draw_grid(self, event=None):
        width = self.canvas.winfo_width()  # Get current width of canvas
        height = self.canvas.winfo_height()  # Get current height of canvas

        # make 100*100 = 10.000 squares
        # for i in range(0, width, 10):
        #     for j in range(0, height, 10):
        #         self.canvas.create_rectangle(i, j, i + 10, j + 10, fill='red', width=1)

        # make 100+100 = 200 lines
        for i in range(0, width, 10):
            for j in range(0, height, 10):
                self.canvas.create_line(i, j, width, j, width=1, fill='#C0C0C0')
                self.canvas.create_line(i, 0, i, height, width=1, fill='#C0C0C0')
        # self.draw_square()

    def draw_square(self, event=None):
        self.canvas.create_rectangle(self.roundNumber(event.x),
                                     self.roundNumber(event.y),
                                     self.roundNumber(event.x) + 10,
                                     self.roundNumber(event.y) + 10,
                                     fill='black',
                                     width=1)

    def roundNumber(self, number):
        return int(number/10)*10
        # print(int(number/10)*10)

# GOL = GameOfLifeView()
