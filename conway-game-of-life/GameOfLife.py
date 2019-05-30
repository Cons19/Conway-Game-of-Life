import numpy as np

class CA:

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

        # self.next_state = self.current_state

        # print("init() current_state")
        # print(self.current_state)
        # print("init() next_state")
        # print(self.next_state)
        # print(self.seeds)
        # print(self.current_state)

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

                # if self.next_state[x][y] == 1 and ((self.check_neighbours_alive(x, y) == 0) or (self.check_neighbours_alive(x, y) == 1)):
                #     self.next_state[x][y] = 0
                if (self.current_state[x][y] == 1) and ((self.check_neighbours_alive(x, y) == 0) or (self.check_neighbours_alive(x, y) == 1)):
                    self.next_state[x][y] = 0
                if (self.current_state[x][y] == 1) and ((self.check_neighbours_alive(x, y) == 2) or (self.check_neighbours_alive(x, y) == 3)):
                    self.next_state[x][y] = 1
                if (self.current_state[x][y] == 1) and (self.check_neighbours_alive(x, y) >= 4):
                    self.next_state[x][y] = 0
                # check for dead cell cases
                if (self.current_state[x][y] == 0) and (self.check_neighbours_alive(x, y) == 3):
                    self.next_state[x][y] = 1
                if (self.current_state[x][y] == 0) and ((self.check_neighbours_alive(x, y) < 3) or (self.check_neighbours_alive(x, y) > 3)):
                    self.next_state[x][y] = 0
        # print("current ------ 1")
        # print(self.current_state)
        # print("next ------ 1")
        # print(self.next_state)

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
        if self.current_state[x][y-1] == 1:
            neighbour_count += 1
        if self.current_state[x][y + 1] == 1:
            neighbour_count += 1
        if self.current_state[x + 1][y -1] == 1:
            neighbour_count += 1
        if self.current_state[x + 1][y] == 1:
            neighbour_count += 1
        if self.current_state[x + 1][y + 1] == 1:
            neighbour_count += 1
        return neighbour_count

    def run(self, frames=5):
        """Progress and print num states.
        0s are replaced by spaces, and 1s are replaced by * for pretty printing."""
        # print(self.current_state.replace("0", " ").replace("1", "*"))
        # for i in range(1, num):
        #     print(self.next().replace("0", " ").replace("1", "*"))  # continue printing the next 17 lines
        #

        print('Frame 0')

        # for i in range(0, 10):
        #     for j in range(0, 10):
        #         print(self.current_state[i][j], end=" ")
        #     print()
        # print()

        print("current")
        print(self.current_state)
        print("next")

        print(self.next_state)

        for k in range(0, frames):
            data = self.next()
            # print('data ' + str(data))
            print('Frame: ' + str(k))

            print("next 21212")

            print(data)
            #         print(data[i][j], end=" ")
            #     print()
            # print()

ca = CA().run()

