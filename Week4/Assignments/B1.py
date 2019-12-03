import random, math, pylab

d = 20
x = [0.0] * d
old_radius_square = 0.0
delta = 0.1
n_trials = 1000000
data_r = []
for i in range(n_trials):
    k = random.randint(0, d - 1)
    x_old_k = x[k]
    x_new_k = x_old_k + random.uniform(-delta, delta)
    new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
    if new_radius_square < 1.0:
        x[k] = x_new_k
        old_radius_square = new_radius_square
    data_r.append(math.sqrt(old_radius_square))

list_r = [i * 0.01 for i in range(101)]
list_Pr = [r ** (d - 1) * float(d) for r in list_r]
pylab.hist(data_r, bins=100, normed=True)
pylab.plot(list_r, list_Pr, 'r-', lw=3)
pylab.title('$r$ distribution in $d=%i$ dimensions' % d)
pylab.xlabel('$r$')
pylab.ylabel('frequency')
pylab.savefig('plot_B1_histo_r_d%i.png' % d)
pylab.show()
