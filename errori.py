"""
Code to calculate errors on a generic function
"""
import numpy as np
import sympy as sp

def compute_error(f, variables, data, error):
    '''
    Function to propagate the error of an arbritay function f.
    For example if f is f(x, y, z) the error, df, will be:

    df = sqrt( (df(x,y,z)/dx * dx)**2 + (df(x,y,z)/dx * dx)**2 + (df(x,y,z)/dx * dx)**2 )

    Parameters
    ----------
    f : sympy.core.(something)
        function, written with sympy simbols,
        of which to compute the error
    variables : list
        list of variables of f, each element
        mu be a sympy.core.symbol.Symbol
    data : list
        list of the numerical value of the variables
    error : list
        list of the error on data
    
    Returns
    -------
    central_value : float
        value of f comuted on data
    error : float
        error on central value
    
    Example
    -------
    >>> x = sp.Symbol('x')
    >>> y = sp.Symbol('y')
    >>> X = [x, y]
    >>> f = ((1/x) + (1/y))**(-1)
    >>> compute_error(f, X, [1.3, 2], [0.1, 0.1])
    >>> (0.7499999999999999, 0.044393977016173036)
    '''

    # Compute the central value i.e. f(data)
    # We use func beacuse we sobsistute on variable at time
    func = f 
    for var, val in zip(variables, data):
        func = func.subs(var, val)
    
    central_value = float(func)

    # Compute the error on f
    # First of all we compute al derivatives of f respect each variable
    d_func = []
    for var in variables:
        d_func.append(sp.diff(f, var))
    
    # Secondly we compute the numerical value of all the derivatives
    d_func_v = []
    for deriv in d_func:
        for var, val in zip(variables, data):
            deriv = deriv.subs(var, val)
        d_func_v.append(deriv)
    
    # Finally we compute the error adding the squares of derivative and error
    d_func_v_2 = [(df*err)**2 for df, err in zip(d_func_v, error)]
    error      = np.sqrt(float(sum(d_func_v_2)))

    return central_value, error

if __name__ == "__main__":

    x = sp.Symbol('x')
    y = sp.Symbol('y')

    X = [x, y]
    f = ((1/x) + (1/y))**(-1)

    print(compute_error(f, X, [1.2, 2], [0.1, 0.15]))