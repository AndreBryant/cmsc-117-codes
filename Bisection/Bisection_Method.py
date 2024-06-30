import numpy as np

def bisection(f, a, b, maxit, tol):
    """
    TODO
    it is better to make a != b and b - a != 0
    """
    err = b-a
    k = 0

    fa = f(a)
    fb = f(b)

    if fa == 0:
        c = a
        err = 0
    if fb == 0:
        c = b
        err = 0
    if np.sign(fa) == np.sign(fb):
        raise RuntimeError("Bolzano's theorem condition is not met")
    
    while err > tol and k < maxit:
        c = a+ (0.5*(b-a))
        fc = f(c)
        if fc == 0:
            return c

        if np.sign(fa) == np.sign(fc):
            a = c
            fa = fc
        else:
            b = c
        err = abs(b-a)
        k += 1
    if err > tol and k == maxit:
        raise RuntimeError("Error in in finding a root")
    
    return [c, fc, err, k]

