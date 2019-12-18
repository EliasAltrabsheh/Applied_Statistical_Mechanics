import math, numpy, pylab

def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

def V(x, cubic, quartic):
    pot =  x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4
    return pot

def rho_anharmonic_trotter(grid, beta, cubic, quartic):
    return numpy.array([[rho_free(x, xp, beta) * \
                             numpy.exp(-0.5 * beta * (V(x, cubic, quartic) + \
                                                      V(xp, cubic, quartic))) \
                         for x in grid] for xp in grid])

quartic = 1.0
cubic = - quartic
x_max = 8.0
nx = 250
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
beta_tmp = 2.0 ** (-6)
beta     = 4.0
rho = rho_anharmonic_trotter(x, beta_tmp, cubic, quartic)
while beta_tmp < beta:
    rho = numpy.dot(rho, rho)
    rho *= dx
    beta_tmp *= 2.0
    print 'beta: %s -> %s' % (beta_tmp / 2.0, beta_tmp)

Z = sum(rho[j, j] for j in range(nx + 1)) * dx
pi_of_x = [rho[j, j] / Z for j in range(nx + 1)]
f = open('data_anharm_matrixsquaring_beta' + str(beta) + '_quartic' + str(quartic) + '.dat', 'w')
for j in range(nx + 1):    f.write(str(x[j]) + ' ' + str(rho[j, j] / Z) + '\n')
f.close()

pylab.plot(x, pi_of_x)
pylab.xlim(-2, 2)
pylab.xlabel('$x$')
pylab.ylabel('$\pi(x)$')
pylab.title('Matrix-squaring for anharmonic oscillator (quartic=%s)' % quartic)
pylab.savefig('plot_C1_matrixsquaring_beta%s.png' % beta)
pylab.show()
