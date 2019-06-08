import unittest

from mvc.model import GameOfLifeModel
from mvc.controller import GameOfLifeController

# to run the tests:  python -m unit_tests.test_model


class TestModel(unittest.TestCase):

    # called before the test method, to prepare it
    def setUp(self):
        self.model = GameOfLifeModel(controller=GameOfLifeController)
        self.current_state = self.model.current_state
        self.current_state[49][50] = 1
        self.current_state[50][51] = 1
        self.current_state[51][49] = 1
        self.current_state[51][50] = 1
        self.current_state[51][51] = 1
        self.next_state = self.current_state
        self.model.next_state = self.next_state
        self.next_state = self.model.next()

    # called after the test method
    def tearDown(self):
        # print(self.model.check_neighbours_alive(51, 50))
        # print(self.current_state[50][49])
        # print(self.next_state[50][49])
        pass

    def test_neighbours(self):
        # verify if self.current_state[51][50] has 3 neighbours
        self.assertEqual(self.model.check_neighbours_alive(51, 50), 3)

        self.assertNotEqual(self.model.check_neighbours_alive(51, 50), 2)
        self.assertNotEqual(self.model.check_neighbours_alive(51, 50), 4)
        self.assertEqual(self.model.check_neighbours_alive(49, 50), 1)
        self.assertEqual(self.model.check_neighbours_alive(50, 51), 3)
        self.assertEqual(self.model.check_neighbours_alive(51, 51), 2)
        self.assertEqual(self.model.check_neighbours_alive(51, 49), 1)
        self.assertNotEqual(self.model.check_neighbours_alive(51, 49), 0)

    def test_next_state(self):
        # check if after next the coordinate becomes alive as should be
        self.assertEqual(self.next_state[50][49], 1)
        self.assertNotEqual(self.next_state[50][49], 0)
        self.assertEqual(self.next_state[52][50], 1)
        self.assertNotEqual(self.next_state[52][50], 0)
        self.assertEqual(self.next_state[50][51], 1)
        self.assertEqual(self.next_state[51][50], 1)
        self.assertEqual(self.next_state[51][51], 1)
        self.assertNotEqual(self.next_state[49][50], 1)
        self.assertNotEqual(self.next_state[51][49], 1)
        self.assertEqual(self.next_state[49][50], 0)
        self.assertEqual(self.next_state[51][49], 0)


if __name__ == '__main__':
    unittest.main()
