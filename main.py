import numpy as np
import matplotlib.pyplot as plt


# Main file of the applet showing a wave packet going through a potential barrier
# This is a bonus part of the PHYS-H2001 course


class Wave:
    def __init__(self):
        self.k = 1
        self.omega = 1
        self.wave = 0

    def wave(self, x, t):
        return np.exp(1j * (k * x - omega * t))



