import numpy as np
from Agent import Agent

a = Agent(100, 50)

bins, count = a.generate_guess()

a.record_history(a.goal_test(bins[:1000], count), 1)
a.train()