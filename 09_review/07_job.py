from joblib import Parallel, delayed
from math import sqrt

#sq1 = [sqrt(i ** 2) for i in range(10000000)]
sq2 = Parallel(n_jobs=-1)(delayed(sqrt)(i ** 2) for i in range(10000000))
