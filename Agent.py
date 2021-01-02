import numpy as np
import tensorflow as tf

class Agent:


    def __init__(self, max, ans):



        # self.Sigma = tf.Variable(np.random.uniform(low=0, high=max), name= 'sigma')
        self.Sigma = np.random.uniform(low=0, high=max)
        self.History = {}
        self.Answer = ans
        self.Min = 0
        self.Max = max
        self.Step = 0.5
        self.optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

    def generate_guess(self, sigma = None):
        sigma = self.Sigma if sigma is None else sigma
        s = np.random.normal(0, sigma, 2000)
        count, bins = np.histogram(s, 1000, density=True)
        return bins[:1000], count

    def goal_test(self, bins, count):
        ideal = 1/(self.Answer * np.sqrt(2 * np.pi)) * np.exp( - (bins)**2 / (2 * self.Answer**2))
        return np.var(count - ideal)

    def evaluate_sigma(self, sigma):
        bins, count = self.generate_guess(sigma)
        return self.goal_test(bins, count)

    def train(self, social_information = None):
        if social_information != None:
            self.Min = social_information['min'] if social_information['min'] > self.Min else self.Min
            self.Max = social_information['max'] if social_information['max'] < self.Max else self.Max
            self.Sigma = social_information['sigma'] if (social_information['max'] < self.Sigma or
                social_information['min'] > self.Sigma) else self.Sigma
        new_sigma = self.Sigma + self.Step if \
            self.Sigma + self.Step < self.Max else \
            self.Sigma - self.Step
        if self.evaluate_sigma(new_sigma) < self.evaluate_sigma(self.Sigma):
            if new_sigma > self.Sigma:
                self.Min = self.Sigma
            else:
                self.Max = self.Sigma
            self.Sigma = new_sigma
            self.Step = np.random.uniform(-1, 1)
        else:
            random_step = np.random.uniform(-1, 1)
            self.Sigma = self.Sigma + random_step if \
                (self.Sigma + random_step < self.Max) and \
                (self.Sigma + random_step > self.Min) else \
                self.Sigma - random_step