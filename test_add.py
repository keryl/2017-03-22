import unittest
import add

class AddTestCase(unittest.TestCase):

    def test_adds_integers(self):
        result = add.add(1, 2)
        self.assertEqual(3, result)

if __name__ == "__main__":
    unittest.main()

