import tkinter as tk
from tkinter import *


class GameOfLifeView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("C&P's Game Of Life")
        self.window.geometry("1000x705")
        # change

        self.rules = []
        self.rules_options = ["Change Rule"]
        self.default_rule_text = tk.StringVar(self.window)
        self.default_rule_text.set(self.rules_options[0])  # default value
        self.rules = self.controller.rules
        self.rules_options += self.rules

        self.patterns = []
        self.patterns_options = ["Default patterns"]
        self.default_pattern_text = tk.StringVar(self.window)
        self.default_pattern_text.set(self.patterns_options[0])
        self.patterns = self.controller.patterns
        self.patterns_options += self.patterns

        # GUI Frames
        self.body_frame = Frame(self.window)
        self.body_frame.pack(side=TOP, fill=BOTH, expand=YES)
        self.left_frame = Frame(self.body_frame, background="#cccccc", borderwidth=1, width=700)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        self.right_frame = Frame(self.body_frame, background="#eeeeee", borderwidth=1, width=300)
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand=YES)
        self.canvas = tk.Canvas(self.left_frame, bg='#dddddd', highlightthickness=2, width=700)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        # self.canvas.bind('<Configure>', self.draw_grid)
        # self.canvas.bind('<Button-1>', self.draw_square)

        # GUI Buttons
        self.start_button = tk.Button(self.right_frame, text="Start", command=self.controller.start_action)
        self.start_button.pack(side=TOP, anchor=N, pady=5)
        self.pause_button = tk.Button(self.right_frame, text="Pause", command=self.controller.pause_action)
        self.pause_button.pack(side=TOP, anchor=N, pady=5)
        self.next_frame_button = tk.Button(self.right_frame, text="Next Frame", command=self.controller.next_frame_action)
        self.next_frame_button.pack(side=TOP, anchor=N, pady=5)
        self.randomize_button = tk.Button(self.right_frame, text="Randomize", command=self.controller.randomize_action)
        self.randomize_button.pack(side=TOP, anchor=N, pady=5)
        self.pattern_set_menu = tk.OptionMenu(self.right_frame, self.default_pattern_text, *self.patterns_options, command=self.controller.patterns_set_menu_action)
        self.pattern_set_menu.pack(side=TOP, anchor=N, pady=5)
        self.rule_set_menu = tk.OptionMenu(self.right_frame, self.default_rule_text, *self.rules_options, command=self.controller.rules_set_menu_action)
        self.rule_set_menu.pack(side=TOP, anchor=N, pady=5)
        self.scale_button = tk.Scale(self.right_frame, from_=1, to=1000, length=300, orient=tk.HORIZONTAL)
        self.scale_button.pack(side=TOP, anchor=N, pady=5)

        # options = [
        #     "Random",
        #     "Rand 1",
        #     "Rand 2",
        #     "Rand 3",
        #     "Rand 4",
        #     "Rand 5"
        # ]
        # variable = tk.StringVar(self.right_frame)
        # variable.set(options[0])  # default value
        # w = tk.OptionMenu(self.right_frame, variable, *options)
        # w.pack(side=TOP, anchor=N, pady=5)

    def draw_next_frame(self):
        # clear canvas

        self.canvas.delete(ALL) # delete all objects from canvas
        self.canvas.create_rectangle(0, 0, 700, 700, fill='white', width=1)

        size = 7
        # make 100+100 = 200 lines
        # draw horizontal lines
        for y in range(0, 700, 7):
            self.canvas.create_line(0, y, 700, y, width=1, fill='#C0C0C0')
        # draw vertical lines
        for x in range(0, 700, 7):
            self.canvas.create_line(x, 0, x, 700, width=1, fill='#C0C0C0')


        # make squares A(x,y), B(x,y)
        [self.canvas.create_rectangle(((i-1) * size) + 1, ((j-1) * size) + 1, (i-1) * size + size, (j-1) * size + size, fill='#000000', width=0)
            for i in range(1, 101)
            for j in range(1, 101)
            if self.controller.current_frame[j][i]]

        # make squares
        # size = 7
        # for i in range(1, 99):
        #     for j in range(1, 99):
        #         if self.controller.current_frame[j][i]:  # array of arrays [j - row][i - column]
        #             self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#000000', width=0)

                # Blue colors
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 1:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#B3E5FC', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 2:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#81D4FA', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 3:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#42A5F5', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 4:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#42A5F5', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 5:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#1E88E5', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 6:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#3F51B5', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 7:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#303F9F', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 8:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#311B92', width=0)

                # # red and yellow
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 1:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#FFEB3B', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 2:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#FFEB3B', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 3:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#FFC107', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 4:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#FFC107', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 5:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#FB8C00', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 6:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#FF7043', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 7:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#F4511E', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 8:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#D84315', width=0)

                # # green and yellow
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 1:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#F7CA18', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 2:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#F7CA18', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 3:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#FFA400', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 4:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#26A65B', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 5:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#26A65B', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 6:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#006442', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 7:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#006442', width=0)
                # if self.controller.current_frame[j][i] and self.controller.check_neighbours_alive(i, j) == 8:  # array of arrays [j - row][i - column]
                #     self.canvas.create_rectangle((i * size) + 1, (j * size) + 1, i * size + size, j * size + size, fill='#006442', width=0)

    def round_number(self, number):
        return int(number/10)*10

    def draw_square(self, event=None):
        # if the cell state is 0
        self.canvas.create_rectangle(self.round_number(event.x) + 1,
                                     self.round_number(event.y) + 1,
                                     self.round_number(event.x) + 10,
                                     self.round_number(event.y) + 10,
                                     fill='orange',
                                     width=0)
        # else if the cell state is 1 draw a white rectangle
        self.temporary_state = self.controller.next_state

        for i in range(0, 10):
            for j in range(0, 10):
                if i == self.round_number(event.x)/10 and j == self.round_number(event.y)/10:
                    self.temporary_state[j][i] = 1
