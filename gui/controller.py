import tkinter as tk

import gui.model
import gui.view


class GameOfLifeController:

    def __init__(self):
        print('Controller1')
        self.model = gui.model.GameOfLifeModel()
        print('Controller2')
        # self.model.run()

        self.view = gui.view.GameOfLifeView(self)

        self.current_frame = self.get_current_frame()



        self.view.window.mainloop()
        # self.window.mainloop()



    def get_current_frame(self):
        print('------model run')
        # print(self.model.run())
        return self.model.run()

    # def quit_action(self):
    #     self.view.window.destroy()
