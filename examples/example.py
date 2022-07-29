import numpy as np
from simplelhs import LatinHypercubeSampling, unnormalise

# create object
lhs = LatinHypercubeSampling(3)

# sample from random Latin Hypercube Design
hc_rand = lhs.random(5)

print("Random Latin Hypercube sample:")
print(hc_rand)

# sample from Maximin Latin Hypercube Design
hc_maximin = lhs.maximin(5, 1000)

print("Maximin Latin Hypercube sample:")
print(hc_maximin)

# scale to specific bounds
lower = np.array([0., -5., 10.,])
upper = np.array([1., 5., 40.])
hc_maximin_scaled = unnormalise(hc_maximin, lower, upper)

print("Scaled Maximin Latin Hypercube sample:")
print(hc_maximin_scaled)
