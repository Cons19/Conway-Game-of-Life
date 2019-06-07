import mvc.model
import mvc.view
import random

class GameOfLifeController:
    def __init__(self):
        self.model = mvc.model.GameOfLifeModel(self)
        self.rules = self.model.rules
        self.patterns = self.model.patterns
        self.next_state = self.model.next_state  # before initializing view
        self.user_changes = 0
        self.view = mvc.view.GameOfLifeView(self)

        self.game_paused = True
        self.task = 1
        self.view.window.mainloop()

    def start_action(self):
        print('start_action')
        self.next_state = self.model.next()
        self.view.draw_next_frame()
        self.task = self.view.window.after(self.view.scale_button.get(), self.start_action)
        self.view.pause_button["state"] = "normal"
        self.view.start_button["state"] = "disabled"

    def pause_action(self):
        print('pause_action')
        self.view.window.after_cancel(self.task)
        self.view.pause_button["state"] = "disabled"
        self.view.start_button["state"] = "normal"

    def next_frame_action(self):
        print('next_frame_action')
        self.model.next_state = self.next_state
        if self.user_changes == 0:  # process the next frame only if the user didn't made changes on the frame
            self.next_state = self.model.next()
        self.view.draw_next_frame()

    def default_button(self):
        print('default_button')

    def randomize_action(self):
        print('randomize_action')
        # TODO: use comprehension list
        # self.model.next_state = [[random.uniform(0, 1) for x in range(100)] for x in range(100)]
        for i in range(0, 100):
            for j in range(0, 100):
                if random.uniform(0, 1) > 0.5:
                    self.model.next_state[i][j] = 1
                else:
                    self.model.next_state[i][j] = 0

    def rules_set_menu_action(self, selection):
        print('rules_menu')
        print(selection)
        self.model.reset_rules()
        self.model.selected_rule = selection
        self.model.read_rule_sets_config()  # read_rule_sets_config(selection)

    def patterns_set_menu_action(self, selection):
        print('patterns_menu')
        print(selection)
        self.model.reset_patterns()
        self.model.selected_pattern = selection
        self.model.read_pattern_sets_config()

        self.next_state = self.model.next_state # sync values from models with controller
        self.user_changes = 1
        self.next_frame_action()

    # check how many neighbours of a cell are alive
    def check_neighbours_alive(self, x, y):
        return self.model.next_state[x - 1][y - 1] + self.model.next_state[x - 1][y] + self.model.next_state[x - 1][y + 1] + \
               self.model.next_state[x][y - 1] + self.model.next_state[x][y + 1] + \
               self.model.next_state[x + 1][y - 1] + self.model.next_state[x + 1][y] + self.model.next_state[x + 1][y + 1]

    def clear_screen_action(self):
        self.next_state = self.model.clear_screen()
        self.user_changes = 1
        self.next_frame_action()

    def quit_action(self):
        self.view.window.destroy()