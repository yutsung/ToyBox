"""
"""
import numpy as np
import multiprocessing as mtp
 
def multiply(x1, x2):
    return x1 * x2
 
def main():
    x1 = np.arange(5)
    x2 = np.array([1, 2, 3, 0, 9])
    p = mtp.Pool(2)
    p_out = p.starmap(multiply, zip(x1, x2))
    print(p_out)
 
if __name__ == "__main__":
    main()
