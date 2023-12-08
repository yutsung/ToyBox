#!/usr/local/bin/python3
"""read and write binary file directory
"""
import os
import subprocess as sbp

import numpy as np


def main():

    data = np.array([4, 2, 3, 7, 1, 9], dtype='f4')
    print( data )
    
    with open('binary_file.bin', 'w+b') as fid:
        fid.write(data.tobytes('C'))
   
    with open('binary_file.bin', 'r+b') as fid:
        fid.seek(4 * 2)        
        data2_str = fid.read(4 * 2)
       
    data2 = np.frombuffer(data2_str, dtype='f4') 
    data2 = data2**2
    
    with open('binary_file.bin', 'r+b') as fid:
        fid.seek(4 * 2)
        fid.write(data2.tobytes('C'))

    data_ans = np.fromfile('binary_file.bin', dtype='f4')
    print( data_ans )

    proc = sbp.Popen(['rm', 'binary_file.bin'])
    proc.communicate()


if __name__ == '__main__':
    main()
