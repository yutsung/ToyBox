#!/usr/local/bin/python3
"""
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
   w = [0.3 * 0.7**i for i in range(10)]
   noise = [ 0.89148973,  1.78701912,  1.63780867,  
             0.20044182, -0.84927559, -4.62805211,
            -0.17856421,  0.54981689, -2.20048703,  
             3.67896849]
   x = np.array([0 ,1, 2, 3, 4, 5, 6, 7, 8, 9])
   y = 8.8 + (6.6 * x) + noise
   y[:3]  += 0
   y[3:7] += 5
   y[7:]  += 9

   X = np.asmatrix(np.c_[np.ones(10), x])
   Y = np.asmatrix(y).T
   W = np.identity(10) * w

   B  = (X.T * X).I * X.T * Y
   BW = (X.T * W * X).I * X.T * W * Y

   fig, ax = plt.subplots(figsize=(16, 9))
   line1, = ax.plot(X * B,  '-')
   line2, = ax.plot(X * BW, '-')
   line3, = ax.plot(y,      'ko')
   line1.set_label('LS')
   line2.set_label('weighted LS')
   ax.legend(fontsize=16)
   fig.savefig('weighted_LS.png')


if __name__ == '__main__':
    main()
