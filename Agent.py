import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self,max):



        self.Sigma = np.random.uniform(low=0, high=max)
        self.History = []

    def generate_guess(self):
        s = np.random.normal(0, self.Sigma, 2000)
        count, bins = np.histogram(s, 1000, density=True)
        return bins, count

    def goal_test(self, ans, bins, count):
        ideal = 1/(ans * np.sqrt(2 * np.pi)) * np.exp( - (bins)**2 / (2 * ans**2))
        return np.var(count - ideal)

    def record_history(self, fitness, iteration):
        self.History.append({'Fitness': fitness, 'Iteration': iteration, 'sigma': self.Sigma})

