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
        print('self.model.next_state')
        print(self.model.next_state)

        self.next_state = self.model.next_state
        self.next_action = self.next_action()



        self.view.window.mainloop()
        # self.window.mainloop()



    def get_current_frame(self):
        print('------model run')
        # print(self.model.run())
        return self.model.run()

    def next_action(self):
        pass
        # self.view.save_frame()
        self.model.next_state = self.view.temporary_state  # send the temporarty data from the view to the model to create the next frame
        # self.view.draw_current_frame()

    # def quit_action(self):
    #     self.view.window.destroy()
