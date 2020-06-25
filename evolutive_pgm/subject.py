import numpy as np
from evolutive_pgm.state import State
from utils import ep_utils as ep
from graphviz import Digraph
import copy


class Subject():
	def __init__(self, n_states, alphabet, predict_string):
		self.n_states   = n_states
		self.alphabet   = alphabet.copy()
		self.states     = []
		self.status     = [0, 1, 2]
		self.initial    = None
		self.graph      = Digraph(comment = 'Subject', format='png')
		self.alphabet_length	= len(alphabet)
		self.predict_string		= predict_string


		for i in range(n_states):
			current_status = ep.choice(self.status)
			new_state = State(chr(i+65), ep.shuffle(alphabet), ep.choice(alphabet, self.alphabet_length), [], current_status, self.alphabet)
			if current_status == 2:
				self.initial = new_state
				self.status.pop()
			self.states.append(new_state)
		if 2 in self.status:
			self.states[0].status   = 2
			self.initial            = self.states[0]
		for state in self.states:
			state.set_neighbours(ep.choice(self.get_active_states(), self.alphabet_length))
		if not self.initial:
			raise BaseException('For some reason initial state does not exist')

	def get_active_states(self):
		return [state for state in self.states if state.is_valid()]

	def copy(self):
		return copy.deepcopy(self)


	def get_fitness(self):
		string = self.predict_string
		current_state   = self.initial
		fitness         = 0
		output_str		= ''
		for idx, char in enumerate(string):
			output, next_neighbour = current_state.execute(int(char))
			output_str	+= str(output)
			current_state	= next_neighbour
			if idx + 1 < len(string):
				if int(string[idx + 1]) == output:
					fitness += 1
		return output_str, fitness/len(string)

	def mutate(self):
		random_number   = np.random.rand()
		picked_state    = ep.choice(self.states)
		print('Before: ', self)
		print('Rand Number: ', random_number)

		if 0 < random_number <= .1:
			print('Desactivar estado')
			if picked_state.status == 2:
				print('- No se desactiva por ser estado inicial')
			else:
				picked_state.deactivate()
				for state in self.states:
					unactive_neighbour_idx = state.find_neighbour(picked_state)
					state_choosed = ep.choice(self.get_active_states())
					state.mut_neightbor(state_choosed, unactive_neighbour_idx)
		elif .1 < random_number <= .3:
			print('Cambiar de estado inicial')
			self.initial.activate()
			picked_state	= ep.choice(self.get_active_states())
			self.initial	= picked_state
			picked_state.make_initial()
		elif .3 < random_number <= .5:
			print('Cambiar simbolos de entrada')
			picked_state.mut_inputs()
		elif .5 < random_number <= .7:
			print('Cambiar un simbolo de salida')
			pos = ep.randint(self.alphabet_length)
			print('Cambiar salida:', pos + 1)
			picked_state.mut_outputs(pos)
		elif .7 < random_number <= .9:
			print('Cambiar estados de salida')
			pos = ep.randint(self.alphabet_length)
			state_choosed = ep.choice(self.get_active_states())
			print('Reemplazo propuesto: ', state_choosed.name)
			print('Posicion propuesta: ', pos + 1)
			picked_state.mut_neightbor(state_choosed, pos)
		else:
			print('Activar estado')
			if picked_state.status != 2:
				picked_state.activate()
		print('Estado seleccionado: ', picked_state.name)
		print('After:  ', self)
		print()

	def get_graph(self, filename='Subject', view=False):
		self.graph.attr('node',color='4', colorscheme='paired4')
		for state in self.get_active_states():
			if state.status == 2:
				self.graph.node('empty', label='', shape='none')
				self.graph.edge('empty',state.name,color='2', colorscheme='paired4')
				self.graph.node(state.name, color='2', colorscheme='paired4')
			for idx, neighbour in enumerate(state.neighbours):
				self.graph.edge(state.name, neighbour.name, label = f'  {state.inputs[idx]}/{state.outputs[idx]}\t\n', color='8', colorscheme='paired8')
		self.graph.render(filename, view=view, cleanup=True)

	def full_representation(self):
		output, fitness = self.get_fitness()
		return f'{str(self)} -> {self.predict_string} - {output} -> {fitness}'
	def __str__(self):
		return '|'.join([str(state) for state in self.states])

	def __repr__(self):
		return str(self)

	def __gt__(self, other):
		return self.get_fitness()[1] > other.get_fitness()[1]

	def __ge__(self, other):
		return self.get_fitness()[1] >= other.get_fitness()[1]


	def __eq__(self, other):
		return self.get_fitness()[1] == other.get_fitness()[1]

	def __iter__(self):
		self.iterator	= 0
		return self

	def __next__(self):
		string = str(self)
		if self.iterator > 0:
			raise StopIteration
		self.iterator += 1
		return string
