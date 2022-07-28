from simplelhs import LatinHypercubeSampling

# create object
lhs = LatinHypercubeSampling(3)

# sample random Latin Hypercube design
hc_rand = lhs.random(5)

print("Random Latin Hypercube design:")
print(hc_rand)

# sample Maximin Latin Hypercube design
hc_maximin = lhs.maximin(5, 1000)

print("Maximin Latin Hypercube design:")
print(hc_maximin)
