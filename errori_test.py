import unittest
import sympy as sp
from uncertainties import ufloat
import uncertainties.umath as uu

from errori import compute_error

class TESTS(unittest.TestCase):

    def test_0(self):
        ''' Litte test
        '''
        x = sp.Symbol('x')
        y = sp.Symbol('y')

        X = [x, y]
        f = x + y

        data  = [1.2, 2]
        error = [0.1, 0.15]

        prop_err = compute_error(f, X, data, error)

        x = ufloat(data[0], error[0])
        y = ufloat(data[1], error[1])

        f = x + y

        print("prop_code:", prop_err)
        print("prop_lib :", f)

        self.assertAlmostEqual(prop_err[0], f.n, 10)
        self.assertAlmostEqual(prop_err[1], f.s, 10)

    def test_1(self):
        ''' Litte test
        '''
        x = sp.Symbol('x')
        y = sp.Symbol('y')

        X = [x, y]
        f = ((1/x) + (1/y))**(-1)

        data  = [1.2, 2]
        error = [0.1, 0.15]

        prop_err = compute_error(f, X, data, error)

        x = ufloat(data[0], error[0])
        y = ufloat(data[1], error[1])

        f = ((1/x) + (1/y))**(-1)

        print("prop_code:", prop_err)
        print("prop_lib :", f)

        self.assertAlmostEqual(prop_err[0], f.n, 10)
        self.assertAlmostEqual(prop_err[1], f.s, 10)

    def test_2(self):
        ''' Litte test
        '''
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        z = sp.Symbol('z')

        X = [x, y, z]
        f = sp.sin(x*z)*sp.log(y/z) + sp.tan(x**y)

        data  = [1.2, 2, 1.5]
        error = [0.1, 0.15, 0.2]

        prop_err = compute_error(f, X, data, error)

        x = ufloat(data[0], error[0])
        y = ufloat(data[1], error[1])
        z = ufloat(data[2], error[2])

        f = uu.sin(x*z)*uu.log(y/z) + uu.tan(x**y)

        print("prop_code:", prop_err)
        print("prop_lib :", f)

        self.assertAlmostEqual(prop_err[0], f.n, 10)
        self.assertAlmostEqual(prop_err[1], f.s, 10)



if __name__ == '__main__':
    unittest.main()
