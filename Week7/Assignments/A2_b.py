import math, random, pylab

def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

def rho_harm_1d(x, xp, beta):
    Upsilon_1 = (x + xp) ** 2 / 4.0 * math.tanh(beta / 2.0)
    Upsilon_2 = (x - xp) ** 2 / 4.0 / math.tanh(beta / 2.0)
    return math.exp(- Upsilon_1 - Upsilon_2)


def z(beta):
    return 1.0 / (1.0 - math.exp(- beta))

def pi_two_bosons(x, beta):
    pi_x_1 = math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta / 2.0))
    pi_x_2 = math.sqrt(math.tanh(beta)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta))
    weight_1 = z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta))
    weight_2 = z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta))
    pi_x = pi_x_1 * weight_1 + pi_x_2 * weight_2
    return pi_x

beta = 2.0
nsteps = 500000
low = levy_harmonic_path(2)
high = low[:]
data = []
for step in xrange(nsteps):
    # move 1
    if low[0] == high[0]:
        k = random.choice([0, 1])
        low[k] = levy_harmonic_path(1)[0]
        high[k] = low[k]
        counts_two_cycles += 1
    else:
        low[0], low[1] = levy_harmonic_path(2)
        high[1] = low[0]
        high[0] = low[1]
        counts_one_cycle += 1
    data += low[:]
    # move 2
    weight_old = (rho_harm_1d(low[0], high[0], beta) *
                  rho_harm_1d(low[1], high[1], beta))
    weight_new = (rho_harm_1d(low[0], high[1], beta) *
                  rho_harm_1d(low[1], high[0], beta))
    if random.uniform(0.0, 1.0) < weight_new / weight_old:
        high[0], high[1] = high[1], high[0]

pylab.hist(data, bins=100, normed=True, )
list_x = [0.01 * i for i in range(-300, 301)]
pylab.plot(list_x, [pi_two_bosons(xx,beta) for xx in list_x], 'r-', label='analytic')
pylab.legend()
pylab.xlabel('$x$')
pylab.title('histogram of the positions of particles 0 and 1')
pylab.savefig('plot_A2_a.png')
pylab.show()
