import random,math

def Markov_Pi(delta):
    x, y = 1.0, 1.0 # x and y represent the square sides ( x axis and y axis)
    delta = 0.1  # delta is the random displacment ( this can be variable)
    n_trials = 2**12
    n_hits = 0
    n_acceptance = 0
    for i in range(n_trials):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            n_acceptance +=1
        if x**2 + y**2 < 1.0: n_hits += 1
    obs_pi= 4.0 * n_hits / float(n_trials)
    return n_hits, n_acceptance,n_trials,obs_pi


deltas = [0.062,0.125,0.25,0.50,1.00,2.00,4.00]
print "delta | hits | acceptance | number of trail | accceptance rate | observed Pi"
for i in deltas:
    temp = Markov_Pi(i)
    print i ," | ", temp[0], " | " , temp[1], " | ", temp[2]," | ", round(float(temp[1])/float(temp[2]),4), " | ", round(temp[3],4)
