probabilities# Lecture 1: Introduction to Monte Carlo
## Monte Carlo sampling
Monte Carlo is all about sampling, the lecturer starts off explaining the types of sampling such as "direct sampling". You have a square with a circle inside it, if you sample enough, you can compute pi from ratio of area of circler to area of square. The area of the circle is Pi and the area of the square is 4. the ratio of the circle to square is pi/4.

For example: if we sample 4000, we might get 3152 hits. This is shown in the following program.

```python
import random

n_trials = 4000
n_hits = 0
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    if x**2 + y**2 < 1.0:
        n_hits += 1
print 4.0 * n_hits / float(n_trials)

```

For the parameters *x* and *y*, they both are uniform random numbers being drawn across the space of **[-1,1]**. we then use trig identity that x<sup>2</sup> + y<sup>2</sup> = z<sup>2</sup>. Imagining that we can have it to be out of circle if side of triangle is larger than 1.

To calculate multiple runs to get the accurate calculation of pi, we have an additional multi-run you can apply.

```python
import random

def direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x ** 2 + y ** 2 < 1.0:
            n_hits += 1
    return n_hits

n_runs = 1000
n_trials = 4000
for run in range(n_runs):
    print 4.0 * direct_pi(n_trials) / float(n_trials)
```

## Markov-chain sampling

Using the analogy of throwing stones into the square-circle. We can sample the whole square, if stones hit outside the circle, we replace stone with new until we reach back into circle target.

Sample code is expanded as following:

```python
import random

x, y = 1.0, 1.0 # x and y represent the square sides ( x axis and y axis)
delta = 0.1  # delta is the random displacment ( this can be variable)
n_trials = 10000
n_hits = 0
for i in range(n_trials):
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
        x, y = x + del_x, y + del_y
    if x**2 + y**2 < 1.0: n_hits += 1
print 4.0 * n_hits / float(n_trials)

```

The additional lines for the Markov bit, show to count deleted samples until they are at least 1 such that they are in the circle. We can also run this multiple times tio get this more accurate if we take a mean.

### pebble game

The aim is spread out these stones(pebbles) even across the square. Imagine now some simple roles and you have a 3 * 3 square ( like knots and crosses ). We have a pebble in the top-right corner, it can either move left or down, we can formulae some rules on this. This is know a transitions probabilities

1)   Top-right corner : *p(a->a) + p(a->b) + p(a ->c) = 1*

consider we run this program many -many times until we reached steady state. We cam calculate the configuration as the following :

2)   **$\pi_a$**     = **$\pi_a$** *p(a->a)* + **$\pi_b$** *P(b ->a)* +  **$\pi_c$***  *P(c ->a)*

if we join **equation 1 & 2)**, we get the following:

$$\pi_a p(a->b) +  \pi_a p(a->c) = \pi_b p(b->a) +  \pi_c p(c->a)$$

This equation is referred too the *(global balance condition*, the set probabilities for Monte Carlo must satisfy this condition.


Also, we can have the *detailed condition* case that a = b = c.

$$ \pi_a p(a->b) = \pi_a p(a->b) \\
\pi_a p(a->b) = \pi_c p(a->c) $$


code of the pebble game of the celebrated Metropolis algorithms defined below.


```python
import random

import random

neighbor =  [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
             [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
             [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]
t_max = 4
site = 8
t = 0
print site
while t < t_max:
    t += 1
    site = neighbor[site][random.randint(0, 3)]
    print site

```



### Inhomogeneous 3x3 pebble game.

This begins with stating that the pebble should be twice as often as top right corner than middle row and 4 times larger upper left corner.

We need to look at details balance condition to resolve this. that such the probabilities of moving from a and b are equal.

$$ P(a-> b) = min (1,\frac{\pi_{(b)}}{\pi_{a}} ) $$

This is the case if the constant probabilities of pi and that its = 1 when both transition probabilities are the same.

suppose you have the following table:

| 2        |0.5          | 1.0 |
| :-------------: |:-------------:| :-----:|
| 0.5      | 1.0 | 0.5 |
| 3     | 0.5      |   1.0 |

if we want to move, Centre left field that has a probability of going down by 1/4. We should accept move by min(1,3/0.5) = min(1,6) = 1 ( so we should accept by 1)


 ##Conclusion of lecture

 * two type of sampling using Monte Carlo
 1) direct sampling
 2) Markov chain sampling ( used discretized version)

 * Global balance criteria
