import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        """Compares abs(-42) and 42 

        :return: None
        """
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        """Compares abs(-42) and -42 

        :return: None
        """
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()