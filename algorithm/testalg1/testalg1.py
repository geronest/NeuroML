import numpy as np
import torch
import libs.manage_name as mn

class Algorithm:
	def __init__(self, args, dir_alg, dm, mm):
		self.dir_alg = dir_alg
		self.args = args
		self.dm = dm
		self.mm = mm

		self.model = None
		self.criterion = torch.nn.MSELoss(reduction = 'sum')
		#self.optimizer = torch.optim.SGD(self.mm.parameters(), lr = 1e-4, momentum = 0.9)
		self.optimizer = None
		self.idx_train = 0

		self.file_log = open(manage_file_dup('log_algorithm.txt', self.dir_alg), "a")

	def report(self, s):
		print(s)
		self.file_log.write(s)

	def init_train(self):
		self.idx_train = 0
		self.model = self.mm.new_model('tn1') ## TODO: needs to pass dimensions according to input and output of data!!
		self.optimizer = torch.optim.SGD(self.model.parameters(), lr = 1e-4, momentum = 0.9)
		self.report("init_train complete")

	'''
	def set_model(self):
		self.model = self.mm.get_model('tn1')
		self.optimizer = torch.optim.SGD(self.model.parameters(), lr = 1e-4, momentum = 0.9)
	'''
	def get_idx_train(self):
		return self.idx_train

	def iter_train(self, x, y):
		y_pred = self.model(x)
		loss = self.criterion(y_pred, y)

		self.optimizer.zero_grad()
		loss.backward()
		self.optimizer.step()

		self.idx_train += 1
		if self.idx_train % 100 == 0:
			self.report("iteration {}, loss {}".format(self.idx_train, loss.item()))

	def run_train(self, idx_terminate = 10000):
		# TODO: implement!!
		pass
		


