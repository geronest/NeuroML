'''
TODO
	
'''

import model.testalg1.testalg1 as ta1

import lib.manage_dir as md
from lib.manage_args import *
import os
import torch

adict = { # algorithm dict?
			'ta1' = ta1.Algorithm
		}

name_config_alg = './algorithm/config_algorithm.ini'


def parse_configs():
    cfparser = configparser.ConfigParser()
    cfparser.read(name_config_alg)

    args = {
            # TODO: fill!
            }

    return args


class AlgorithmManager:
	def __init__(self, args_alg, dm, mm): # args got from experiment.py
		self.dm = dm
		self.mm = mm
		self.algs = dict()
		self.dir_alg = args_alg['dir_results'] + args_alg['res_algorithm']
		self.dirs = dict()
		self.args_am = parse_configs()

	def new_algorithm(self, name, args_adefine = {}):
		args_a = overwrite_args(self.args_am, args_adefine)
		if name not in self.algs.keys():
			self.algs[name] = list()
			self.dirs[name] = self.dir_alg + name + '/'
		self.algs[name].append(adict[name](args_a, self.dirs[name], self.dm, self.mm))
		self.algs[name][-1].init_train()

		return self.algs[name][-1]

	def get_algorithm(self, name, idx = 0):
		return self.algs[name][idx]

	def save_algorithm(self, name, idx = 0, path = ""):
		md.make_dir(self.dirs[name] + path)
		# TODO: save what? model??

	def load_algorithm(self, name, idx = 0, path = "", args_adefine = {}):
		args_a = overwrite_args(self.args_am, args_adefine)
		# TODO: load what? model??

	def run_algorithm(self, name, idx):
		alg = self.algs[name][idx]
		alg.run_train()

	def resume_training(self):
		pass #???
