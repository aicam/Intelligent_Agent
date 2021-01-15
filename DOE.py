import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys



total_count = 1000
attributes_shape = [3, total_count]
attributes_p = [.8, .3, .5]


condition_p = [.5, .5, .5]
def generate_random_attribute(p, shape):
    attributes = np.zeros(shape)
    for i in range(attributes.shape[0]):
        attributes[i] = np.array([0 if t > p[i] else 1 for t in np.random.rand(attributes.shape[1])])
    return attributes.astype(np.int)

def generate_estimation(attr, cond):
    time_estimation = len(attr)
    random_attr = []
    for i in range(len(attr)):
        random_attr.append(np.random.uniform(-1, 0) if attr[i] == (i%3 == 0)
            else np.random.uniform(0, 1))
        time_estimation += random_attr[i]*cond[i]
    return int(time_estimation*1000), np.round(random_attr, 2)

def random_mask(attr):
    return [a if np.random.uniform(0, 1) < .9 else 'NaN' for a in attr]

attribute_columns = ['attribute_' + str(i) for i in range(attributes_shape[0])]
df = pd.DataFrame(columns=['user_id', 'spent_ms', 'is_clicked'] + attribute_columns + ['condition'])
attributes = generate_random_attribute(attributes_p, attributes_shape)
conditions = generate_random_attribute(condition_p, attributes_shape)

for i in range(total_count):
    es_time, random_attr = generate_estimation(attributes[:,i], conditions[:,i])
    df.loc[i] = np.concatenate((np.array([i, es_time,
                          1 if np.random.uniform(0, .8) < (1 - np.e**(- int(es_time/3000))) else 0,
                 ]), random_mask(random_attr), [''.join(conditions[:,i].astype(np.str))]), axis=0)

df.to_csv('DOE.csv')
