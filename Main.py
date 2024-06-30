from Bisection.Bisection_Method import bisection
from First_Order_Approximations.Chord_Method import chord
from First_Order_Approximations.Secant_Method import secant
from First_Order_Approximations.Regula_Falsi_Method import regula_falsi
from First_Order_Approximations.Inexact_Newton_Method import inexactNewton
from First_Order_Approximations.Steffensen_Method import steffensen
from Picard_Fixed_Point_Method.Picard_Method import fixPoint

import numpy as np

def main():
    a = -2
    b = 2
    tol = 10e-10
    maxit = 1000
    wa = 0.5
    wf = 0.5
    x = 3

    print(inexactNewton(f,-1, x, maxit, tol))
    # print("Method \t Root x \t Iteration k \t Error \t Function Value f(x)")

    # root = inexactNewton(f, -1, x, maxit, tol, wa, wf)
    # print(f"(Backward) Newton-Rhapson \t {root[0]} \t {root[3]} \t {root[2]} \t {root[1]}")

    # root = inexactNewton(f, 0, x, maxit, tol, wa, wf)
    # print(f"(Centered) Newton-Rhapson \t {root[0]} \t {root[3]} \t {root[2]} \t {root[1]}")

    # root = inexactNewton(f, 1, x, maxit, tol, wa, wf)
    # print(f"(Forward) Newton-Rhapson \t {root[0]} \t {root[3]} \t {root[2]} \t {root[1]}")

    # root = steffensen(f, x, maxit, tol, wa, wf)
    # print(f"Steffensen \t {root[0]} \t {root[3]} \t {root[2]} \t {root[1]}")

    # root = fixPoint(g, x, maxit, tol)
    # print(f"Picard Fix Point \t {root[0]} \t {root[3]} \t {root[2]} \t {root[1]}")

def g(x):
    # return np.arccos(np.log(3*np.sin(x)))
    return np.arcsin(np.exp(np.cos(x)) / 3)


def f(x):
    #Roots are 1, 2, and 3
    # return (x ** 3) - 6 * (x ** 2) + 11 * x - 6
    return (x ** 12) - 331776
    # return np.exp(np.cos(x)) - 3 * np.sin(x)

main()

    # a = 0
    # b = 3.5
    # maxit = 10e3
    # tol = 10e-5
    # print(f"Bisection Method \n {bisection(f, a, b, maxit, tol)} \n \n")

    # #The root returned by the chord method does not necessarily have to be within a and b.
    # #a and b are just passed to compute for the fixed qk
    # x = 1.1
    # print(f"Chord Method \n {chord(f, a, b, x, maxit, tol)} \n \n")

    # x0 = a
    # x1 = b
    # print(f"Secant Method \n {secant(f, x0, x1, maxit, tol)} \n \n")

    # print(f"Regula-Falsi Method \n {regula_falsi(f, x0, x1, maxit, tol)} \n \n")

    # x = 1.1
    # print(f"Inexact Newton Method (Backward)\n {inexactNewton(f, -1, x, maxit, tol)} \n \n")
    
    # print(f"Inexact Newton Method (Centered)\n {inexactNewton(f, 0, x, maxit, tol)} \n \n")

    # print(f"Inexact Newton Method (Forward)\n {inexactNewton(f, 1, x, maxit, tol)} \n \n")

    # print(f"Steffensen Method \n {steffensen(f, x, maxit, tol)} \n \n")


    # print(f"Picard Method \n {fixPoint(g, x, maxit, tol)} \n \n")