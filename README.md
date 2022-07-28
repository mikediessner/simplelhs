# simplelhs
Simple implementation of Latin Hypercube Sampling.

# Example

The example below shows how to sample a random Latin Hypercube design with five points for three inputs.

```python
from simplelhs import LatinHypercubeSampling

lhs = LatinHypercubeSampling(3)
hc = lhs.random(5)

print(hc)
```

```
[[0.65830165 0.26660356 0.78491755]
 [0.42168063 0.43244666 0.979281  ]
 [0.39058169 0.76099351 0.34764726]
 [0.07122137 0.15507069 0.58082752]
 [0.87530571 0.94575193 0.03949576]]
 ```

The example below shows how to sample a Maximin Latin Hypercube design with five points for three inputs. Out of 1000 randomly sampled Latin Hypercube designs the design with the maximal minimal distance between points is selected.

```python
from simplelhs import LatinHypercubeSampling

lhs = LatinHypercubeSampling(3)
hc = lhs.maximin(5, 1000)

print(hc)
```

```
[[0.74819463 0.30320436 0.44740315]
 [0.04272589 0.04285395 0.64291632]
 [0.23792251 0.45723098 0.04046911]
 [0.57580627 0.70606249 0.94469312]
 [0.96656601 0.9932299  0.29306131]]
 ```
 