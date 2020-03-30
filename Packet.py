from Wave import Wave
import numpy as np


class Packet:
    def __init__(self, x, t):
        self.complexValue = np.array(Wave().wave_func(x, t))

    def add_wave(self, wave_to_add, x, t):
        self.complexValue += wave_to_add.wave_func(x, t)
        return
