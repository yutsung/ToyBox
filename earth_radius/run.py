#!/usr/local/bin/python3
"""
"""
import numpy as np

def earth_radius(lat):
    theta = lat/180 * np.pi
    r_equatorial = 6378.1370
    a = r_equatorial
    r_polar = 6356.7523
    b = r_polar

    r_theta = np.sqrt(
        ((a**2 * np.cos(theta))**2 + (b**2 * np.sin(theta))**2) /
        ((a    * np.cos(theta))**2 + (b    * np.sin(theta))**2)
    )
    return r_theta


if __name__ == '__main__':
    print( earth_radius(23.5) )
    print( earth_radius(60.0) )
