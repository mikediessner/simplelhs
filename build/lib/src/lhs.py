import numpy as np
from scipy.spatial.distance import pdist


class LatinHypercubeSampling:

    def __init__(self, dims):
        """
        Latin hypercube sampling.

        Attributes
        ----------
        dims : int
            Number of dimensions for the Latin hypercube sample.

        Examples
        --------
        >>> lhs = LatinHypercubeSampling(3)
        >>> hc = lhs.maximin(3, 1000)
        >>> print(hc)
        [[0.59649698 0.88939696 0.94479167]
         [0.04031957 0.15612151 0.46349955]
         [0.94145643 0.37355910 0.05135256]]
        """

        self.dims = dims

    def random(self, points):
        """
        Draw a random Latin hypercube Sample.

        1. Pick random permutations of the set (0, 1, ..., points-1) for each
           dimension. Each integer defines the quantile to which the final
           value has to belong to.
        2. Translate the integers to the [0, 1] range.
        3. Sample and add an individual random uniform sample U(0, 1/points)
           to each value.

        Parameters
        ----------
        points : int
            Number of points for the Latin hypercube sample.

        Returns
        -------
        hypercube : ndarray
            n x d array containing the random Latin hypercube sample where n
            is the number of points and d is the number of dimensions.
        """

        hypercube = np.empty((points, self.dims))

        # pick random permutation of (1, ..., points) for each dimension
        for dim in range(self.dims):
            hypercube[:, dim] = np.random.permutation(points)

        # translate each dimension to [0, 1] range
        increment = 1/points
        hypercube = hypercube * increment

        # pick random value within increment
        hypercube = hypercube + np.random.uniform(low=0.0, high=increment,
                                                  size=hypercube.shape)

        return hypercube

    def maximin(self, points, samples=1000):
        """
        Draw a maximin Latin hypercube sample.

        1. Draw a large number of random Latin hypercube samples.
        2. Compute the minimal distance between the points for each random
           Latin hypercube sample.
        3. Pick the random Latin hypercube sample with the largest minimal
           distance.

        Parameters
        ----------
        points : int
            Number of points for the Latin hypercube sample.
        samples : int
            Number of random Latin hypercube samples that should be considered.

        Returns
        -------
        maximin_hypercube : ndarray
            n x d array containing the maximin Latin hypercube sample where n
            is the number of points and d is the number of dimensions.
        """

        hypercubes = np.empty((samples, points, self.dims))
        min_dist = np.empty(samples)

        for sample in range(samples):

            # sample random Latin hypercubes
            hypercubes[sample, :, :] = self.random(points)

            # compute minimal distance of all samples
            min_dist[sample] = np.min(pdist(hypercubes[sample, :, :]))

        # pick hypercube with maximal minimal distance
        maximin_index = np.argmax(min_dist)
        maximin_hypercube = hypercubes[maximin_index]

        return maximin_hypercube