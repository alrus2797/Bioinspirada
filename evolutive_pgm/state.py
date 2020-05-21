import numpy as np
from utils import ep_utils as ep
class State:
	def __init__(self, name, inputs, outputs, neighbours, status, alphabet):
		self.name       = name
		self.inputs     = np.array(inputs)
		self.outputs    = np.array(outputs)
		self.neighbours	= np.array(neighbours)
		self.status     = status
		self.alphabet   = np.array(alphabet)

	def is_valid(self):
		return self.status

	def get_status(self):
		return self.status

	def set_neighbours(self, neighbours):
		self.neighbours = neighbours

	def find_neighbour(self, req_neighbour):
		return np.where(self.neighbours == req_neighbour)[0]

	def make_initial(self):
		self.status = 2

	def execute(self, char, verbose = False):
		pos = np.where(self.inputs == char)[0][0]
		if verbose: print(self.name, pos, pos[0][0], self.inputs, char)
		if not self.neighbours[pos].is_valid(): raise BaseException('Transition to a unactive state')
		return self.outputs[pos], self.neighbours[pos]

	def deactivate(self):
		self.status = 0

	def mut_inputs(self):
		self.inputs = self.inputs[::-1]

	def mut_outputs(self, pos):
		self.outputs[pos] = not self.outputs[pos]

	def mut_neightbor(self, state, pos):
		self.neighbours[pos] = state

	def activate(self):
		self.status = 1

	def __str__(self):
		return f'{self.status}{"".join(map(str, self.inputs))}{"".join(map(str, self.outputs))}{"".join(map(lambda x: x.name.title(), self.neighbours))}'

	def __repr__(self):
		return str(self)
	
	def __eq__(self, other):
		return self.name == other.name