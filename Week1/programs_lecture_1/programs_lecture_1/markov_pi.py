import random



x, y = 1.0, 1.0 # x and y represent the square sides ( x axis and y axis)
delta = 0.1  # delta is the random displacment ( this can be variable)
n_trials = 4000
n_hits = 0
for i in range(n_trials):
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
        x, y = x + del_x, y + del_y
    if x**2 + y**2 < 1.0: n_hits += 1
print 4.0 * n_hits / float(n_trials)
