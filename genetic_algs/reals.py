import numpy as np
import math
from utils import ga_utils
from tabulate import tabulate

sep = '-----------------------------'
params = {
	'iterations'	: 2500,
	'n_population'	: 16,
	'mating_length'	: 16,
	'p_cross'		: 0.9,
	'p_mut'			: 0.05,
	'blx_a'			: 0.5,
}

print(tabulate(params.items()))

def f(x,y):
	return -math.cos(x)*math.cos(y)*math.exp(-(x-math.pi)**2-(y-math.pi)**2)

params = type('new_dict', (object,), params)

population = np.random.uniform(-10,10,(params.n_population,2))
apptitude = list(map(lambda x : (f(*x[1]), x[0]),enumerate(population)))


best_apptitude = float('inf')

for iteration in range(params.iterations):
	print('|'+sep, f'Iteracion {iteration + 1}', sep+'|','\n')
	print('Poblacion Inicial:') if iteration + 1 == 1 else print('Poblacion Actual:')
	print(tabulate(population,headers=['x','y'],tablefmt='orgtbl', showindex='always'),'\n')
	print('Calculo de aptitud:')
	# print('[\tx\t','\ty\t','\tf(x,y)\t ]')
	print(tabulate(np.append(population, np.array(apptitude)[:,[0]], axis=1), headers= ['x','y','f(x,y)'],tablefmt='orgtbl'),'\n')

	mating_pool = [0] * params.n_population
	pairs = np.random.randint(0, params.n_population, ((params.n_population,2)))

	for i,(p1, p2) in enumerate(pairs):
		# print(i,p1,p2)
		winner = min(apptitude[p1], apptitude[p2])[1]
		mating_pool[i] = winner

	# print('Creacion de MATING POOL')
	# print('-'*49)
	# print('|\tm1\t|\tm2\t |\twin\t|')
	# print('-'*49)
	# list(map(lambda x,y: print(f'|\t{x[0]}\t-\t{x[1]}\t=>\t{y}\t|') , pairs, mating_pool))
	ga_utils.show_map_table('Creacion de MATING POOL',pairs, mating_pool, cols=['m1','m2','win'])

	parents = np.random.randint(0, params.n_population, ((params.n_population,2)))

	new_population = population.copy()
	for i, (m1,m2) in enumerate(parents):
		# Reproduction starts
		idp1, idp2 = mating_pool[m1], mating_pool[m2]
		print(f'Padres: {m1} - {m2} => {idp1} - {idp2} => {population[idp1]}, {population[idp2]}')
		print('Cruzamiento? ', end='')
		if np.random.random() < params.p_cross:
			print('Si')
			print('Beta: ')
			child = ga_utils.blx_cross(population[idp1],population[idp2], params.blx_a, True)
		else:
			print('No')
			child = new_population[min(apptitude[idp1], apptitude[idp2])[1]]
		print("Hijo: ", child)
		new_population[i] = child.copy()

		# Mutation starts

		print('Mutacion? ', end='')
		if np.random.random() < params.p_mut:
			print('Si')
			ga_utils.uniform_mut(new_population[i])
			print('Nueva forma:', new_population[i])
		else: print('No')
		print()
	print('|'+sep, f'Fin de Iteracion {iteration + 1}', sep+'|','\n')

	population = new_population
	apptitude = list(map(lambda x : (f(*x[1]), x[0]),enumerate(population)))

	best_curr_gen = min(apptitude)
	if  best_curr_gen[0] < best_apptitude:
		best_of_best, best_it, best_curr_gen = population[best_curr_gen[1]].copy(), iteration+1, best_curr_gen


print('Poblacion Final:')
print(tabulate(np.append(population, np.array(apptitude)[:,[0]], axis=1), headers= ['x','y','f(x,y)'],tablefmt='orgtbl'),'\n')
print('Best:', best_of_best, '=>',best_curr_gen[0], 'Iteration', best_it)



	





