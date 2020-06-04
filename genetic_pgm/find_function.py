from utils import gp_utils as gp
from tabulate import tabulate
import sys
import random
import numpy as np
from graphviz import Digraph

default_params = {
	'iterations'	: 1000,
	'n_poblation'	: 8,
	'p_cross'		: 0.2,
	't_cross'		: 2,
	'p_mut'			: 0.4,
	't_mut'			: 3,
	'p_repr'		: 0.4,
	't_repr'		: 3,
}


tests = [
	[0, 0],
	[0.1, 0.005],
	[0.2, 0.02],
	[0.3, 0.045],
	[0.4, 0.08],
	[0.5, 0.125],
	[0.6, 0.18],
	[0.7, 0.245],
	[0.8, 0.32],
	[0.9, 0.405],
]

def run(new_params = {}, stdout = None):
	if not stdout: 
		stdout = sys.stdout
	default_params.update(new_params)
	print('Parametros:')
	print(tabulate(default_params.items(), headers = ['Nombre','Valor'], tablefmt='orgtbl', colalign = ("center","center")), '\n')
	params = type('new_dict', (object,), default_params)

	graph      = Digraph(comment = 'Arbol', format='png')

	poblation	= gp.generate_poblation(params.n_poblation)
	print('Poblacion inicial')
	gp.show_poblation(poblation)
	fitness		= gp.get_poblation_fitness(poblation, tests)

	poblation, fitness = np.array(poblation), np.array(fitness)

	gp.show_poblation(poblation, fitness)

	for iteration in range(params.iterations):
		print(f'-------------- Iteracion {iteration + 1} --------------')
		new_poblation = []

		while len(new_poblation) < params.n_poblation:
			random_number = random.random()
			print('Aleatorio: ', random_number)

			if random_number <= params.p_cross:
				# Parent 1
				print('------ Cruzamiento ------')
				tourney_idx = np.random.randint(0, params.n_poblation, params.t_cross)
				print(f'Seleccionados para el torneo padre 1: ', tourney_idx)
				selected_fitness	= fitness[tourney_idx]
				parent1_index		= tourney_idx[np.argmin(selected_fitness)]
				print(f'Ganador: {parent1_index}')

				# Parent 2
				tourney_idx = np.random.randint(0, params.n_poblation, params.t_cross)
				print(f'Seleccionados para el torneo padre 2: ', tourney_idx)
				selected_fitness	= fitness[tourney_idx]
				parent2_index		= tourney_idx[np.argmin(selected_fitness)]
				print(f'Ganador: {parent2_index}')
				parent1	= poblation[parent1_index].copy()
				parent2	= poblation[parent2_index].copy()
				gp.rand_point_cross(parent1, parent2)
				new_poblation.append(parent1)
				if len(new_poblation) == params.n_poblation:
					print('Se inserta solo Descendiente 1')
					break

				new_poblation.append(parent2)
				print('Se insertan los dos descendientes')

			elif params.p_cross < random_number <= params.p_cross + params.p_mut:
				# Mut
				print('------ Mutacion ------')
				tourney_idx	= np.random.randint(0, params.n_poblation, params.t_mut)
				print(f'Seleccionados para el torneo: ', tourney_idx)
				selected_fitness	= fitness[tourney_idx]
				winner_index		= tourney_idx[np.argmin(selected_fitness)]
				print(f'Ganador: {winner_index}')
				winner	= poblation[winner_index].copy()
				gp.simple_mut(winner)
				new_poblation.append(winner)

			else:
				# Repr
				print('------ Replicacion ------')
				tourney_idx = np.random.randint(0, params.n_poblation, params.t_repr)
				print(f'Seleccionados para el torneo: ', tourney_idx)
				selected_fitness	= fitness[tourney_idx]
				winner_index		= tourney_idx[np.argmin(selected_fitness)]
				print(f'Ganador: {winner_index} => ', end = '')
				winner	= poblation[winner_index].copy()
				gp.show_subject(winner)
				new_poblation.append(winner)

			print()

		poblation = new_poblation
		print('Calcular aptitud para cada individuo: ')
		fitness	= np.array(gp.get_poblation_fitness(poblation, tests))
		print('Nueva poblacion: ')
		gp.show_poblation(poblation, fitness)
	
	best_idx = np.argmin(fitness)
	best = poblation[best_idx]

	for i in range(len(best)):
		graph.node(str(i), best[i])

	graph.edge('3', '1')
	graph.edge('3', '5')
	graph.edge('1', '0')
	graph.edge('1', '2')
	graph.edge('5', '4')
	graph.edge('5', '6')

	graph.render('output/best_tree', view=True, cleanup=True)