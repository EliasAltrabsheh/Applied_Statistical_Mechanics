import random, math,pylab,os




filename = 'disk_configuration_N16_eta0.72.txt'
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    L = []
    for k in range(16):
        L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
    print 'starting from a new random configuration'

L[0][0] = 3.3
f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()





def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)


def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 1):
            for iy in range(-1, 1):
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()





sigma = 0.30
sigma_sq = sigma ** 2
delta = 0.1
N = 4
N_sqrt = N **2
eta = N *(math.pi *sigma_sq )
radius = math.sqrt(eta/math.pi)
print eta,radius

delxy = sigma
two_delxy = sigma_sq 
n_steps = 100000
for steps in range(n_steps):
    a =  [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)] # Modify cooridates
    min_dist = min(dist(b,c) for c in L if c != a)
    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if not (box_cond or min_dist < 4.0 * sigma **2):  ## test for overlaps
        a[:] = b
print L
show_conf(L, sigma, 'test graph', 'B3_image.png')
