import math, random, pylab

def rho_free(x, y, beta):    # free off-diagonal density matrix
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

def V(x, cubic, quartic):
    pot =  x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4
    return pot

def read_file(filename):
    list_x = []
    list_y = []
    with open(filename) as f:
        for line in f:
            x, y = line.split()
            list_x.append(float(x))
            list_y.append(float(y))
    f.close()
    return list_x, list_y

beta = 4.0
quartic = 1.0
cubic = -quartic
N = 16
dtau = beta / N
delta = 1.0
n_steps = 40000000
x = [0.0] * N
samples_x = []
for step in xrange(n_steps):
    k = random.randint(0, N - 1)                  # random slice
    knext, kprev = (k + 1) % N, (k - 1) % N       # next/previous slices
    x_new = x[k] + random.uniform(-delta, delta)  # new position at slice k
    old_weight  = (rho_free(x[knext], x[k], dtau) *
                   rho_free(x[k], x[kprev], dtau) *
                   math.exp(-dtau * V(x[k], cubic, quartic)))
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-dtau * V(x_new, cubic, quartic)))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    if step % 10 == 0:
        samples_x.append(x[0])

pylab.hist(samples_x, normed=True, bins=100, label='QMC')
x, pi_x = read_file('data_anharm_matrixsquaring_beta' + str(beta) + '_quartic' + str(quartic) + '.dat')
pylab.plot(x, pi_x, 'r', label='matrix squaring')
pylab.xlim(-2, 2)
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('$\pi(x)$')
pylab.title('Anharmonic oscillator (cubic=-quartic=%s)' % cubic)
pylab.savefig('plot_C2_beta%s.png' % beta)
pylab.show()
