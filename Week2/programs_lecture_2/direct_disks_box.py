import random, math

N = 4  # number of boxes
sigma = 0.1 # initail step
condition = False
while condition == False:
    L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
    for k in range(1, N):
        a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
        min_dist = min(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L)
        if min_dist < 2.0 * sigma:
            condition = False
            break
        else:
            L.append(a)
            condition = True
print L
