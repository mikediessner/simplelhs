# simplelhs
Simple implementation of Latin Hypercube Sampling.

[![Downloads](https://static.pepy.tech/badge/simplelhs)](https://pepy.tech/project/simplelhs)

# Example

The example below shows how to sample from a random Latin Hypercube Design with five points for three inputs.

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

The example below shows how to sample from a Maximin Latin Hypercube Design with five points for three inputs. Out of 1000 randomly sampled Latin Hypercube samples the sample with the maximal minimal distance between points is selected.

```python
from simplelhs import LatinHypercubeSampling

lhs = LatinHypercubeSampling(3)
hc = lhs.maximin(5, 1000)

print(hc)
```

```
[[0.24607101 0.11399068 0.5456922 ]
 [0.88731638 0.40600431 0.32305333]
 [0.47416121 0.99487745 0.03087923]
 [0.06288706 0.7227211  0.78248764]
 [0.77081332 0.36862214 0.99449703]]
 ```
 
To scale the data to unit cube and back to its original range the functions `normalise()` and `unnormalise()` are provided. The example below scales the Maximin Latin Hypercube sample back to its original range.

```python
from simplelhs import unnormalise

lower = np.array([0., -5., 10.,])
upper = np.array([1., 5., 40.])
hc_maximin_scaled = unnormalise(hc_maximin, lower, upper)

print(hc_maximin_scaled)
```

 ```
 [[ 0.24607101 -3.86009322 26.37076609]
 [ 0.88731638 -0.93995687 19.69159997]
 [ 0.47416121  4.94877447 10.92637679]
 [ 0.06288706  2.22721099 33.47462916]
 [ 0.77081332 -1.31377864 39.83491091]]
 ```
