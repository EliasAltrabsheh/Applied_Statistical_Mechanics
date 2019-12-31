import math, random, pylab

def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

def pi_x(x, beta):
    sigma = 1.0 / math.sqrt(2.0 * math.tanh(beta / 2.0))
    return math.exp(-x ** 2 / (2.0 * sigma ** 2)) / math.sqrt(2.0 * math.pi) / sigma

beta = 2.0
nsteps = 1000000
low = levy_harmonic_path(2)
high = low[:]
data = []
for step in xrange(nsteps):
    data += low
    k = random.choice([0, 1])
    low[k] = levy_harmonic_path(1)[0]
    high[k] = low[k]
    #print high[k]
    data.append(high[k])

# graphics part

pylab.hist(data, bins=100, normed=True, )
list_x = [0.01 * i for i in range(-300, 301)]
pylab.plot(list_x, [pi_x(xx,beta) for xx in list_x], 'r-', label='analytic')
pylab.legend()
pylab.xlabel('$x$')
pylab.title('histogram of the positions of particles 0 and 1')
pylab.savefig('plot_A1.png')
pylab.show()
