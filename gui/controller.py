import tkinter as tk
import numpy as np

import gui.model
import gui.view


class GameOfLifeController:

    def __init__(self):
        print('Controller1')
        self.model = gui.model.GameOfLifeModel(self)
        print('Controller2')
        # self.model.run()
        self.view = gui.view.GameOfLifeView(self)
        # self.current_frame = self.get_current_frame()
        self.current_frame = self.model.next_state
        print('self.model.next_state')
        print(self.model.next_state)
        self.next_state = self.model.next_state
        self.next_action = self.next_action()
        self.view.window.mainloop()

    def next_action(self):
        # self.model.next_state = self.view.temporary_state  # send the temporarty data from the view to the model to create the next frame
        # self.model.current_state = self.view.temporary_state  # send the temporarty data from the view to the model to create the next frame
        # self.view.draw_next_frame()
        self.model.current_state = self.model.next_state
        self.model.next()
        self.view.draw_next_frame()
        # self.view.temporary_state = self.model.next_state # send the temporarty data from the view to the model to create the next frame



    # def quit_action(self):
    #     self.view.window.destroy()
