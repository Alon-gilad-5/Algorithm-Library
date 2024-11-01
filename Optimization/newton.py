import numpy as np
def generic_newton (f , df, ddf, x0 ,k):
    """
    this method returns an k-iterations approximation to a minimum of f
    f   - given function
    df  - deverative of f
    ddf - second derevative of f
    x0  - starting point to the function
    k   - number of iterations
    """
    g = df
    dg = ddf
    results = []
    x = []
    x.append(x0)
    results.append(f(x0))
    counter = 0

    while(counter < k):
        curr_res = x[counter] - g(x[counter])/dg(x[counter])
        results.append(f(curr_res))
        x.append(curr_res)
        counter = counter + 1

    results = np.array(results)
    return x[-1] , results