from utility.utility_module1 import getSlope

def regula_falsi(func, x0, x1, maxit, tol, wa = 0.5, wf = 0.5):

    err = tol + 1
    x = []
    x.append(x0)
    x.append(x1)
    f = []
    f.append(func(x0))
    f.append(func(x1))
    k = 1

    while err > tol and k < maxit:
        xc = x[k]
        fc = f[k]

        k_tilde = k - 1

        x_tilde = x[k_tilde]
        f_tilde = f[k_tilde]
        
        while f_tilde * fc >= 0 and k_tilde >= 1:
            k_tilde -= 1
            x_tilde = x[k_tilde]
            f_tilde = f[k_tilde]

        if k_tilde == 1:
            k_tilde -= 1
            x_tilde = x[k_tilde]
            f_tilde = f[k_tilde]

        q = getSlope(f_tilde, fc, x_tilde, xc)
        a = xc - fc / q
        x.append(a)
        f.append(func(a))

        err = wa * abs(a-xc) + wf * abs(f[k+1])
        
        k += 1

    if err > tol and k == maxit:
        raise RuntimeError("Error in Approximation")

    return [x.pop(),f.pop(), err, k]