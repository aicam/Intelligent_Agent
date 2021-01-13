import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys



total_count = 1000
attributes_shape = [3, total_count]
attributes_p = [.8, .3, .5]

def generate_random_attribute(p, shape):
    attributes = np.zeros(shape)
    for i in range(attributes.shape[0]):
        attributes[i] = np.array([0 if t > p[i] else 1 for t in np.random.rand(attributes.shape[1])])
    return attributes

def generate_estimation(attr):
    time_estimation = len(attr) + 1
    for i in range(len(attr)):
        time_estimation += np.random.uniform(-1, 0) if attr[i] == (i%3 == 0) else np.random.uniform(0, 1)
    time_estimation += np.random.uniform(-1, 1)
    return int(time_estimation*1000)

df = pd.DataFrame(columns=['user_id', 'spent_ms', 'is_clicked', 'conditions'])
attributes = generate_random_attribute(attributes_p, attributes_shape)

for i in range(total_count):
    es_time = generate_estimation(attributes[:,i])
    df.loc[i] = [i,
                 es_time,
                 1 if np.random.uniform(0, 1) < (1 - np.e**es_time) else 0,
                 ]
