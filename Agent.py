import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self,max):



        self.Sigma = np.random.uniform(low=0, high=max)
        self.History = []

    def generate_guess(self):
        s = np.random.normal(0, self.Sigma, 2000)
        _, bins = np.histogram(s, 300, density=True)
        return bins, 1/(self.Sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins)**2 / (2 * self.Sigma**2))
