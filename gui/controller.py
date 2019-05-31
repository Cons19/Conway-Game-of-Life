import gui.model
import gui.view

class GameOfLifeController:
    def __init__(self):
        self.model = gui.model.GameOfLifeModel(self)
        self.view = gui.view.GameOfLifeView(self)
        self.current_frame = self.model.next_state
        self.next_state = self.model.next_state
        self.next_action = self.next_action()
        self.view.window.mainloop()

    def next_action(self):
        self.model.next()
        self.view.draw_next_frame()
