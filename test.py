import unittest

from monthlyDogFood import nextMonthDogFood2


class TestCalc(unittest.TestCase):
    def test_calc(self):
        """
        Test dog food calculation is correct based on requirement
        """
        result = nextMonthDogFood2(5,3,7,17)
        self.assertEqual(result, 363.6)

    def test_noLeftOvers(self):
        """
        Test dog food calculation when no remaining food in current month
        """
        result = nextMonthDogFood2(5,3,7,0)
        self.assertEqual(result, 384.0)

    def test_nonNumeric(self):
        """
        Test dog food calculation with non-numeric datatypes
        """
        with self.assertRaises(TypeError):
            result = nextMonthDogFood2(a,6,7,0)

    def test_capsLeters(self):
        """
        Test dog food calculation with capital letter
        """
        with self.assertRaises(TypeError): 
            result = nextMonthDogFood2(5,B,7,0)


if __name__ == '__main__':
    unittest.main()
