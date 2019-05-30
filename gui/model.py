import numpy as np


class GameOfLifeModel:
    print('Model')
    def __init__(self):
        self.current_state = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        self.next_state = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        # self.seeds = {
        #     "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
        #     "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
        #     "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
        #     "spaceship": [[0, 0, 1, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]],
        # }

    def state(self):
        """Returns the next state."""
        return self.next_state

    def next(self):
        """Progress one step and then return the current state."""

        self.current_state = self.next_state
        self.next_state = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        for x in range(1, 9):
            for y in range(1, 9):
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
        # self.current_state = self.next_state
        print("current")
        print(self.current_state)
        print("model - next - next_state ")
        print(self.next_state)
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

    def run(self, frames=5):
        """Progress and print num states.
        0s are replaced by spaces, and 1s are replaced by * for pretty printing."""
        print('Frame 0')

        # print("current")
        # print(self.current_state)
        # print("next")
        # print(self.next_state)
        # self.next()
        # print("current")
        # print(self.current_state)
        # print("next")
        # print(self.next_state)
        # self.next()
        # print("current")
        # print(self.current_state)
        # print("next")
        # print(self.next_state)

        # for k in range(0, frames):
        #     data = self.next()
        #     print('Frame: ' + str(k))
        #     print("next 21212")
        #     print(data)
        # print(self.next())
        # print(data)
        return self.next_state

