import numpy as np

def mean(value):
    i = 0
    value_m = []
    t_m = []
    while i < 50:
        i += 1
        time = i * 100
        value_raw = sum(value[(time - 100):time]) / 100
        value_m.append(value_raw)
        t_m.append(time)
    value_m = np.array(value_m)
    t_m = np.array(t_m)
    return t_m, value_m
