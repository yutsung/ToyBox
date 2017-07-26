"""
"""
import numpy as np
import multiprocessing as mtp
 
def multiply(param):
    x1, x2 = param
    return x1 * x2
 
def main():
    x1 = np.arange(20)
    x2 = np.arange(20)
    p = mtp.Pool(3)
    p_out = p.map(multiply, zip(x1, x2))
    print(p_out)
 
if __name__ == "__main__":
    main()
