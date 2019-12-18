import math, random, pylab

def psi_0_square(x):
    psi = math.exp(-x ** 2 / 2.0) * math.pi ** (-1.0 / 4.0)
    return psi ** 2

x = 0.0
delta = 2.0
nsteps = 1000000
samples_x = []
for step in range(nsteps):
    xnew = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) < psi_0_square(xnew) / psi_0_square(x):
        x = xnew
    samples_x.append(x)
# graphics part
pylab.hist(samples_x, bins=100, normed=True, label='MC')
list_x = [0.01 * i for i in range(-300, 301)]
pylab.plot(list_x, [psi_0_square(xx) for xx in list_x], 'r-', label='analytic')
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('$|\psi_0(x)|^2$')
pylab.title('Harmonic oscillator: sampling $|\psi_0(x)|^2$')
pylab.savefig('plot_A1_psi0_square.png')
pylab.show()
