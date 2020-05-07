import numpy as np
from tabulate import tabulate
from bio_utils import bio_utils

sep = '-----------------------------'
params = {
	'iterations'	: 5000,
	'n_population'	: 20,
	'n_places'      : 10,
	'mating_length'	: 8,
	'p_cross'		: 0.9,
	'p_mut'			: 0.07,
}

params = type('new_dict', (object,), params)

places = list(range(params.n_places))

routes = [
	[0,	12, 3,  23, 1,  5,  23, 56, 12, 11],
	[12, 0, 9,  18, 3,	41,	45,	5,	41, 27],
	[3,	 9, 0,  89, 56,  21,  12, 48, 14, 29],
	[23,18,89,   0, 87,  46,  75, 17, 50, 42],
	[1, 3, 56,  87, 0,  55,  22, 86, 14, 33],
	[5,41, 21,  46, 55,  0,  21, 76, 54, 81],
	[23,45,12,  75, 22,  21,  0, 11, 57, 48],
	[56,5,48,  17, 86,  76,  11, 0, 63, 24],
	[12,41, 14,  50, 14,  54,  57, 63, 0, 9],
	[11,27, 29,  42, 33,  81,  48, 24, 9, 0],
]


population = []

for i in range(params.n_population):
	p = places.copy()
	np.random.shuffle(p)
	population.append(p)

population = np.array(population)
# print('Población Inicial')
# print(tabulate(population, showindex='always', headers = ['idx']+list(range(1,params.n_population+1)), tablefmt='simple'))
bio_utils.show_map_table('Poblacion Inicial', population, np.array(range(params.n_population)).reshape(-1,1),lambda x, y: print(bio_utils.show_route(x)))
apptitutes = list(map(lambda x: (bio_utils.get_route_cost(routes, x[1]), x[0]), enumerate(population)))

for iteration in range(params.iterations):

	bio_utils.show_map_table('Poblacion Actual - Aptitudes', population, np.array(apptitutes)[:,0],lambda x, y: print(bio_utils.show_route(x),' => ',y))

	mating_pool = [0] * params.n_population
	pairs = np.random.randint(0, params.n_population, ((params.n_population,2)))
	for i,(p1, p2) in enumerate(pairs):
		# print(i,p1,p2)
		winner = min(apptitutes[p1], apptitutes[p2])[1]
		mating_pool[i] = winner
		
	bio_utils.show_map_table('Creacion de MATING POOL',pairs, mating_pool, cols = ['m1','m2','win'])

	parents = np.random.randint(0, params.n_population, ((params.n_population//2,2)))

	new_population = []

	for i, (m1, m2) in enumerate(parents):
		# Reproduction starts
		idp1, idp2 = mating_pool[m1], mating_pool[m2]
		print(f'Padres: {m1} - {m2} => {idp1} - {idp2} => {bio_utils.show_route(population[idp1])}, {bio_utils.show_route(population[idp2])}')
		print('Cruzamiento? ', end='')
		if np.random.random() < params.p_cross:
			print('Si')
			child1, child2 = bio_utils.obx_cross(population[idp1],population[idp2])
		else: print('No')
		new_population.append(child1)
		new_population.append(child2)
		print("Hijos: ")
		print(f'{bio_utils.show_route(child1)} - {bio_utils.show_route(child2)}')
		# Mutation starts

		print('Mutacion? Hijo 1 ', end='')
		if np.random.random() < params.p_mut:
			print('Si')
			bio_utils.simple_mut(child1)
			print('Nueva forma:', bio_utils.show_route(child1))
		else: print('No')

		print('Mutacion? Hijo 2 ', end='')
		if np.random.random() < params.p_mut:
			print('Si')
			bio_utils.simple_mut(child2)
			print('Nueva forma:', bio_utils.show_route(child2))
		else: print('No')
		print()
	
	population = new_population
	apptitutes = list(map(lambda x: (bio_utils.get_route_cost(routes, x[1]), x[0]), enumerate(population)))

	print('|'+sep, f'Fin de Iteracion {iteration + 1}', sep+'|','\n')



bio_utils.show_map_table('Poblacion Final', population, np.array(apptitutes)[:,0],lambda x, y: print(bio_utils.show_route(x),' => ',y))
# print('Best:', best_of_best, 'Iteration', best_it)




