import random

N = 15
L = 10.0
sigma = 0.1
n_configs = 100
for config in range(n_configs):
    x = [] # empty array that will hold positions of pins
    while len(x) < N: # Check length of  array
        x.append(random.uniform(sigma, L - sigma))
        for k in range(len(x) - 1):
            if abs(x[-1] - x[k]) < 2.0 * sigma:# check distance of new pins
                x = [] # if we overlap we do the tabla - rusa rule
                break
    print x
