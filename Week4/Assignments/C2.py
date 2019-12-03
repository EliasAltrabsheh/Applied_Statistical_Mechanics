import random, math

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)
n_trials = 1
n_runs = 25
d_max = 19
delta = 0.1
while n_trials < 10000000:
    tot_vol = 0.0
    tot_vol_sq = 0.0
    for run in range(n_runs):
        vol = 2.0
        for d in range(1, d_max + 1):
            x = [0.0] * d
            old_radius_square = 0.0
            n_hits = 0
            for i in range(n_trials):
                k = random.randint(0, d - 1)
                x_old_k = x[k]
                x_new_k = x_old_k + random.uniform(-delta, delta)
                new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
                if new_radius_square < 1.0:
                    x[k] = x_new_k
                    old_radius_square = new_radius_square
                if old_radius_square + random.uniform(-1.0, 1.0) ** 2 < 1.0:
                    n_hits += 1
            vol *= (2.0 * n_hits / float(n_trials))
        tot_vol += vol
        tot_vol_sq += vol ** 2
    av_vol = tot_vol / float(n_runs)
    av_vol_sq = tot_vol_sq / float(n_runs)
    error = math.sqrt((av_vol_sq - av_vol ** 2) / float(n_runs))
    diff = av_vol - V_sph(d_max + 1)
    print '%10i\t%14g\t%14g\t%14g\t%14g' % (n_trials, av_vol, V_sph(d_max + 1), error, diff)
    n_trials *= 10
