import unittest
from simple_test import add

class AdditionTest(unittest.TestCase):
    def test_add(self):
        AdditionResult = add(2, 3)
        self.assertEqual(AdditionResult, 5)

if __name__ == '__main__':
    unittest.main()

#unit test complete
