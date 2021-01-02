from Agent import Agent
import numpy as np

class CrowdWisdom:
    def __init__(self, initial_population = 1000, random_count = 200):
        self.initial_population = initial_population
        self.random_count = random_count
        self.agents = np.array([Agent() for _ in range(initial_population)])

    def optimize(self, epoch = 20):
        indices = np.arange(self.initial_population)
        for i in range(epoch):
            np.random.shuffle(indices)
            step_size = int(self.initial_population / self.random_count)
            for j in range(step_size):
                group = self.agents[j*self.random_count:(j + 1)*self.random_count]
                max_fitness = sorted(group, key= lambda x: x.Max - x.Min, reverse=True)
                social_information = {'min': max_fitness[0].Min, 'max': max_fitness[0].Max,
                                      'sigma': max_fitness[0].Sigma}
                for k in range(self.random_count):
                    for _ in range(10):
                        group[k].train(social_information)
