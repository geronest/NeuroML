import torch

class Model(torch.nn.Module):
	def __init__(self, args):
		assert len(args['dims'])>3
		super(Model, self).__init__()

		self.layers = list()
		self.afuncs = list() # activation function (result)s

		for i in range(len(args['dims'])-1):
			self.layers.append(torch.nn.Linear(args['dims'][i], args['dims'][i+1]))
		self.layer_input = self.layers[0]
		self.layer_output = self.layers[-1]


	# Asssumes use of ReLU
	def forward(self, x):
		for i in range(len(self.layers)-1):
			if i == 0:
				self.afuncs.append(self.layers[i](x).clamp(min=0))
			else:
				self.afuncs.append(self.layers[i](self.afuncs[-1]).clamp(min=0))

		y_pred = self.layers[-1](self.afuncs[-1])

		return y_pred

