import random, math, pylab

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

d_max = 199
list_V_sph = [2.0]
delta = 0.1
for d in range(1, d_max + 1):
    x = [0.0] * d
    old_radius_square = 0.0
    n_trials = 150000
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
    list_V_sph.append(list_V_sph[-1] * (2.0 * n_hits / float(n_trials)))
    print d + 1, list_V_sph[-1], V_sph(d + 1)
list_d = range(1, d_max + 2)
pylab.plot(list_d, [V_sph(d) for d in list_d], 'r-', lw=2)
pylab.plot(list_d, list_V_sph, 'k.')
pylab.yscale('log')
pylab.xlabel('dimension $d$')
pylab.ylabel('V_sph(d)')
pylab.savefig('plot_C1_volumes.png')
pylab.show()
