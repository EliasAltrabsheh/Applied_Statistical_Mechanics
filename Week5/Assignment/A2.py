import math, random, pylab

def psi_n_square(x, n):
    if n == -1:
        return 0.0
    else:
        psi = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]
        psi.append(math.sqrt(2.0) * x * psi[0])
        for k in range(2, n + 1):
            psi.append(math.sqrt(2.0 / k) * x * psi[k - 1] -
                       math.sqrt((k - 1.0) / k) * psi[k - 2])
        return psi[n] ** 2

beta = 1.0
nsteps = 5000000
delta = 1.0
samples_x = []
x = 1.0
n = 1
for step in range(nsteps):
    # move 1
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) < psi_n_square(x_new, n) / psi_n_square(x, n):
        x = x_new
    # move 2
    delta_n = random.choice([-1, 1])
    n_new = n + delta_n
    p_acc = math.exp(- beta * delta_n) * psi_n_square(x, n_new) / psi_n_square(x, n)
    if random.uniform(0.0, 1.0) < p_acc:
        n = n_new
    # take measures
    if step % 100 == 0:
        samples_x.append(x)

def pi_class(x, beta):
    return math.exp(-beta * x ** 2 / 2.0) * math.sqrt(beta / (2.0 * math.pi))

def pi_quant(x, beta):
    return math.exp(-x ** 2 * math.tanh(beta / 2.0)) * math.sqrt(math.tanh(beta / 2.0) / math.pi)

pylab.hist(samples_x, bins=100, normed=True, label='MC')
dx = 0.01
list_x = [dx * i for i in range(-1000, 1001)]
prob_quant_x = [pi_quant(xx, beta) for xx in list_x]
prob_class_x = [pi_class(xx, beta) for xx in list_x]
pylab.plot(list_x, prob_quant_x, label='pi_quant')
pylab.plot(list_x, prob_class_x, label='pi_class')
pylab.xlabel('position $x$')
pylab.ylabel('$\mathrm{prob}(x)$')
pylab.title('harmonic oscillator - beta=%s' % beta)
pylab.legend()
pylab.savefig('plot_A2_beta%s_prob_x.png' % beta)
pylab.show()
