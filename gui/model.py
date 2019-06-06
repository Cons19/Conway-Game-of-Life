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

        self.selected_rule = "Rule 1"
        self.list_rule = []
        self.list_states = []
        self.rules = []
        self.status = []
        self.dead_nr_neighbours = []
        self.dead_result = []
        self.alive_nr_neighbours = []
        self.alive_result = []

        self.patterns = []
        self.pattern("Exploder")

        with open('rule_sets.json') as rules_file:
            self.rule_sets = json.load(rules_file)

        self.read_rule_sets_config()


    def reset_rules(self):
        self.list_rule = []
        self.list_states = []
        self.status = []
        self.dead_nr_neighbours = []
        self.dead_result = []
        self.alive_nr_neighbours = []
        self.alive_result = []

    def read_rule_sets_config(self):

        print("model - read_config")
        print(self.selected_rule)
        #print(self.rule_sets)
        for i in self.rule_sets:
            self.rules.append(i)
            if i == self.selected_rule:
                print(self.rule_sets[i])
                self.list_rule.append(self.rule_sets[i])
                for j in self.rule_sets[i]:
                    self.status.append(j)
                    self.list_states.append(self.rule_sets[i][j])

        #print(self.list_states1[0])
        #print(self.list_states1[1])
        print(self.status[1])
        print(self.rule_sets[self.rules[0]])

        for d in self.list_states[0]:
            for nr_neighbours, result in d.items():
                self.dead_nr_neighbours.append(nr_neighbours)
                self.dead_result.append(result)

        print("list_states")
        print(self.list_states)
        print("--")

        for d in self.list_states[1]:
            for nr_neighbours, result in d.items():
                self.alive_nr_neighbours.append(nr_neighbours)
                self.alive_result.append(result)

    def pattern(self, name):
        # if name == "Clear":
        #     self.next_state = [[0 for x in range(100)] for x in range(100)]
        if name == "Glider":
            self.next_state[49][50] = 1
            self.next_state[50][51] = 1
            self.next_state[51][49] = 1
            self.next_state[51][50] = 1
            self.next_state[51][51] = 1
        elif name == "Exploder":
            self.next_state[48][48] = 1
            self.next_state[48][50] = 1
            self.next_state[48][52] = 1
            self.next_state[49][48] = 1
            self.next_state[49][52] = 1
            self.next_state[50][48] = 1
            self.next_state[50][52] = 1
            self.next_state[51][48] = 1
            self.next_state[51][52] = 1
            self.next_state[52][48] = 1
            self.next_state[52][50] = 1
            self.next_state[52][52] = 1
        elif name == "Small Exploder":
            self.next_state[49][49] = 1
            self.next_state[50][48] = 1
            self.next_state[50][49] = 1
            self.next_state[50][50] = 1
            self.next_state[51][48] = 1
            self.next_state[51][50] = 1
            self.next_state[52][49] = 1
        elif name == "10 Cell Row":
            self.next_state[50][45] = 1
            self.next_state[50][46] = 1
            self.next_state[50][47] = 1
            self.next_state[50][48] = 1
            self.next_state[50][49] = 1
            self.next_state[50][50] = 1
            self.next_state[50][51] = 1
            self.next_state[50][52] = 1
            self.next_state[50][53] = 1
            self.next_state[50][54] = 1



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
                if self.current_state[x][y] == int(self.status[1]):
                    if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[0]):
                        self.next_state[x][y] = int(self.alive_result[0])
                    if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[1]):
                        self.next_state[x][y] = int(self.alive_result[1])
                    if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[2]):
                        self.next_state[x][y] = int(self.alive_result[2])
                    if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[3]):
                        self.next_state[x][y] = int(self.alive_result[3])
                    if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[4]):
                        self.next_state[x][y] = int(self.alive_result[4])
                    if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[5]):
                        self.next_state[x][y] = int(self.alive_result[5])
                    if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[6]):
                        self.next_state[x][y] = int(self.alive_result[6])
                    if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[7]):
                        self.next_state[x][y] = int(self.alive_result[7])
                    if self.check_neighbours_alive(x, y) == int(self.alive_nr_neighbours[8]):
                        self.next_state[x][y] = int(self.alive_result[8])
                # check for dead cell cases
                if self.current_state[x][y] == int(self.status[0]):
                    if self.check_neighbours_alive(x, y) == int(self.dead_nr_neighbours[0]):
                        self.next_state[x][y] = int(self.dead_result[0])
                    if self.check_neighbours_alive(x, y) == int(self.dead_nr_neighbours[1]):
                        self.next_state[x][y] = int(self.dead_result[1])
                    if self.check_neighbours_alive(x, y) == int(self.dead_nr_neighbours[2]):
                        self.next_state[x][y] = int(self.dead_result[2])
                    if self.check_neighbours_alive(x, y) == int(self.dead_nr_neighbours[3]):
                        self.next_state[x][y] = int(self.dead_result[3])
                    if self.check_neighbours_alive(x, y) == int(self.dead_nr_neighbours[4]):
                        self.next_state[x][y] = int(self.dead_result[4])
                    if self.check_neighbours_alive(x, y) == int(self.dead_nr_neighbours[5]):
                        self.next_state[x][y] = int(self.dead_result[5])
                    if self.check_neighbours_alive(x, y) == int(self.dead_nr_neighbours[6]):
                        self.next_state[x][y] = int(self.dead_result[6])
                    if self.check_neighbours_alive(x, y) == int(self.dead_nr_neighbours[7]):
                        self.next_state[x][y] = int(self.dead_result[7])
                    if self.check_neighbours_alive(x, y) == int(self.dead_nr_neighbours[8]):
                        self.next_state[x][y] = int(self.dead_result[8])

        self.controller.current_frame = self.current_state
        return self.next_state

    # check how many neighbours of a cell are alive
    def check_neighbours_alive(self, x, y):
        neighbour_count = 0
        if self.current_state[x - 1][y - 1] == int(self.status[1]):
            neighbour_count += 1
        if self.current_state[x - 1][y] == int(self.status[1]):
            neighbour_count += 1
        if self.current_state[x - 1][y + 1] == int(self.status[1]):
            neighbour_count += 1
        if self.current_state[x][y - 1] == int(self.status[1]):
            neighbour_count += 1
        if self.current_state[x][y + 1] == int(self.status[1]):
            neighbour_count += 1
        if self.current_state[x + 1][y - 1] == int(self.status[1]):
            neighbour_count += 1
        if self.current_state[x + 1][y] == int(self.status[1]):
            neighbour_count += 1
        if self.current_state[x + 1][y + 1] == int(self.status[1]):
            neighbour_count += 1
        return neighbour_count
