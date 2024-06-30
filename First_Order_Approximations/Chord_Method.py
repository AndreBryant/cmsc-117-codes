from utility.utility_module1 import getSlope

def chord(f, a, b, x, maxit, tol, wa = 0.5, wf = 0.5):
    """
    TODO
    Ito yung may fixed slope
    """
    err = tol + 1
    q = getSlope(f(a), f(b), a, b)
    fx = f(x)
    k = 0

    while err > tol and k < maxit:
        xold = x
        x = x - fx/q
        fx = f(x)
        err = wa * abs(x - xold) + wf * abs(fx)
        k += 1
    if err > tol and k == maxit:
        raise RuntimeError("Error in approximation")

    return [x, fx, err, k]