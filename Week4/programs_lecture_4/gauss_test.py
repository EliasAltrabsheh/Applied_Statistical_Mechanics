import random, math

def gauss_test(sigma):
    phi = random.uniform(0.0, 2.0 * math.pi)
    Upsilon = random.uniform(0.0, 1.0)
    #print round(Upsilon,3)
    Psi = - math.log(Upsilon)
    print round(Psi,3)
    r = sigma * math.sqrt(2.0 * Psi)
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return [x, y]

nsamples = 100
for sample in range(nsamples):
    [x, y] = gauss_test(1.0)
    #print x, y
