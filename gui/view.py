import tkinter as tk


class GameOfLifeView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Game Of Life")
        self.window.geometry("1000x1000")
        self.canvas = tk.Canvas(self.window, bg='white', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.draw_grid)
        self.canvas.bind('<Button-1>', self.draw_square)
        self.start_button = tk.Button(self.window, text="Start", command=self.controller.start_action)
        self.start_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(self.window, text="Pause", command=self.controller.next_action)
        self.pause_button.pack(side=tk.LEFT)
        self.next_button = tk.Button(self.window, text="Next Frame", command=self.controller.next_action)
        self.next_button.pack(side=tk.LEFT)
        self.default_button = tk.Button(self.window, text="Default", command=self.controller.next_action)
        self.default_button.pack(side=tk.LEFT)
        self.random_button = tk.Button(self.window, text="Randomize", command=self.controller.next_action)
        self.random_button.pack(side=tk.LEFT)
        self.rules = []
        options = [
            "Speed",
            "1 per second",
            "2 per second",
            "3 per second",
            "5 per second",
            "10 per second",
            "20 per second",
            "30 per second"
        ]
        variable = tk.StringVar(self.window)
        variable.set(options[0])  # default value
        w = tk.OptionMenu(self.window, variable, *options)
        w.pack(side=tk.LEFT)

        self.rules_options = ["Change Rule"]
        variable = tk.StringVar(self.window)
        variable.set(self.rules_options[0])  # default value
        self.rules = self.controller.rules
        self.rules_options += self.rules
        print(self.controller.rules)
        self.rule_set_menu = tk.OptionMenu(self.window, variable, *self.rules_options)
        self.rule_set_menu.pack(side=tk.LEFT)

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

    def draw_next_frame(self):
        # clear canvas
        self.canvas.create_rectangle(0, 0, 1000, 1000, fill='white', width=0)
        width = self.canvas.winfo_width()  # Get current width of canvas
        height = self.canvas.winfo_height()  # Get current height of canvas

        # # make 100+100 = 200 lines
        # for i in range(0, width, 10):
        #    for j in range(0, height, 10):
        #        self.canvas.create_line(i, j, width, j, width=1, fill='#C0C0C0')
        #        self.canvas.create_line(i, 0, i, height, width=1, fill='#C0C0C0')

        # make squares
        for i in range(0, 29):
            for j in range(0, 29):
                if self.controller.current_frame[j][i]:  # array of arrays [j - row][i - column]
                    self.canvas.create_rectangle((i * 10)+1, (j * 10)+1, i * 10 + 10, j * 10 + 10, fill='black', width=0)

    def round_number(self, number):
        return int(number/10)*10

    def draw_square(self, event=None):
        # if the cell state is 0
        self.canvas.create_rectangle(self.round_number(event.x) + 1,
                                     self.round_number(event.y) + 1,
                                     self.round_number(event.x) + 10,
                                     self.round_number(event.y) + 10,
                                     fill='red',
                                     width=0)
        # else if the cell state is 0 draw a white rectangle
        self.temporary_state = self.controller.next_state

        for i in range(0, 10):
            for j in range(0, 10):
                if i == self.round_number(event.x)/10 and j == self.round_number(event.y)/10:
                    self.temporary_state[j][i] = 1
