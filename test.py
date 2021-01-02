import numpy as np
from Agent import Agent

a = Agent(100, 50)

bins, count = a.generate_guess()

a.train()

