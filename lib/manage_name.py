import glob

def manage_file_dup(name, dst): # name contains path to the file
    name = name.split('/')[-1]
    split_name = name.split('.')
    ext_name = split_name[-1]
    name_file = split_name[-2]
    
    res_glob = glob.glob(dst + name_file + "*." + ext_name)

    return dst + name_file + str(len(res_glob)) + "." + ext_name

class NameManager:
    def __init__(self):
        self.dict_name = {}

    def chk_name(self, name):
        if name in self.dict_name.keys():
            self.dict_name[name] += 1
        else:
            self.dict_name[name] = 0
        return self.dict_name[name]

            
        
