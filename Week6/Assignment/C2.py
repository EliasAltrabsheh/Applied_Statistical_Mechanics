import math, random, pylab

def V_anharm(x, cubic, quartic): # using only the anharmonic part
    pot =  cubic * x ** 3 + quartic * x ** 4
    return pot

def levy_harmonic_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + \
               1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + \
               xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, \
               1.0 / math.sqrt(Ups1)))
    return x

beta = 20.0
cubic = -1.0
quartic = 1.0
N = 100
Ncut = 25
dtau = beta / N
n_steps = 1000000
x = [0.1] * N
old_Trotter_weight = math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x))
data = []
n_acc = 0
for step in xrange(n_steps):
    x_new = levy_harmonic_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
    new_Trotter_weight = math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x_new))
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
pylab.xlim(-1.5, 2.0)
pylab.title('levy_harmonic + anharmonic Trotter correction\n(beta=%s, N=%i)' % (beta, N))
pylab.savefig('plot_C2_beta%s.png' % beta)
pylab.show()
