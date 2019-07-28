'''
TODO
	1) Constructing models via simple settings
	2) *** MODEL SAVE & LOAD !!! ***
	3) resuming training?
'''

import model.testnn1.testnn1 as tn1
import configparser

import lib.manage_dir as md
from lib.manage_args import *
import os
import torch

mdict = { # model dict?
			'testnn1': tn1.Model
		}

name_config_model = './model/config_model.ini'


def parse_configs(name):
    cfparser = configparser.ConfigParser()
    cfparser.read(name_config_model)

    args = dict()
    for key in cfparser[name]:
    	args[key] = cfparser[name][key]
    split_dims = args['dims'][1:-1].split(",")
    args['dims'] = list()
    for dim in split_dims: args['dims'].append(int(dim))

    return args


class ModelManager:
	def __init__(self, args_exp): # args got from experiment.py
		self.models = dict()
		self.dir_model = args_exp['dir_results'] + args_exp['res_model']
		self.dirs = dict()
		self.args_mm = parse_configs(args_exp['name_model'])

	def new_model(self, name, args_mdefine = {}):
		args_m = overwrite_args(self.args_mm, args_mdefine)
		if name not in self.models.keys():
			self.models[name] = list()
			self.dirs[name] = self.dir_model + name + '/'
		self.models[name].append(mdict[name](args_m))

		return self.models[name][-1]

	def get_model(self, name, idx = 0):
		return self.models[name][idx]

	def save_model(self, name, idx = 0, path = ""):
		md.make_dir(self.dirs[name] + path)
		torch.save(self.models[name][idx].state_dict(), self.dirs[name] + path)

	def load_model(self, name, idx = 0, path = "", args_mdefine = {}):
		args_m = overwrite_args(self.args_mm, args_mdefine)
		self.models[name][idx] = mdict[name](args_m)
		self.models[name][idx].load_state_dict(torch.load(path))
		self.models[name][idx].eval()

	def resume_training(self):
		pass #???
