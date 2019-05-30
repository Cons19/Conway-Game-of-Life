import tkinter as tk

import gui.model
import gui.view


class GameOfLifeController:

    def __init__(self):
        self.model = gui.model.GameOfLifeModel()
        self.view = gui.view.GameOfLifeView(self)
        self.view.window.mainloop()
        # self.window.mainloop()


    def next_frame_action(self):
        pass

    # def quit_action(self):
    #     self.view.window.destroy()
