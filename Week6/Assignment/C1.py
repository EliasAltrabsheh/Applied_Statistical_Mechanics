import math, random, pylab

def V(x, cubic, quartic):
    pot = x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4
    return pot

def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / \
                 (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
    return x

beta = 20.0
cubic = -1.0
quartic = 1.0
N = 100
Ncut = 15
dtau = beta / N
n_steps = 1000000
x = [0.1] * N
old_Trotter_weight = math.exp(sum(-V(a, cubic, quartic) * dtau for a in x))
data = []
n_acc = 0
for step in xrange(n_steps):
    x_new = levy_free_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
    new_Trotter_weight = math.exp(sum(-V(a, cubic, quartic) * dtau for a in x_new))
    if random.uniform(0.0, 1.0) < new_Trotter_weight / old_Trotter_weight:
        n_acc += 1
        old_Trotter_weight = new_Trotter_weight
        x = x_new[:]
    x = x[1:] + x[:1]
    k = random.randint(0, N - 1)
    data.append(x[k])
print 'acceptance rate:', n_acc / float (n_steps)

pylab.hist(data, normed=True, bins=80)
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.title('levy_free + anharmonic Trotter correction\n(beta=%s, N=%i)' % (beta, N))
pylab.xlim(-1.5, 2.0)
pylab.savefig('plot_C1_beta%s.png' % beta)
pylab.show()
