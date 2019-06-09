import numpy as np
import random

class ReplayBuffer:
    def __init__(self, names, config):
        self.idx = 0
        self.len = 0
        self.max_len = config['max_len']
        self.data = {}
        for name in names:
            self.data[name] = np.zeros(config["shape_{}".format(name)])

    def add(self, data_new):
        for name in data_new.keys():
            self.data[name][self.idx] = data_new[name]

        self.idx = (self.idx + 1) % self.max_len
        self.len = min(self.len + 1, self.max_len)

    def sample(self, length = 1):
        res = {}
        idx = np.random.randint(0, self.len, length)
        for key in self.data.keys():
            res[key] = self.data[key][idx]
        
        return res

