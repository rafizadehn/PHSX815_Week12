import sys
import numpy as np
import matplotlib.pyplot as plt

def true_density(x):
        return np.exp(-x**2/2) / np.sqrt(2*np.pi)

def gaussian_kernel(x, x_i, h):
        return np.exp(-(x - x_i)**2 / (2*h**2)) / np.sqrt(2*np.pi) / h
 
def kernel_density_estimation(x, data, h):
    n = len(data)
    density_estimate = np.zeros_like(x)
    for i in range(n):
        density_estimate += gaussian_kernel(x, data[i], h)
    density_estimate /= n*h
    return density_estimate

if __name__ == "__main__":

    # read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
    
    # default values
    seed = 555
    Nexp = 100

    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = int(sys.argv[p+1])
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Nexp = int(sys.argv[p+1])
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed] change seed value" % sys.argv[0])
        print
        sys.exit(1)

    np.random.seed(seed)

    data = np.random.normal(0, 1, Nexp)
    x_min = -3
    x_max = 3
    x = np.linspace(x_min, x_max, 500)
    bandwidth = 0.5
    density_estimate = kernel_density_estimation(x, data, bandwidth)

    fig, ax = plt.subplots()
    ax.plot(x, true_density(x), label='True Density')
    ax.hist(data, bins=20, density=True, alpha=0.5, label='Generated Data')
    ax.plot(x, density_estimate, label='Estimated Density')
    ax.legend()
    ax.set_xlim([x_min, x_max])
    ax.set_xlabel('x')
    ax.set_ylabel('Density')
    plt.show()

