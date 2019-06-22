import numpy as np
import torch

class TestAlg1:
	def __init__(self, dm, mm):
		self.dm = dm
		self.mm = mm
		self.criterion = torch.nn.MSELoss(reduction = 'sum')
		self.optimizer = torch.optim.SGD(self.mm.parameters(), lr = 1e-4, momentum = 0.9)
		self.idx_train = 0

	def init_train(self):
		self.idx_train = 0

	def iter_train(self, x, y):
		y_pred = self.mm(x)
		loss = criterion(y_pred, y)

		optimizer.zero_grad()
		loss.backward()
		optimizer.step()

		self.idx_train += 1
		if self.idx_train % 100 == 0:
			print("iteration {}, loss {}".format(self.idx_train, loss.item()))


