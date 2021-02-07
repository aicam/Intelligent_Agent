import numpy as np
import pandas as pd

conditions_constraints = [[3, [0, 1, 0]], [2, [1, 0, 1]]]

attributes_p = [.8, .3, .5]


def generate_conditions(c):
    t = 0
    for condition in c:
        t += condition[0]
    total_count = t
    a_s = [3, total_count]
    attributes = np.zeros(a_s)
    for i in range(3):
        con_raw = []
        for con in c:
            con_raw += [con[1][i]]*con[0]
        attributes[i] = np.array(con_raw)
    return attributes.astype(np.int), a_s

conditions, attributes_shape = generate_conditions(conditions_constraints)
total_count = attributes_shape[1]
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

def convert_to_meaningfulString(attr):
    new_a = ['', '', '']
    new_a[0] = 'M' if attr[0] == 0 else 'F'
    new_a[1] = int(np.random.uniform(30,50)) if attr[1] == 0 else int(np.random.uniform(50,70))
    new_a[2] = 'High' if attr[2] == 0 else 'Low'
    return new_a

attribute_columns = ['gender', 'age', 'education']#['attribute_' + str(i) for i in range(attributes_shape[0])]
df = pd.DataFrame(columns=['user_id', 'spent_ms', 'is_clicked'] + attribute_columns + ['condition'])
attributes = generate_random_attribute(attributes_p, attributes_shape)


for i in range(total_count):
    es_time, random_attr = generate_estimation(attributes[:,i], conditions[:,i])
    df.loc[i] = np.concatenate((np.array([i, es_time,
                          1 if np.random.uniform(0, .8) < (1 - np.e**(- int(es_time/3000))) else 0,
                 ]), random_mask(convert_to_meaningfulString(attributes[:, i])),
                                [''.join(conditions[:,i].astype(np.str))]), axis=0)

df.to_csv('DOE.csv')
