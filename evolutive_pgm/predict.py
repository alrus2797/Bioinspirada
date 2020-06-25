from evolutive_pgm.subject import Subject
from tabulate import tabulate
from utils import ep_utils as ep

import numpy as np
import sys

default_params = {
	'iterations'	: 1000,
	'n_poblation'	: 16,
	'n_states'		: 5,
	'alphabet'		: [0,1],
	'predict_seq'	: '0111001010011100101001110010100111001010'
}

def _run(new_params = {}, stdout = None):
	if not stdout: 
		stdout = sys.stdout
	print('Parametros:')
	default_params.update(new_params)
	print(tabulate(default_params.items(),headers= ['Nombre','Valor'],tablefmt='orgtbl', colalign=("center","center")),'\n')
	params = type('new_dict', (object,), default_params)

	poblation = []
	for i in range(params.n_poblation):
		poblation.append(Subject(params.n_states, params.alphabet, params.predict_seq))

	poblation	= np.array(poblation)
	# fitness		= np.array([subject.get_fitness()[1] for subject in poblation])
	print('Poblacion Inicial:')
	print(tabulate(poblation, headers=['Individuos'],tablefmt='orgtbl', showindex='always', colalign=("center","center")),'\n')

	ite, best = 0, poblation[0]

	for iteration in range(params.iterations):
			print('|' + '-' * 20, f'Iteracion {iteration + 1}', '-' * 20 + '|','\n')
			print(f'Poblacion Seleccionada - Calculo de aptitud:')
			ep.show_subjects(poblation)
			children	= np.array([subject.copy() for subject in poblation])

			print('\nProceso Mutacion')
			for idx, child in enumerate(children):
				print(f'Mutacion {idx + 1}\n')
				child.mutate()

			ep.show_subjects(children, 'Descendientes')
			
			idx_best_poblation	= np.argsort(poblation)[params.n_poblation // 2:]
			idx_best_children	= np.argsort(children)[params.n_poblation // 2:]

			ep.show_subjects(poblation[idx_best_poblation], 'Mejores Ascendientes')

			ep.show_subjects(children[idx_best_children], 'Mejores Descendientes')

			max_poblation	= idx_best_poblation[-1]
			max_children	= idx_best_children[-1]

			current_best = max(poblation[max_poblation], children[max_children])


			temp = sys.stdout
			sys.stdout = stdout
			
			if current_best >= best:
				best	= current_best
				ite		= iteration
				b_output, b_fitness	= best.get_fitness()
				print(f"\tIteration: {iteration + 1}\t/ {params.iterations} - Best subject {best} -> {b_output}, {b_fitness}",end='\r')
			
			sys.stdout = temp


			poblation	= np.concatenate((poblation[idx_best_poblation], children[idx_best_children]))


			ep.show_subjects(poblation, 'Nueva Poblacion')

	print(f'Best found in iteration {ite + 1}: {best} -> {best.get_fitness()[1]}')
	return best
	best.get_graph('output/best_subject')

def run(new_params={}, stdout=None):
	for i in range(100):
		temp = sys.stdout
		sys.stdout = stdout
		print('\n')
		print('Hyperiteration', i + 1)
		sys.stdout = temp
		best=_run(new_params, stdout)
		best.get_graph(f'output/subjects/best_subject_{i}')

		


