import math
import numpy as np
from utils import ga_utils as ga, es_utils as es
from tabulate import tabulate
import sys


def f(x,y):
	return -math.cos(x)*math.cos(y)*math.exp(-(x-math.pi)**2-(y-math.pi)**2)

sep = '-----------------------------'



default_params = {
	'iterations'	: 500,
	'n_dimension'   : 2,
	'sigma'			: 1,
	'mu'            : 8,
	'_lambda'		: 1,
	'range'			: (-10,10),
}


def run(new_params={}, stdout=None):
	if not stdout: 
		stdout = sys.stdout
	print('Parametros:')
	default_params.update(new_params)
	print(tabulate(default_params.items(),headers= ['Name','Value'],tablefmt='orgtbl'),'\n')
	params = type('new_dict', (object,), default_params)
	params.n_poblation = params.mu

	poblation	= np.random.uniform(*params.range,(params.n_poblation, params.n_dimension))
	sigmas		= np.full((params.n_poblation, params.n_dimension), params.sigma).astype('float64')
	fitness		= np.array(list(map(lambda x : f(*x), poblation)))
	delta_sigma	= es.get_delta_sigma(params.n_dimension)
	print('Poblacion Inicial:')
	print(tabulate(poblation, headers=['x','y'],tablefmt='orgtbl', showindex='always'),'\n')

	for iteration in range(params.iterations):
		print('|'+sep, f'Iteracion {iteration + 1}', sep+'|','\n')
		print(f'Poblacion Seleccionada ({params.mu} sujetos seleccionados) - Calculo de aptitud:')
		print(tabulate(np.column_stack((poblation, sigmas, fitness)), headers= ['x','y', 'sigma1','sigma2','f(x,y)'],tablefmt='orgtbl', showindex='always'),'\n')
		lambda_poblation	= poblation.copy()
		lambda_sigmas		= sigmas.copy()
		lambda_fitness		= fitness.copy()
		# print(params._lambda)
		for lambda_counter in range(params._lambda):
			parents_set_idx = np.random.randint(0, params.n_poblation, (2, 2))
			print(f'Generar descendiente: {lambda_counter + 1}')
			print('Cruzamiento:')
			parents_idx = np.zeros(2).astype(int)
			
			for idx, parents in enumerate(parents_set_idx):
				min_idx = parents[np.argmin(fitness[parents])]
				parents_idx[idx]	= min_idx
				print(f'\tParents {idx + 1}: {parents} => {min_idx} => {poblation[min_idx]} {sigmas[min_idx]}')
				
			child		= ga.mean_cross(*poblation[parents_idx])
			sigma_child	= es.sigma_uniform_cross(*sigmas[parents_idx])
			print(f'Hijo {lambda_counter + 1}: {child} sigmas: {sigma_child}\n') 
			print('Mutacion:')
			sigma_child = es.sigma_mutation(sigma_child, delta_sigma)
			child		= es.subject_mutation(child, sigma_child, params.range, True)

			print(f'Hijo {lambda_counter + 1} mutado - Sigma mutado: {child} - {sigma_child}\n')
			
			# Concatenate
			lambda_poblation	= np.row_stack((lambda_poblation, child))
			lambda_sigmas		= np.row_stack((lambda_sigmas, sigma_child))
			lambda_fitness		= np.append(lambda_fitness, f(*child))
		
		print('Poblacion mu y sigma')
		print(tabulate(np.column_stack((lambda_poblation, lambda_sigmas, lambda_fitness)), headers= ['x','y', 'sigma1','sigma2','f(x,y)'],tablefmt='orgtbl', showindex='always'),'\n')
		
		ordered_idx	= np.argsort(lambda_fitness)
		poblation	= lambda_poblation[ordered_idx][:-params._lambda]
		sigmas		= lambda_sigmas[ordered_idx][:-params._lambda]
		fitness		= lambda_fitness[ordered_idx][:-params._lambda]

		best_subject_idx = np.argmin(fitness)

		temp = sys.stdout
		sys.stdout = stdout
		
		print(f"\tIteration: {iteration + 1}/{params.iterations} - Best subject {poblation[best_subject_idx]} -> {fitness[best_subject_idx]:.5f}",end='\r')
		# print(f'\tBest subject: {poblation[best_subject_idx]}', end='\r')
		sys.stdout = temp
			

	print('Poblacion Final Seleccionada:')
	print(tabulate(np.column_stack((poblation, sigmas ,fitness)), headers= ['x','y', 'sigma1','sigma2','f(x,y)'],tablefmt='orgtbl', showindex='always'),'\n')


			


	






