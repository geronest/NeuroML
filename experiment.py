import os, time, glob
import numpy
from lib.plotting import *
import configparser

def parse_configs():
    cfparser = configparser.ConfigParser()
    cfparser.read('./config_experiment.ini')

    args = {
            'id_user' = cfparser['User']['id_user'],
            'dir_data' = cfparser['Data']['dir_data'],
            'dir_model' = cfparser['Model']['dir_model'],
            'dir_results' = cfparser['Results']['dir_results']
            }

    return args
    
def make_dirs(args):
	

path_results = "test"
if os.path.exists(path_results):
    os.makedirs(path_results)


    
