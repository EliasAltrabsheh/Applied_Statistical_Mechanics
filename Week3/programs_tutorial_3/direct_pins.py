import random

N = 15
L = 10.0
sigma = 0.1
n_configs = 100
rejected = 0
for config in range(n_configs):
    x = []
    while len(x) < N:
        x.append(random.uniform(sigma, L - sigma))
        for k in range(len(x) - 1):
            if abs(x[-1] - x[k]) < 2.0 * sigma:
                x = []
                rejected += 1
                break
    my_rounded_list = [ round(elem, 2) for elem in x ]
    print "number of tabula rasa before config was preduces = {}".format(rejected)
    print    my_rounded_list
