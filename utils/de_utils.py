import numpy as np


def f(x, y, a, b):
	return ((x + 2 * y - 7) ** 2) + ((2 * x + y - 5) ** 2) + ((a + 2 * b - 7) ** 2) + ((2 * a + b - 5) ** 2)

def mutate_process(k_vector, l_vector, m_vector, mut_const):
	print('Mutacion:')
	op_vector = k_vector - l_vector
	print(f'xk - xl (Vector Diferencia): {op_vector}')

	op_vector = mut_const * op_vector
	print(f'F * (xk - xl) (Vector Ponderado): {op_vector}')

	op_vector = m_vector + op_vector
	print(f'xm + F * (xk - xl) (Vector Mutado): {op_vector}')
	
	return op_vector

def cross_proccess(subject, mutated_vector):
	print('Cruzamiento: ')
	random_numbers = np.random.rand(len(subject)) 
	print('Numeros aleatorios: ', random_numbers)
	mask = np.where(random_numbers < 0.5)[0]
	print('Indices seleccionados: ', mask)
	for idx in mask:
		subject[idx] = mutated_vector[idx]

def get_fitness(subject, f = f):
	return f(*subject)

def mut_cross(subject, k_vector, l_vector, m_vector, mut_const, subject_fitness):
	mutated_vector  = mutate_process(k_vector, l_vector, m_vector, mut_const)
	trial_vector    = subject.copy()
	cross_proccess(trial_vector, mutated_vector)

	trial_fitness = get_fitness(trial_vector)
	print(f'Vector Trial: {trial_vector} - Fitness: {subject}')

	return trial_vector, trial_fitness < subject_fitness