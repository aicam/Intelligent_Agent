import numpy as np
import tensorflow as tf

class Agent:


    def __init__(self, max = 100, ans = 62.5):



        # self.Sigma = tf.Variable(np.random.uniform(low=0, high=max), name= 'sigma')
        self.Sigma = np.random.uniform(low=0, high=max)
        self.History = {}
        self.Answer = ans
        self.Min = 0
        self.Max = max
        self.Step = 8
        self.optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

    def generate_guess(self, sigma = None):
        sigma = self.Sigma if sigma is None else sigma
        s = np.random.normal(0, sigma, 2000)
        count, bins = np.histogram(s, 200, density=True)
        return bins[:200], count

    def goal_test(self, bins, count):
        ideal = np.array(1/(self.Answer * np.sqrt(2 * np.pi)) * np.exp( - (bins)**2 / (2 * self.Answer**2)))
        count = np.array(count)
        boundary = int(np.sqrt(self.Sigma))
        return np.mean((count[-boundary + 100:100 + boundary] - ideal[-boundary + 100:100 + boundary])**2)

    def evaluate_sigma(self, sigma):
        bins, count = self.generate_guess(sigma)
        return self.goal_test(bins, count)

    def train(self, social_information = None):
        if social_information != None:
            self.Min = social_information['min'] if social_information['min'] > self.Min else self.Min
            self.Max = social_information['max'] if social_information['max'] < self.Max else self.Max
            self.Sigma = social_information['sigma'] if (self.Max < self.Sigma or
                self.Min > self.Sigma) else self.Sigma
        sigmas = [self.Sigma + self.Step, self.Sigma - self.Step]
        random_index = np.random.choice([0, 1])
        new_sigma = sigmas[random_index] if (sigmas[random_index] < self.Max) and \
                                            (sigmas[random_index] > self.Min) else sigmas[int(not random_index)]
        # print(self.Sigma)
        # print(new_sigma)
        # print(new_sigma, "   ", self.Sigma,
        #       '     ', self.evaluate_sigma(new_sigma) < self.evaluate_sigma(self.Sigma))
        try:
            if int(self.evaluate_sigma(new_sigma)*(10**9)) < int(self.evaluate_sigma(self.Sigma)*(10**9)):
                # print("Found better solution")
                if new_sigma > self.Sigma:
                    self.Min = self.Sigma
                else:
                    self.Max = self.Sigma
                self.Sigma = new_sigma
                self.Step = np.random.uniform(-5, 5)
            else:
                # print("Random assign")
                random_step = np.random.uniform(-1, 1)
                self.Sigma = self.Sigma + random_step if \
                    (self.Sigma + random_step < self.Max) and \
                    (self.Sigma + random_step > self.Min) else \
                    self.Sigma - random_step
        except ValueError:
            pass
        # print()