import random, math

def prob(x):
    s1 = math.exp(-(x + 1.2) ** 2 / 0.72)
    s2 = math.exp(-(x - 1.5) ** 2 / 0.08)
    return (s1 + 2.0 * s2) / math.sqrt(2.0 * math.pi)

delta = 0.1
nsteps = 1000000
acc_tot = 0
acc_tmp = 0
x = 0.0
x_av = 0.0
for step in xrange(nsteps):
    if(step % 100 == 0):
        if (acc_tmp > 60):
            delta = delta * 1.1
        else:
            delta = delta / 1.1
        acc_tmp = 0

    xnew = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) < prob(xnew) / prob(x):
        x = xnew
        acc_tot += 1
        acc_tmp += 1
    x_av += x

print 'global acceptance ratio:', acc_tot / float(nsteps)
print '<x> =', x_av / float(nsteps)
