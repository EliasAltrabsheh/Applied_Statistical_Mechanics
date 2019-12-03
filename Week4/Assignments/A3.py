import random, math

x, y, z = 0.0, 0.0, 0.0
delta = 0.1
n_trials = 1000000
n_hits = 0
for i in range(n_trials):
    xnew = x + random.uniform(-delta, delta)
    ynew = y + random.uniform(-delta, delta)
    znew = z + random.uniform(-delta, delta)
    if xnew ** 2 + ynew ** 2 + znew ** 2 < 1.0:
        x, y, z = xnew, ynew, znew
    alpha = random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 + z ** 2 + alpha ** 2 < 1.0:
        n_hits += 1
print '%f' % (2.0 * n_hits / float(n_trials))
print '%f' % (3.0 * math.pi / 8.0)
