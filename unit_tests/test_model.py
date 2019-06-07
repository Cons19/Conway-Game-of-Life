import unittest

# from mvc import model


class TestModel(unittest.TestCase):

    # called before the test method, to prepare it
    def setUp(self):
        pass

    # called after the test method
    def tearDown(self):
        pass

    # def test_neighbours(self):
    #     # self.assertEqual(model)
    #     pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FO')


if __name__ == '__main__':
    unittest.main()
