import numpy as np
from tabulate import tabulate
from utils import de_utils as de
import sys

default_headers = ['x', 'y', 'a', 'b']

default_params = {
	'iterations'	: 1000,
	'n_dimension'	: 4,
	'n_poblation'	: 16,
	'range'			: (-10,10),
	'mut_const'		: 0.8,
}

def print_tab(poblation, title = '', headers = default_headers, show_index = 'always'):
	align = ["center"] * (len(headers) + (1 if show_index else 0) )
	print(f'{title}')
	print(tabulate(poblation, headers = headers, tablefmt='orgtbl',
			showindex = show_index, colalign = align),'\n')


def run(new_params={}, stdout=None):
	if not stdout: 
		stdout = sys.stdout
	default_params.update(new_params)
	print_tab(default_params.items(), title='Parametros', headers= ['Name','Value'], show_index = None)
	params = type('new_dict', (object,), default_params)

	poblation = np.random.uniform(*params.range,(params.n_poblation, params.n_dimension))
	print_tab(poblation, 'Poblacion',headers=['x','y','a','b'])

	fitness	= list(map(lambda vector: de.get_fitness(vector), poblation))

	res = np.column_stack((poblation, fitness))

	print_tab(res, 'Fitness', headers=['x','y','a','b', 'f(x, y, a, b)'])

	for iteration in range(params.iterations):
		print(f'-------- Iteracion {iteration + 1} --------')
		new_poblation = []
		for idx, subject in enumerate(poblation):
			print(f'******** Vector {idx} ********')
			random_vectors_idx = np.random.randint(0, params.n_poblation, 3)
			print('Indices de vectores seleccionados (xk, xl, xm):', random_vectors_idx)

			k_vector, l_vector, m_vector = poblation[random_vectors_idx]
			print('xk:', k_vector)
			print('xl:', l_vector)
			print('xm:', m_vector)


			trial_vector, is_better = de.mut_cross(subject, k_vector, l_vector, m_vector, params.mut_const, fitness[idx])

			if is_better:
				new_poblation.append(trial_vector)
				print('El vector target es reemplazado por el trial')
			else:
				new_poblation.append(subject.copy())
				print('El vector target continua en la siguiente poblacion')
			
			print('\n' * 2)

		temp = sys.stdout
		sys.stdout = stdout
		best_subject_idx = np.argmin(fitness)
		print(f"\tIteration: {iteration + 1}/{params.iterations} - Best subject {np.around(poblation[best_subject_idx],2)} -> {fitness[best_subject_idx]:.15f} {' ' * 19}", end='\r')
		sys.stdout = temp

		poblation	= np.array(new_poblation)
		fitness		= list(map(lambda vector: de.f(*vector), poblation))
		res = np.column_stack((poblation, fitness))


		print_tab(res, 'Nueva poblacion - Fitness', headers=['x','y','a','b', 'f(x, y, a, b)'])


if __name__ == '__main__':
	console_stdout	= sys.stdout
	sys.stdout		= open(f'./output/minimize.txt', 'w')

	run(stdout = console_stdout)

	sys.stdout		= console_stdout
	print()