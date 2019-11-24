import random

N = 10
L = 20.0
sigma = 0.75
n_runs = 800
for run in range(n_runs):
    y = [random.uniform(0.0, L - 2 * N * sigma) for k in range(N)]
    y.sort()
    print [round(y[i] + (2 * i + 1) * sigma,4) for i in range(N)]

"""
We can comuaute patrion function of this alogorthim by
$$Z(N) = int_{sigma}^{L-sigma)} dx_{0}\pi(x0 ....)$$ ...
"""
