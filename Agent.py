import numpy as np
import tensorflow as tf

class Agent:


    def __init__(self, max, ans):



        self.Sigma = tf.Variable(np.random.uniform(low=0, high=max), name= 'sigma')
        self.History = {}
        self.Answer = ans
        self.Min = 0
        self.Max = max
        self.Step = 0.5
        self.optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

    def generate_guess(self):
        s = np.random.normal(0, self.Sigma.value(), 2000)
        count, bins = np.histogram(s, 1000, density=True)
        return bins, count

    def goal_test(self, bins, count):
        ideal = 1/(self.Answer * np.sqrt(2 * np.pi)) * np.exp( - (bins)**2 / (2 * self.Answer**2))
        return np.var(count - ideal)

    def train(self, social_information):
        self.Min = social_information['min'] if social_information['min'] > self.Min else self.Min
        self.Max = social_information['max'] if social_information['max'] < self.Max else self.Max
