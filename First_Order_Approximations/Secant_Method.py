from utility.utility_module1 import getSlope

def secant(f, x0, x1, maxit, tol, wa = 0.5, wf = 0.5):
    err  = tol + 1
    f0 = f(x0)
    f1 = f(x1)
    k = 1

    while err > tol and k < maxit:
        q = getSlope(f0, f1, x0, x1)

        #I think pwede nang di gumamit ng xtemp??
        #Update x1
        xtemp = x1
        x1 = x1 - f1 / q

        #Update x0 and f0
        x0 = xtemp
        f0 = f1

        #Update f1
        f1 = f(x1)

        #Calculate error and update k
        err = wa * abs(x1 - x0) + wf * abs(f1)
        k += 1

    if err > tol and k == maxit:
        raise RuntimeError("Error in Approximation")
    return [x1, f1, err, k]