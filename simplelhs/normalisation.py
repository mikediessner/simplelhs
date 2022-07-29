def normalise(x, lower, upper):
    """
    Normalise data to the range [0, 1].

    Parameters
    ----------
    x : ndarray
        Data that should be scaled where each row represents one of n data points and each column represents one of d input dimensions.
    lower : scalar or narray
        Scalar or one-dimensional array specifying the lower bounds for each dimension of x.
    upper: scalar or narray
        Scalar or one-dimensional array specifying the upper bounds for each dimension of x.
    """

    return (x - lower)/(upper - lower)


def unnormalise(x, lower, upper):
    """
    Reverse normalisation to the range [lower, upper].

    Parameters
    ----------
    x : ndarray
        Data that should be scaled where each row represents one of n data points and each column represents one of d input dimensions.
    lower : scalar or narray
        Scalar or one-dimensional array specifying the lower bounds for each dimension of x.
    upper: scalar or narray
        Scalar or one-dimensional array specifying the upper bounds for each dimension of x.
    """

    return x * (upper - lower) + lower
