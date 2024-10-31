import numpy as np


def gss(f, a, b, eps, N):
    """
    :param a: left bound
    :param b: right bound
    :param f: target function
    :param eps: acceptable error
    :param N: num of iterations
    :return: the minimum of the function
    """
    golden_ratio = (-1 + np.sqrt(5)) / 2
    x2 = a + (1 - golden_ratio)*(b - a) #updating step
    fx2 = f(x2)
    x3 = a + golden_ratio * (b - a) #updating step
    fx3 = f(x3)
    print('%.4e %.4e %.4e %.4e %.4e\n' % (x2, x3, fx2, fx3, b-a))

    for i in range(N - 2):
        if fx2 < fx3:
            b = x3
            x3 = x2
            x2 = a + (1 - golden_ratio)*(b - a)
            fx3 = f(x3)
            fx2 = f(x2)
        else:
            a = x2
            x2 = x3
            x3 = a + golden_ratio * (b - a)
            fx3 = f(x3)
            fx2 = f(x2)
        print('%.4e %.4e %.4e %.4e %.4e\n' % (x2, x3, fx2, fx3, b-a))
        if np.abs(b - a) < eps:
            print(f"The function converged after {i + 1} iterations")
            break
    print(f"a = {a}")
    print(f"b = {b}")
    return np.abs(b - a)

