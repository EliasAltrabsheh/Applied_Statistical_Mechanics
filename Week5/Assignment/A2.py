import random, math,pylab

x = 0.0
delta = 0.5

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

def psi_0_sq(x):

    return (1/math.pi**0.25) * math.exp(-x**2)

data = []

for k in range(1000):
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) <  \
        min(1,psi_n_square(x_new)/psi_n_square(x_new)**2) :
        x = x_new
    #print x
    data.append(x)



    pylab.hist(data,  normed='True')
    pylab.xlabel('$x$', fontsize=16)
    pylab.ylabel('$\pi(x)$', fontsize=16)
    x = [a  for a in xrange(0, 1)]
    y = [a  for a in data]
    pylab.plot(x, y, linewidth=1.5, color='r')
    pylab.title(' normalized\
        \n histogram for '+str(len(data))+' samples',fontsize=16)

    pylab.show()
