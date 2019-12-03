import random, math

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

d = 199
x = [0.0] * d
old_radius_square = 0.0
delta = 0.1
n_trials = 20000000
n_hits = 0
for i in range(n_trials):
    k = random.randint(0, d - 1)
    x_old_k = x[k]
    x_new_k = x_old_k + random.uniform(-delta, delta)
    new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
    if new_radius_square < 1.0:
        x[k] = x_new_k
        old_radius_square = new_radius_square
    if old_radius_square + random.uniform(-1.0, 1.0) ** 2 < 1.0:
        n_hits += 1
print '<Q_%i> = %f' % (d + 1, 2.0 * n_hits / float(n_trials))
print 'Q_%i   = %f' % (d + 1, V_sph(d + 1) / V_sph(d))
