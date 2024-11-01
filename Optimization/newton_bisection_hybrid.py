import numpy as np


def generic_hybrid(f, df, ddf, l, u, x0, eps, k):
    """
    This method returns a k-iterations approximation to a minimum of f
    using the Newton's method and bisection method.

    f   - given function
    df  - derivative of f
    ddf - second derivative of f
    l   - lower bound
    u   - upper bound
    x0  - starting point to the function
    eps - epsilon (accuracy level)
    k   - number of iterations
    """
    x = [x0]
    fv = [f(x0)]
    g = df
    dg = ddf
    counter = 0

    # Loop until the desired number of iterations (k) is reached
    while counter < k:

        # Step 1: Perform a Newton's method update to approximate the root of g
        # Newton's method formula: x_newt = x - g(x) / g'(x)
        x_newt = x[-1] - g(x[-1]) / dg(x[-1])

        # Step 2: Check if the Newton step is within bounds and effectively reduces g(x)
        # - Condition 1: The new estimate (x_newt) must lie within the interval [l, u]
        # - Condition 2: g(x_newt) should be significantly smaller than g(x[-1]) to ensure convergence
        if (l <= x_newt <= u) and np.abs(g(x_newt)) < (0.99 * np.abs(g(x[-1]))):
            # If both conditions are met, accept the Newton step as the next x value
            x_next = x_newt
        else:
            # Step 3: Use the midpoint of [l, u] if Newton's method does not meet the criteria
            # This acts as a fallback to ensure x_next is within the interval and to continue the search
            x_next = (l + u) / 2

        # Step 4: Add the new reached point to x which stores all the values we reached so far
        # Also store the value of f for the new point in fv which stores function values

        x.append(x_next)
        fv.append(f(x_next))

        # Step 5: Check if we reached a point where we can stop searching for min
        # Condition 1: The change between following iterations should be bigger than eps otherwise stop
        # Condition 2: If the value of g at the reached point is smaller than the acceptable error stop
        if np.abs(x_next - x[-2]) < eps and np.abs(g(x_next)) < eps:
            break

        # Step 6: Update the bisection boundaries with respect to the new reached point
        if g(u) * g(x_next) > 0:
            u = x_next
        else:
            l = x_next

        counter += 1
    # Step 7: Return the last reached point and the array of values of f for all reached points
    return x[-1], np.array(fv)
