import time
from multiprocessing import Pool
from PIL import Image
import array

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193


def calculate_z(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output


def calc_mandelbrot_set(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex parameters (cs), build Mandelbrot set"""
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []
    ycoord = y2
    while ycoord < y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs = [complex(xcoord, ycoord) for ycoord in y for xcoord in x]
    cs = [complex(c_real, c_imag)] * len(zs)

    print("x:", len(x))
    print("Total:", len(zs))
    start_time = time.time()

    # Use multiprocessing for parallel computation
    with Pool() as p:
        output = p.starmap(calculate_z, [(max_iterations, [z], [c]) for z, c in zip(zs, cs)])

    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z.__name__ + " took", secs, "seconds")


if __name__ == "__main__":
    calc_mandelbrot_set(desired_width=1000, max_iterations=300)
