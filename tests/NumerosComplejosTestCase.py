import libreria as lc
import unittest

class TestCplxoperations(unittest.TestCase):

    def test(self):
        suma = lc.cplxsum((3, 5),(-2.6, 6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)



if __name__ == '__main__':
    unittest.main()


import unittest


class TestCplxrest(unittest.TestCase):

        def test(self):
            resta = lc.cplxrest((7, 9), (-4, 8))
            self.assertAlmostEqual(resta[0], 11)
            self.assertAlmostEqual(resta[1], 1)


if __name__ == '__main__':
    unittest.main()