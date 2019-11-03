# Tutorial 1: Exponential convergence and the 3x3 pebble game

We are focused on main tool of sampling that will allow us to illustrate that the MCMC will converge to exponential that will be in equilibrium.

equilibrium  converged by:

$$  \exp^{-\frac{t}{\tau}}$$

an example of this is the radio active half life, the compound becomes more stable.

We can now look at the sample of the simple pebble game in python code.


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

For the code, 0 = right, 1 = up , 2 = left and 3 = down

we can use the following matrix to help with our questions:

```python
-------
|6,7,8|
|3,4,5|
|0,1,2|
-------
```
1) if the pebble is at site 8 at t =0on which site can it be at t =1 ?

* site  = 7 with P(s) = 1/4
* site = 5 with P(s) = 1/4
* site = 8 with P(s) = 1/2

2) if the pebble is at side 8 , at what time can it be at side 0 that it becomes finite?
* t = 4
3) What is the probability be at side 0 at time = 4, given that it started at side 8 at t = 0?

* side 8 -> side 8 = 1/2 * 1/2 * 1/2 * 1/2 = 1/8
* answer = 6/256 = (6/4^4)


## Transfer method Matrix

Allows to solve exactly the Monte Carlo dynamic of the 3 * 3 pebble games. For larger systems this does not apply.

to compute the probabilities of the pebble at all times we need to introduce a vector.
that $$ \pi^{t} = (\pi^{0} ....) $$.

The matrix in this game is 9 * 9 as there are 9 configurations, if we fill in the entire matrix.The t+1 vector of pi is a result of the transfer matrix product with pi vector at time t = 0 . Code of this transfer is shown as


```python
import numpy

neighbor =  [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
             [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
             [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]
transfer = numpy.zeros((9, 9))
for k in range(9):
    for neigh in range(4): transfer[neighbor[k][neigh], k] += 0.25
position = numpy.zeros(9)
position[8] = 1.0
for t in range(100):
    print t,'  ',["%0.5f" % i for i in position]
    position = numpy.dot(transfer, position)

```

The output of this is the entire Monte Carlo dynamic for an infinite number of pebble games and its exact. We end up getting the equilibriem probability.

What we have found from this is by finding the Eigen vectors and values, we can derive a step closer on our convergence equation mention at start of lesson as:

$$  \exp^{-\frac{t}{\tau}}$$

 where $\tau$ is = 3.476 (correlation time)

 Our Eigen values are calculated by following program:
```python
 import numpy
 numpy.set_printoptions(suppress=True)
 neighbor =  [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
              [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
              [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]
 transfer = numpy.zeros((9, 9))
 for k in range(9):
     for neigh in range(4): transfer[neighbor[k][neigh], k] += 0.25
 eigenvalues, eigenvectors = numpy.linalg.eig(transfer)
 print eigenvalues.

 # you may print the eigenvectors by uncommenting the following lines...
 #for iter in range(9):
 #    print eigenvalues[iter]
 #    for i in range(9):
 #       print eigenvectors[i][iter]


```

with results in our list as :
```python
[-0.5   1.    0.75  0.    0.5   0.25  0.75  0.    0.25]
```

## Irreducibility and aperiodic in the Markov chain

All eigenvalues have modulus less than or equal to one, an eigenvalue larger than one would lead to an explosion of the probability at large time. At large times, the dynamics converges to the eigenvector with the largest eigenvalue equal to one. this is what we will call the probability vector of the equilibrium state, or the steady state. When does this picture really apply?

What are the rigorous mathematical conditions ensuring that one converges at large times to a unique steady state?


This is what we will find out in the final part of this tutorial.

 There is a simple physical example in which a strange phenomenon occurs. Consider a system in which you have two copies of the 3x3 pebble game, one in red and one in blue. In each of these games, the pebble jumps from site to site with the same rules as we have seen before.


 If it is started in the red one, it will remain there forever and if it is started in the blue one the same thing will happen.

 The combined system is described by a 18x18 transfer matrix because we now have 18 sites. There are lot of zeros in this matrix indicating that the pebble cannot jump from the red game to the blue game and vice versa.

 In fact, we are in an annoying and physically unacceptable situation, where the outcome of the simulation depends on the starting configuration even at infinite times. We are also in a mathematically annoying situation, because the transfer matrix of our dual pebble game has two eigenvalues one.


 This is described in the program pebble_dual_eigen.py. Mathematicians describe this situation that we must avoid as stemming from the reducibility of the transfer matrix of our dual game. Reducible means that we can split apart the transfer matrix of our system into two subsystems without affecting the rest.

  One of the two mathematically rigorous conditions, for a Monte Carlo Markov chain algorithm is that this pulling apart is not possible, that would be irreducible. We can in fact render our dual pebble game irreducible, by adding a small probability of transition between the two games as depicted here. We now observe that the pebble can change its game.

  This small probability can also be observed in the transfer matrix in the program pebble_dual_eigen.py, where it allows to recover a unique eigenvector of eigenvalue one that is to say, a unique steady state. We realize we must have a unique eigenvector of eigenvalue one, ensuring that the matrix is irreducible. In fact, this is not enough. We need a second condition, ensuring that the probability converges to the steady state, in the large time limit.

  Main points( mathematics conditions) for MCMC is that :

  1. aperiodic : Must not get in a recurring state where we are sure to find it in fixed time
  2. MC must satisfy global balance
  3. Irreducibility 
