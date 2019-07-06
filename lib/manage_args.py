

def overwrite_args(args_orig, args_new):
	res = args_orig.copy()
	for k in args_new.keys():
		res[k] = args_new[k]
	return res
