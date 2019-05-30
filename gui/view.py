import numpy as np
import tkinter as tk


class GameOfLifeView:

    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Game Of Life")
        self.window.geometry("100x100")
        self.canvas = tk.Canvas(self.window, bg='white', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.draw_grid)
        # self.canvas.bind('<Button-1>', self.draw_square)
        # self.canvas.bind('<Button-1>', self.save_frame)
        self.next_button = tk.Button(self.window, text="Next", command=self.controller.next_action)
        # self.next_button = tk.Button(self.window, text="Next", self.save_frame)
        self.next_button.pack()
        self.next_button.place(height=30, width=60)
        # self.temporary_state = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        # self.draw_next_frame()

    def draw_grid(self, event=None):
        width = self.canvas.winfo_width()  # Get current width of canvas
        height = self.canvas.winfo_height()  # Get current height of canvas

        # make 100+100 = 200 lines
        for i in range(0, width, 10):
            for j in range(0, height, 10):
                self.canvas.create_line(i, j, width, j, width=1, fill='#C0C0C0')
                self.canvas.create_line(i, 0, i, height, width=1, fill='#C0C0C0')
        # self.draw_square()
        self.draw_next_frame()

    # def draw_square(self, event=None):
    #     self.canvas.create_rectangle(self.roundNumber(event.x)+1,
    #                                  self.roundNumber(event.y)+1,
    #                                  self.roundNumber(event.x) + 10,
    #                                  self.roundNumber(event.y) + 10,
    #                                  fill='red',
    #                                  width=0)
    #     print('draw_square')
    #     print(event.x)
    #     print(event.y)
    #     print(self.roundNumber(event.x))
    #     print(self.roundNumber(event.y))
    #     self.temporary_state = self.controller.next_state
    #     print('view - draw_square - self.temporary_state')
    #     for i in range(0, 10):
    #         for j in range(0, 10):
    #             if i == self.roundNumber(event.x)/10 and j == self.roundNumber(event.y)/10:
    #                 self.temporary_state[j][i] = 1
    #     print(self.temporary_state)

    def draw_next_frame(self):
        # clear canvas
        self.canvas.create_rectangle(0, 0, 1000, 1000, fill='white', width=0)
        width = self.canvas.winfo_width()  # Get current width of canvas
        height = self.canvas.winfo_height()  # Get current height of canvas

        # make 100+100 = 200 lines
        for i in range(0, width, 10):
            for j in range(0, height, 10):
                self.canvas.create_line(i, j, width, j, width=1, fill='#C0C0C0')
                self.canvas.create_line(i, 0, i, height, width=1, fill='#C0C0C0')
        # make squares
        for i in range(0, 10):
            for j in range(0, 10):
                # if self.controller.current_frame[j][i]:  # array of arrays [j - row][i - column]
                if self.controller.current_frame[j][i]:  # array of arrays [j - row][i - column]
                    self.canvas.create_rectangle((i * 10)+1, (j * 10)+1, i * 10 + 10, j * 10 + 10, fill='black', width=0)

    def roundNumber(self, number):
        return int(number/10)*10
        # print(int(number/10)*10)

# GOL = GameOfLifeView()
