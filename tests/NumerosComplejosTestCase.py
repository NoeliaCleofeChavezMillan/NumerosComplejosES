import src.logica.libreria as lc
import unittest

class TestCplxoperations(unittest.TestCase):

    def test(self):
        suma = lc.cplxsum((3, 5),(-2.6, 6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)


if __name__ == '__main__':
    unittest.main()

