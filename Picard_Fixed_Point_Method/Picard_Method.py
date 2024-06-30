def fixPoint(g, x, maxit, tol):
    err = tol + 1
    k = 0

    while err > tol and k < maxit:
        xold = x
        x = g(x)
        err = abs(x - xold)
        k += 1
    if err > tol and k == maxit:
        raise RuntimeError("Error in Approximation")
    
    return [x, xold, err, k]