"""
"""
import numpy as np
import multiprocessing as mtp
 
def power3(data):
    return data**3
 
def main():
    x = np.arange(50)
    p = mtp.Pool(3)
    p_out = p.map(power3, x)
    print(p_out)
 
if __name__ == "__main__":
    main()
