import numpy as np
from Wave import Wave
from Packet import Packet

# Main file of the applet showing a wave packet going through a potential barrier
# This is a bonus part of the PHYS-H2001 course

x_lim = 20
a = 0.10  # Width of the barrier
x = np.linspace(-x_lim, x_lim + a, 500)


def gaussian(x, mean, deviation):
    a = 1/(deviation*np.sqrt(2*np.pi))
    b = (((x - mean)/deviation)**2)/2
    return a*np.exp(-b)


firstWave = Wave()




