import numpy as np


def bisection(g, a, b, eps, N):
    """
    this function returns the stationary points for function f ( df = g)
    :param g: derivative of f. this is the target function
    :param a: lower-bound
    :param b: upper-bound
    :param eps: acceptable error rate
    :param N: number of iterations
    :return: the minimum of the function g
    """
    # Firstly we need to check that the input is suitable for our algorithm
    try:
        while g(a)*g(b) > 0:
            if g(a) > 0:
                a *= 2
            if g(b) < 0:
                b *= 2
    except Exception as e:
        print("this function is not suitable for bisection method", e)
    lb = a
    ub = b
    for i in range(N-2):
        if np.abs(ub - lb) < eps:
            print(f"The function converged after {i + 1} iterations")
            return np.abs(ub - lb)
        h = (ub + lb) / 2
        if g(h) * g(ub) > 0:
            ub = h
        else:
            lb = h
        print('%.4e %.4e %.4e\n' % (lb, ub, np.abs(ub - lb)))
    print(f"a = {lb}")
    print(f"b = {ub}")
    return np.abs(ub - lb)
