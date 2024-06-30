import numpy as np

def getSlope(f0, f1, x0, x1):
    return (f1 - f0) / (x1 - x0)

def getDerivative(f, x, i):
    h = np.sqrt(np.finfo(float).eps)

    match i:
        case -1: #Backward
            df = (f(x) - f(x - h)) / h

        case 0: #Centered
            df = (f(x+h) - f(x-h)) / (2*h)

        case 1: #Forward
            df = (f(x+h) - f(x)) / h
    return df

def update(x, fx, q):
    return x - fx / q