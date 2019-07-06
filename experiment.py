import os, time, glob, json, shutil
import numpy as np
from lib.plotting import *
from lib.time import *
from lib.manage_dir import *
from lib.manage_name import *

from data.DataManager import *
from model.ModelManager import *

import configparser

name_config_exp = 'config_experiment.ini'
name_config_data = 'config_data.ini'
name_config_model = 'config_model.ini'
name_config_algorithm = 'config_algorithm.ini'

def parse_configs():
    cfparser = configparser.ConfigParser()
    cfparser.read(name_config_exp)

    args = {
            ### User ###
            'id_user': cfparser['User']['id_user'],
            'comment_experiment': cfparser['User']['comment_experiment'],

            ### Data ###
            'dir_data': cfparser['Data']['dir_data'],
            'type_learning': cfparser['Data']['type_learning'],
            'name_data' : cfparser['Data']['name_data'],

            ### Model ###
            'dir_model': cfparser['Model']['dir_model'],

            ### Algorithm ###
            'dir_algorithm': cfparser['Algorithm']['dir_algorithm'],

            ### Results ###
            'dir_results': cfparser['Results']['dir_results'],
            'res_plots': 'plots/',
            'res_model': 'model/', 
            'res_configs': 'configs/',
            'order_dirname': cfparser['Results']['order_dirname'][1:-1].split(", ")
            }

    # print(args)
    # for k in args.keys():
    #     print ("{} : {}".format(k, args[k]))

    return args
    
def make_dirs(args):
    # assumes directories for data and model are already created.
    # only creates directories for results and plots, if they do not exist.
    check_dir(args['dir_data'])
    check_dir(args['dir_model'])
    check_dir(args['dir_algorithm'])
    
    res_dirname = ""
    res_fullname = get_fulltime()
    order_dirname = ['date', 'time', 'id', 'comment']

    # check if order_dirname was given correctly from .ini file
    if set(args['order_dirname']) == set(order_dirname):
        order_dirname = args['order_dirname']
    else:
        print("ERROR - make_dirs: failed to parse order_dirname {}\nusing default setting {}".format(args['order_dirname'], order_dirname))

    for item in order_dirname:
        if item == 'date': res_dirname += res_fullname[0] + "_"
        if item == 'time': res_dirname += res_fullname[1] + "_"
        if item == 'id': res_dirname += args['id_user'] + "_"
        if item == 'comment': res_dirname += args['comment_experiment'] + "_"

    res_dirname = res_dirname[:-1] # deleting the last "_"
    print("### making directory with name {} ###".format(res_dirname))
	
    try:
        args['dir_results'] += res_dirname + "/"
        make_dir(args['dir_results'] + args['res_plots'])
        make_dir(args['dir_results'] + args['res_model'])
        make_dir(args['dir_results'] + args['res_configs'])
        return True
    except Exception as e:
        print("ERROR - make_dirs: failed to make directory {}".format(res_dirname))
        raise e

def save_configs(args):
    try:
        shutil.copyfile(name_config_exp, manage_file_dup(name_config_exp, dir_configs))
        shutil.copyfile(args['dir_data'] + name_config_data, manage_file_dup(name_config_data, dir_configs))
        shutil.copyfile(args['dir_model'] + name_config_model, manage_file_dup(name_config_model, dir_configs))
        shutil.copyfile(args['dir_algorithm'] + name_config_algorithm, manage_file_dup(name_config_algorithm, dir_configs))
    except Exception as e:
        raise e

def load_data(args):
    dm = DataManager(args['type_learning'], args['name_data'])

    if args['type_learning'][:2] == 'RL':
        return dm.get_env()
    elif args['type_learning'][:2] == 'SL':
        return dm

def load_model(args):
    mm = ModelManager(args) # ModelManager
    return mm

def execute_algorithm(args, dm, mm):
    return False

def main():
    print("\n@@@@@ experiment.py: start code @@@@@\n")

    tm = TimeManager()
    tm.start('experiment_whole')

    args = parse_configs()

    assert make_dirs(args)
    save_configs(args)

    tm.start('load_data')
    dm = load_data(args)
    tm.check('load_data')

    tm.start('load_model')
    mm = load_model(args)
    tm.check('load_model')

    tm.start('execute_algorithm')
    res_alg = execute_algorithm(args, dm, mm)
    tm.check('execute_algorithm')

    tm.check('experiment_whole')

    print("\n@@@@@ experiment.py: end code @@@@@\n")
    print(tm.get_stat_whole())

main()
    



    
