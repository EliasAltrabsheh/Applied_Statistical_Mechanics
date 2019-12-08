import random, math,pylab

x = 0.0
delta = 0.5


def psi_0_sq(x):

    return (1/math.pi**0.25) * math.exp(-x**2)

data = []

for k in range(1000):
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) <  \
         psi_0_sq(x_new)**2/psi_0_sq(x)**2 :
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
