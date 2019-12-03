import random

x, y ,z,alpha= 0.0, 0.0,0.0,0.0 # x and y represent the square sides (x axis and y axis)
delta = 1 # delta is the random displacment (this can be variable)
n_trials = 1000000
n_hits = 0
for i in range(n_trials):
    del_x, del_y ,del_z,del_alpha = random.uniform(-delta,delta), random.uniform(-delta, delta),random.uniform(-1, 1),random.uniform(-1, 1)
    if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0 and abs(z + del_z) < 1.0 :
        x, y, z = x + del_x, y + del_y, z + del_z,
    if x**2 + y**2 + z**2  + alpha**2 < 1.0: n_hits += 1
print 2 * n_hits / float(n_trials)
