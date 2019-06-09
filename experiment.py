import os, time, glob, json
import numpy
from lib.plotting import *
from lib.manage_dir import *
from lib.time import *
import configparser

def parse_configs():
    cfparser = configparser.ConfigParser()
    cfparser.read('./config_experiment.ini')

    args = {
            'id_user': cfparser['User']['id_user'],
            'comment_experiment': cfparser['User']['comment_experiment'],
            'dir_data': cfparser['Data']['dir_data'],
            'dir_model': cfparser['Model']['dir_model'],
            'dir_algorithm': cfparser['Model']['dir_algorithm'],
            'dir_results': cfparser['Results']['dir_results'],
            'dir_plots': cfparser['Results']['dir_plots'],
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
        make_dir(args['dir_results'] + res_dirname + "/" + args['dir_plots'])
        return True
    except:
        print("ERROR - make_dirs: failed to make directory {}".format(res_dirname))
        return False


def main():
    print("\n@@@@@ start code @@@@@\n")
    args = parse_configs()
    res_mkdir = make_dirs(args)
    print("\n@@@@@ end code @@@@@\n")

main()
    



    
