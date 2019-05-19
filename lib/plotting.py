import matplotlib.pyplot as plt
import glob

def save_plot(self, name, path, print_msg = True):
    list_plots = glob.glob(path + "*.png")
    for n_pl in list_plots:
        if name == n_pl[:-4]:
            if print_msg: print("!!plot name already exists!!")
            split_dup = n_pl.split('_')[-1]
            try:
                num_dup = int(split_dup)
                name = name + "_{}".format(num_dup+1)
            except:
                name = name + "_0"

    str_save = path + name + ".png"
    plt.savefig(str_save)  
    print("plot saved: {}".format(str_save))

def draw_plot(x, y, title = "plot", xlabel = "x axis", ylabel = "y axis", legends = []):

    coef_margin = 0.1

    x_len = np.max(x) - np.min(x)
    y_len = np.max(y) - np.min(y)

    plt.clear()
    plt.title(title)
    plt.axis([np.min(x) - coef_margin * x_len, np.max(x) + coef_margin * x_len, \
            np.min(y) - coef_margin * y_len, np.max(y) + coef_margin * y_len])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x, y)
    plt.show()

class PlotManager:
    def __init__(self, path_save):
        self.path_save = path_save
        self.plots = {}
       
    def add_plot(self, plot, name = "", print_msg = True):
        if name == "":
            if print_msg:
                print("no name given for the plot. automatically assigning")
            num_plots = len(list(self.plots.keys())) 
            name = "plot_{}".format(num_plots)
        else:
            if name in self.plots.keys():
                if print_msg: print("!!plot name already exists!!")
                split_dup = name.split('_')[-1]
                try:
                    num_dup = int(split_dup)
                    name = name + "_{}".format(num_dup+1)
                except:
                    name = name + "_0"

        self.plots[name] = plot
        if print_msg:
            print("plot added as: {}".format(name))

    def get_plot(self, name):
        res = None
        try:
            res = self.plots[name]
        except:
            print("!! no plot with given name {} !!".format(name))
        return res


