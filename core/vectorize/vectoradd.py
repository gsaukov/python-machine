import numpy as np
import numba
from timeit import default_timer as timer
from numba import vectorize

@vectorize(["float32(float32, float32)"], target = 'cuda')
def VectorAdd(a, b):
    return a + b

def main():
    N = 32000000
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)

    start = timer()
    C = VectorAdd(A, B)
    vectoradd_time = timer() - start

    print("C[:5] = " + str(C[:5]))
    print("C[-5:] = " + str(C[-5:]))

    print("Vector took %f seconds" % vectoradd_time)
    numba.cuda.profile_stop()

if __name__ == '__main__':
    main()

