import json
import sys
import numpy as np


class GameOfLifeModel:
    def __init__(self, controller):
        self.controller = controller
        np.set_printoptions(threshold=sys.maxsize)
        # initial states
        # self.current_state = np.zeros(shape=(30, 30), dtype=int)
        # self.current_state1 = ['0' for i in range(10) [ '1' for j in range(10)]]
        self.current_state = [[0 for x in range(100)] for x in range(100)]
        self.next_state = [[0 for x in range(100)] for x in range(100)]
        # self.next_state = np.zeros(shape=(30, 30), dtype=int)

        self.pattern("Exploder")

        with open('../rule_sets.json') as rules_file:
            self.rule_sets = json.load(rules_file)


        self.list_rule1 = []
        self.list_states1 = []
        self.rules = []
        self.status = []
        #print(self.rule_sets)
        for i in self.rule_sets:
            self.rules.append(i)
            if i == self.rules[0]:
                print(self.rule_sets[i])
                self.list_rule1.append(self.rule_sets[i])
                for j in self.rule_sets[i]:
                    self.status.append(j)
                    self.list_states1.append(self.rule_sets[i][j])

        #print(self.list_states1[0])
        #print(self.list_states1[1])
        print(self.status[0])
        print(self.rule_sets[self.rules[0]])

        self.dead_nr_neighbours = []
        self.dead_result = []
        for d in self.list_states1[0]:
            for nr_neighbours, result in d.items():
                self.dead_nr_neighbours.append(nr_neighbours)
                self.dead_result.append(result)

        print("list_states")
        print(self.list_states1)
        print("--")
        self.alive_nr_neighbours = []
        self.alive_result = []
        for d in self.list_states1[1]:
            for nr_neighbours, result in d.items():
                self.alive_nr_neighbours.append(nr_neighbours)
                self.alive_result.append(result)

    def pattern(self, name):
        if name == "Clear":
            pass
        elif name == "Glider":
            self.next_state[3][5] = 1
            self.next_state[4][6] = 1
            self.next_state[5][4] = 1
            self.next_state[5][5] = 1
            self.next_state[5][6] = 1
        elif name == "Exploder":
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
        elif name == "Small Exploder":
            self.next_state[20][20] = 1
            self.next_state[21][19] = 1
            self.next_state[21][20] = 1
            self.next_state[21][21] = 1
            self.next_state[22][19] = 1
            self.next_state[22][21] = 1
            self.next_state[23][20] = 1
        elif name == "10 Cell Row":
            self.next_state[30][30] = 1
            self.next_state[30][31] = 1
            self.next_state[30][32] = 1
            self.next_state[30][33] = 1
            self.next_state[30][34] = 1
            self.next_state[30][35] = 1
            self.next_state[30][36] = 1
            self.next_state[30][37] = 1
            self.next_state[30][38] = 1
            self.next_state[30][39] = 1



    def state(self):
        """Returns the next state."""
        return self.next_state

    def next(self):
        """Progress one step and then return the current state."""
        self.current_state = self.next_state
        # self.next_state = np.zeros(shape=(30, 30), dtype=int)
        self.next_state = [[0 for x in range(100)] for x in range(100)]

        for x in range(1, 99):
            for y in range(1, 99):
                # check for alive cell cases
                if self.current_state[x][y] == 1:
                    if self.check_neighbours_alive(x, y) == 0:
                        self.next_state[x][y] = 0
                    if self.check_neighbours_alive(x, y) == 1:
                        self.next_state[x][y] = 0
                    if self.check_neighbours_alive(x, y) == 2:
                        self.next_state[x][y] = 1
                    if self.check_neighbours_alive(x, y) == 3:
                        self.next_state[x][y] = 1
                    if self.check_neighbours_alive(x, y) == 4:
                        self.next_state[x][y] = 1
                    if self.check_neighbours_alive(x, y) == 5:
                        self.next_state[x][y] = 0
                    if self.check_neighbours_alive(x, y) == 6:
                        self.next_state[x][y] = 1
                    if self.check_neighbours_alive(x, y) == 7:
                        self.next_state[x][y] = 1
                    if self.check_neighbours_alive(x, y) == 8:
                        self.next_state[x][y] = 1
                # check for dead cell cases
                if self.current_state[x][y] == 0:
                    if self.check_neighbours_alive(x, y) == 0:
                        self.next_state[x][y] = 0
                    if self.check_neighbours_alive(x, y) == 1:
                        self.next_state[x][y] = 0
                    if self.check_neighbours_alive(x, y) == 2:
                        self.next_state[x][y] = 0
                    if self.check_neighbours_alive(x, y) == 3:
                        self.next_state[x][y] = 1
                    if self.check_neighbours_alive(x, y) == 4:
                        self.next_state[x][y] = 1
                    if self.check_neighbours_alive(x, y) == 5:
                        self.next_state[x][y] = 1
                    if self.check_neighbours_alive(x, y) == 6:
                        self.next_state[x][y] = 0
                    if self.check_neighbours_alive(x, y) == 7:
                        self.next_state[x][y] = 0
                    if self.check_neighbours_alive(x, y) == 8:
                        self.next_state[x][y] = 0
                #
                # # check for alive cell cases
                # if self.current_state[x][y] == int(self.status[1]):
                #     if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[0]) or \
                #             self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[1]):
                #         self.next_state[x][y] = int(self.alive_result[0])
                #     if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[2]) or \
                #             self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[3]):
                #         self.next_state[x][y] = int(self.alive_result[2])
                #     if self.check_neighbours_alive(x, y) >= int(self.alive_nr_neighbours[4]):
                #         self.next_state[x][y] = int(self.alive_result[4])
                # # check for dead cell cases
                # if self.current_state[x][y] == int(self.status[0]):
                #     if self.check_neighbours_alive(x, y) == int(self.dead_nr_neighbours[3]):
                #         self.next_state[x][y] = int(self.dead_result[3])
                #     if self.check_neighbours_alive(x, y) < int(self.dead_nr_neighbours[3]) or \
                #             self.check_neighbours_alive(x, y) > int(self.dead_nr_neighbours[3]):
                #         self.next_state[x][y] = int(self.dead_result[0])


        # for x in range(1, 99):
        #     for y in range(1, 99):
        #         # check for alive cell cases
        #         if self.current_state[x][y] == 1:
        #             if self.check_neighbours_alive(x, y) == 0 or self.check_neighbours_alive(x, y) == 1:
        #                 self.next_state[x][y] = 0
        #             if self.check_neighbours_alive(x, y) == 2 or self.check_neighbours_alive(x, y) == 3:
        #                 self.next_state[x][y] = 1
        #             if self.check_neighbours_alive(x, y) >= 4:
        #                 self.next_state[x][y] = 0
        #         # check for dead cell cases
        #         if self.current_state[x][y] == 0:
        #             if self.check_neighbours_alive(x, y) == 3:
        #                 self.next_state[x][y] = 1
        #             if self.check_neighbours_alive(x, y) < 3 or self.check_neighbours_alive(x, y) > 3:
        #                 self.next_state[x][y] = 0




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
