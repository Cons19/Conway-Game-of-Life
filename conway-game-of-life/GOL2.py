import numpy as np

class CA:

    def __init__(self):
        # self.current_state = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #               [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #               [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #               [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #               [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #               [6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #               [7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #               [8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #               [9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #               [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.current_state = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        # self.current_state = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        #                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        #                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        #                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
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

        # for i in range(0, 10):
        #     for j in range(0, 10):
        #         self.next_state[i][j] = 0

        # print("next() next_state clean")
        # print(self.next_state)
        # print("next() current_state before")
        # print(self.current_state)


        for x in range(0, 10):
            for y in range(0, 10):
                if self.current_state[x, y] == 0:
                    self.next_state[x, y] = 1
                elif self.current_state[x, y] == 1:
                    self.next_state[x, y] = 0

        # for x in range(0, 10):
        #     for y in range(0, 10):
        #         if self.current_state[x][y] == int('4'):
        #             self.next_state[x][y] = 0
                # elif self.current_state[x][y] == int('4'):
                #     self.next_state[x][y] = 0
        #
        # print("next_state with data")
        # print(self.next_state)
        # print("next() current_state after")
        # print(self.current_state)

        return self.next_state

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

        print(self.current_state)


        for k in range(0, frames):
            data = self.next()
            # print('data ' + str(data))
            print('Frame: ' + str(k))

            print(data)
            #         print(data[i][j], end=" ")
            #     print()
            # print()

ca = CA().run()
