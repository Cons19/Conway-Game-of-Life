import sys
import numpy as np


class GameOfLifeModel:
    def __init__(self, controller):
        self.controller = controller
        np.set_printoptions(threshold=sys.maxsize)
        # initial states
        self.current_state = np.zeros(shape=(30, 30),dtype=int)
        self.next_state = np.zeros(shape=(30, 30), dtype=int)

        # glider pattern
        # self.next_state[3][5] = 1
        # self.next_state[4][6] = 1
        # self.next_state[5][4] = 1
        # self.next_state[5][5] = 1
        # self.next_state[5][6] = 1

        # exploder pattern
        self.next_state[8][8] = 1
        self.next_state[9][8] = 1
        self.next_state[10][8] = 1
        self.next_state[11][8] = 1
        self.next_state[12][8] = 1
        self.next_state[8][10] = 1
        self.next_state[12][10] = 1
        self.next_state[8][12] = 1
        self.next_state[9][12] = 1
        self.next_state[10][12] = 1
        self.next_state[11][12] = 1
        self.next_state[12][12] = 1


    def state(self):
        """Returns the next state."""
        return self.next_state

    def next(self):
        """Progress one step and then return the current state."""
        self.current_state = self.next_state
        self.next_state = np.zeros(shape=(30, 30), dtype=int)
        for x in range(1, 29):
            for y in range(1, 29):
                # check for alive cell cases
                if (self.current_state[x][y] == 1) and (
                        (self.check_neighbours_alive(x, y) == 0) or (self.check_neighbours_alive(x, y) == 1)):
                    self.next_state[x][y] = 0
                if (self.current_state[x][y] == 1) and (
                        (self.check_neighbours_alive(x, y) == 2) or (self.check_neighbours_alive(x, y) == 3)):
                    self.next_state[x][y] = 1
                if (self.current_state[x][y] == 1) and (self.check_neighbours_alive(x, y) >= 4):
                    self.next_state[x][y] = 0
                # check for dead cell cases
                if (self.current_state[x][y] == 0) and (self.check_neighbours_alive(x, y) == 3):
                    self.next_state[x][y] = 1
                if (self.current_state[x][y] == 0) and (
                        (self.check_neighbours_alive(x, y) < 3) or (self.check_neighbours_alive(x, y) > 3)):
                    self.next_state[x][y] = 0
        self.controller.current_frame = self.current_state
        return self.next_state

    # check how many neighbours of a cell are alive
    def check_neighbours_alive(self, x, y):
        neighbour_count = 0
        if self.current_state[x - 1][y - 1] == 1:
            neighbour_count += 1
        if self.current_state[x - 1][y] == 1:
            neighbour_count += 1
        if self.current_state[x - 1][y + 1] == 1:
            neighbour_count += 1
        if self.current_state[x][y - 1] == 1:
            neighbour_count += 1
        if self.current_state[x][y + 1] == 1:
            neighbour_count += 1
        if self.current_state[x + 1][y - 1] == 1:
            neighbour_count += 1
        if self.current_state[x + 1][y] == 1:
            neighbour_count += 1
        if self.current_state[x + 1][y + 1] == 1:
            neighbour_count += 1
        return neighbour_count
