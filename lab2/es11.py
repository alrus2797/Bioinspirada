import math
import numpy as np
from utils import bio_utils as bu, es11_utils as es
from tabulate import tabulate

def f(x,y):
	return -math.cos(x)*math.cos(y)*math.exp(-(x-math.pi)**2-(y-math.pi)**2)

sep = '-----------------------------'
params = {
	'n_poblation'   : 1,
	'n_dimension'   : 2,
	'iterations'	: 500,
	'sigma'         : 1,
	'range'			: (-10,10),
}

print('Parametros:')
print(tabulate(params.items(),headers= ['Name','Value'],tablefmt='orgtbl'),'\n')

params = type('new_dict', (object,), params)

poblation	= np.random.uniform(*params.range,(params.n_poblation, params.n_dimension))
sigmas		= np.full((params.n_poblation, params.n_dimension), params.sigma).astype('float64')
fitness		= list(map(lambda x : f(*x), poblation))
print('Poblacion Inicial:')
print(tabulate(poblation, headers=['x','y'],tablefmt='orgtbl', showindex='always'),'\n')

for iteration in range(params.iterations):
	print('|'+sep, f'Iteracion {iteration + 1}', sep+'|','\n')
	print('Poblacion Actual - Calculo de aptitud:')
	print(tabulate(np.column_stack((poblation, sigmas ,fitness)), headers= ['x','y', 'sigma1','sigma2','f(x,y)'],tablefmt='orgtbl', showindex='always'),'\n')

	for idx, (subject, sub_fitness, sigma) in enumerate(zip(poblation, fitness, sigmas)):
		candidate	= es.get_candidate(subject, sigma, params.range, verbose = True)
		cte_fitness	= f(*candidate)
		print(f'{np.around(candidate,5)} -> {cte_fitness}', end='')
		if cte_fitness <= sub_fitness:
			poblation[idx]	= candidate
			fitness[idx]	= cte_fitness
			sigmas[idx]		*= 1.5
			print(' <- Sobrevive')
		else:
			sigmas[idx]		*= 0.9036
			print(' <- No sobrevive')
		print()
		

print('Poblacion Final:')
print(tabulate(np.column_stack((poblation, sigmas ,fitness)), headers= ['x','y', 'sigma1','sigma2','f(x,y)'],tablefmt='orgtbl', showindex='always'),'\n')


			


	






