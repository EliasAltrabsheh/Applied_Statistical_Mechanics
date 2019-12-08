import math, random

def rho_free(x, y, beta):    # free off-diagonal density matrix
    return math.exp(-(x - y) ** 2 / (2.0 * beta))


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
N = 10                                             # number of slices
dtau = beta / N
delta = 1.0                                       # maximum displacement on one slice
n_steps = 1000000                                 # number of Monte Carlo steps
x = [0.0] * N                                     # initial path

x_temp = []
for step in range(n_steps):
    k = random.randint(0, N - 1)                  # random slice
    knext, kprev = (k + 1) % N, (k - 1) % N       # next/previous slices
    x_new = x[k] + random.uniform(-delta, delta)  # new position at slice k
    old_weight  = (rho_free(x[knext], x[k], dtau) *
                   rho_free(x[k], x[kprev], dtau) *
                   math.exp(-0.5 * dtau * x[k] ** 2))
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-0.5 * dtau * x_new ** 2))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    #print x
    if step % 10 == 0:
        x_temp = x

pylab.hist(x_temp,  normed='True')
pylab.xlabel('$x$', fontsize=16)
pylab.ylabel('$\pi(x)$', fontsize=16)

##pylab.plot(x, y, linewidth=1.5, color='r')
pylab.title(' normalized\
        \n histogram for '+str(len(pi_of_x))+' samples',fontsize=16)

pylab.show()
