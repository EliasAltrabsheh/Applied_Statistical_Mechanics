import math, numpy, pylab

def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

def rho_harmonic_trotter(grid, beta):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * 0.5 * (x ** 2 + xp ** 2)) \
                         for x in grid] for xp in grid])

x_max = 8.0
nx = 150
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
beta_tmp = 2.0 ** (-6)
beta     = 2.0 ** 2
rho = rho_harmonic_trotter(x, beta_tmp)
while beta_tmp < beta:
    rho = numpy.dot(rho, rho)
    rho *= dx
    beta_tmp *= 2.0
    print 'beta: %s -> %s' % (beta_tmp / 2.0, beta_tmp)

Z = sum(rho[j, j] for j in range(nx + 1)) * dx
pi_of_x = [rho[j, j] / Z for j in range(nx + 1)]
f = open('data_harm_matrixsquaring_beta' + str(beta) + '.dat', 'w')
for j in range(nx + 1):
    f.write(str(x[j]) + ' ' + str(rho[j, j] / Z) + '\n')
f.close()

def pi_quant(x, beta):
    return math.exp(-x ** 2 * math.tanh(beta / 2.0)) * math.sqrt(math.tanh(beta / 2.0) / math.pi)
pylab.plot(x, pi_of_x, label='matrix-squaring')
pylab.plot(x, [pi_quant(xx, beta) for xx in x], label='analytical')
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('$\pi(x)$')
pylab.title('Matrix-squaring, beta=%s' % beta)
pylab.savefig('plot_B1_matrixsquaring_beta%s.png' % beta)
pylab.show()
