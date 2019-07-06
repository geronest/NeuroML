import numpy as np
import torch

class TestAlg1:
	def __init__(self, args, dm, mm):
		self.args = args
		self.dm = dm
		self.mm = mm
		self.model = None
		self.criterion = torch.nn.MSELoss(reduction = 'sum')
		#self.optimizer = torch.optim.SGD(self.mm.parameters(), lr = 1e-4, momentum = 0.9)
		self.optimizer = None
		self.idx_train = 0

	def init_train(self):
		self.idx_train = 0
		self.model = self.mm.new_model('tn1') ## ??????? -> do I need to pass args for initializing models here? or was it supposed to be done inside ModelManager?
		self.optimizer = torch.optim.SGD(self.model.parameters(), lr = 1e-4, momentum = 0.9)

	'''
	def set_model(self):
		self.model = self.mm.get_model('tn1')
		self.optimizer = torch.optim.SGD(self.model.parameters(), lr = 1e-4, momentum = 0.9)
	'''

	def iter_train(self, x, y):
		y_pred = self.model(x)
		loss = self.criterion(y_pred, y)

		self.optimizer.zero_grad()
		loss.backward()
		self.optimizer.step()

		self.idx_train += 1
		if self.idx_train % 100 == 0:
			print("iteration {}, loss {}".format(self.idx_train, loss.item()))


