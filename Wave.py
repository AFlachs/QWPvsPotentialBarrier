import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cst  # for physical constants, type help(cst) for details


class Wave:
    def __init__(self):
        """ Constructor for waves """
        self.k = 1
        self.omega = 1
        self.z = []

    def coefficients(self, V_0, E, a):
        """
        Computes the transmission, reflexion... coefficient of the wave
        :param a: width of the barrier
        :param V_0: flt, height of the barrier
        :param E: flt, energy of the electron
        :return:
        """
        h2m = cst.hbar ** 2 / 2 / cst.m_e / cst.e * 1e18
        if V_0 == 0:
            K = self.k
            T = 1
            R = 0
            A = 1
            B = 0

        elif E < V_0:
            K = np.sqrt((V_0 - E) / h2m)
            T = np.exp(-1j * self.k * a) * 2 * self.k * K / (2 * self.k * K * np.cosh(K * a) + 1j * (K ** 2 - self.k ** 2) * np.sinh(K * a))
            R = -1j * T * np.exp(1j * self.k * a) * (self.k ** 2 + K ** 2) * np.sinh(K * a) / (2 * self.k * K)
            A = 1j * self.k * (1 - R) / K
            B = 1 + R

        elif E == V_0:
            T = np.exp(-1j * self.k * a) * 2 * self.k / (2 * self.k - 1j * self.k ** 2 * a)
            R = -1j * T * np.exp(1j * self.k * a) * self.k ** 2 * a / 2 / self.k
            A = 1j * self.k * (1 - R)
            B = 1 + R
            K = self.k

        else:
            K = np.sqrt((E - V_0) / h2m)
            K2 = K / self.k
            v1 = np.exp(1j * K * a) / np.exp(1j * self.k * a)
            v2 = np.exp(-1j * K * a) / np.exp(1j * self.k * a)
            A = -2 * v2 * (1 + K2) / (v1 * (1 - K2) ** 2 - v2 * (1 + K2) ** 2)
            B = (2 - A * (1 + K2)) / (1 - K2)
            R = A + B - 1
            T = A * v1 + B * v2
        return A, B, T, R, K

    def format_for_plot(self, x, t, V_0, E, a):
        """
        This function returns the value of one specific electron wave between
        :param x: np array of any size
        :param t: flt, scalar value
        :return: np array representing the complex wave function of the electron
        """
        A, B, T, R, K = self.coefficients(V_0, E, a)
        for v in x:
            if v < 0:
                self.z.append(np.exp(1j * self.k * v) + R * np.exp(-1j * self.k * v))
            elif 0 < v < a:
                if E < V_0:
                    self.z.append(A * np.sinh(K * v) + B * np.cosh(K * v))
                elif E == V_0:
                    self.z.append(A * v + B)
                else:
                    self.z.append(A * np.exp(1j * K * v) + B * np.exp(-1j * K * v))
            else:
                self.z.append(T * np.exp(1j * self.k * v))

        return self.z

    def normalize(self):

        return self.z