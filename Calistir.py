import unittest
from main import Main

class TestMainClass(unittest.TestCase):

    def setUp(self):
        self.main_object = Main()

    def test_mainObject(self):
        self.assertIsInstance(self.main_object, Main)

if __name__ == '__main__':
    unittest.main()