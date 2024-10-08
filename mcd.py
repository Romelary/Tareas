import unittest


def mcd_dos_numeros(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def mcd_cuatro_numeros(a, b, c, d):
    return mcd_dos_numeros(mcd_dos_numeros(a, b), mcd_dos_numeros(c, d))


class TestMCD(unittest.TestCase):
    def test_mcd_dos_numeros(self):
        esperado = 4
        actual = mcd_dos_numeros(8, 12)
        self.assertEqual(actual, esperado)

        esperado = 6
        actual = mcd_dos_numeros(54, 24)
        self.assertEqual(actual, esperado)

        esperado = 1
        actual = mcd_dos_numeros(7, 3)
        self.assertEqual(actual, esperado)

        esperado = 5
        actual = mcd_dos_numeros(0, 5)
        self.assertEqual(actual, esperado)

        esperado = 0
        actual = mcd_dos_numeros(0, 0)
        self.assertEqual(actual, esperado)

    def test_mcd_cuatro_numeros(self):
        esperado = 4
        actual = mcd_cuatro_numeros(8, 12, 16, 24)
        self.assertEqual(actual, esperado)

        esperado = 6
        actual = mcd_cuatro_numeros(54, 24, 36, 18)
        self.assertEqual(actual, esperado)

        esperado = 1
        actual = mcd_cuatro_numeros(7, 3, 5, 9)
        self.assertEqual(actual, esperado)

        esperado = 5
        actual = mcd_cuatro_numeros(100, 50, 25, 10)
        self.assertEqual(actual, esperado)

if __name__ == '__main__':
    unittest.main()
