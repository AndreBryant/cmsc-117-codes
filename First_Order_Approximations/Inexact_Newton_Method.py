from utility.utility_module1 import getDerivative

def inexactNewton(f, i, x, maxit, tol, wa = 0.5, wf = 0.5):
    """
    TODO
    i determines the f' if forward, backward or centered
    """
    err = tol + 1
    fx = f(x)
    k = 0

    while err > tol and k < maxit:
        xold = x 
        qk = getDerivative(f, x, i)
        x = x - fx / qk
        fx = f(x)
        err = wa * abs(x - xold) + wf * abs(fx)
        k += 1
        
    if err > tol and k == maxit:
        raise RuntimeError("Error in Approximation")
    
    return [x, fx, err, k]