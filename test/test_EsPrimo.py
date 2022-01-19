
import unittest
from funciones import esPrimo

class TestEsPrimo(unittest,unittest.TestCase):
    def test_IsANumber(self):
        self.assertFalse(esPrimo("A"))
        self.assertFalse(esPrimo(True))
        self.assertFalse(esPrimo(3.4))
        self.assertTrue(esPrimo(11))

if __name__ == '__main__':
    unittest.main()

