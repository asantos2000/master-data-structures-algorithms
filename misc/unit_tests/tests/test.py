import unittest
import functions

# Avoid using Assert.IsTrue
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(functions.add(4, 2), 6)
        self.assertEqual(functions.add(-1, 1), 0)
        self.assertEqual(functions.add(-1, -1), -2)
        self.assertEqual(functions.add(0, -1), -1)

class TestRound(unittest.TestCase):
     def test_round(self):
          self.assertEqual(functions.round_plus_ten(4.3), 14)
          self.assertEqual(functions.round_plus_ten(4.7), 15)
          self.assertEqual(functions.round_plus_ten(4.5), 15)

if __name__ == '__main__':
    unittest.main()
