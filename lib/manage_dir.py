import os

def make_dir(path):
    if not os.path.exists(path):
        print("make_dir: path {} does NOT exist. making one".format(path))
        os.makedirs(path)

def check_dir(path):
    if not os.path.exists(path):
        print("ERROR - check_dir: path {} does NOT exist!".format(path))
        return False

    return True
