import random
import numpy as np
from operator import add, sub, mul, truediv as div

_operators      = ['+', '-', '*', '/']
_f_operators	= [add, sub, mul, div]
_numbers_range  = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

def generate_subject(length = 7, operators = _operators, numbers_range = _numbers_range, w_operator = True):
	subject = [0] * length
	if w_operator: numbers_range = list(numbers_range) + ['X']
	for i in range(length):
		subject[i] = random.choice(numbers_range if i % 2 == 0 else operators)
	while subject_is_valid(subject) == None:
		for i in range(length):
			subject[i] = random.choice(numbers_range if i % 2 == 0 else operators)
	return subject


def generate_poblation(n_poblation):
	poblation = []
	for i in range(n_poblation):
		poblation.append(generate_subject())
	return poblation

def evaluate_operation(operation, _input = 0):
	if len(operation) > 3:
		raise Exception(f'{operation}: Operation too big')
	operator_idx	= _operators.index(operation[1])
	function		= _f_operators[operator_idx]
	try:
		var_idx	= np.where(operation == 'X')[0]
		# print(operation)
		operation[var_idx] = _input
	except ValueError:
		print(operation)
		pass
	return function(float(operation[0]), float(operation[2]))

def evaluate_subject(subject, _input):
	factor1 = evaluate_operation(np.array(subject[:3]), _input)
	factor2 = evaluate_operation(np.array(subject[4:]), _input)
	return evaluate_operation(np.array([factor1, subject[3], factor2]))

def subject_is_valid(subject, _input = 0):
	try:
		return evaluate_subject(subject, _input)
	except ZeroDivisionError:
		return None

def get_fitness(subject, tests):
	error = 0
	for _input, output in tests:
		evaluated = evaluate_subject(subject, _input)
		print(f'{_input}\t{output}\t{evaluated}\t{output - evaluated}')
		error += evaluated ** 2
	error = error / len(tests)
	print(f'Fitness: {error} \n')
	return error

def show_subject(subject):
	for gen in subject:
			print(gen, end = '|')
	print()

def show_poblation(poblation, w_fitness = []):
	show_fit = False
	if len(w_fitness) != 0: show_fit = True
	for idx, subject in enumerate(poblation):
		print(f'{idx}) ', end = '|')
		show_subject(subject)
		if show_fit: print(f'Fitness: {w_fitness[idx]}')
	print()
		

def get_poblation_fitness(poblation, tests):
	fitness = [0] * len(poblation)
	print('Calcular la Aptitud para cada Individuo')
	for idx, subject in enumerate(poblation):
		print(f'{idx}) ', end = '|')
		show_subject(subject)
		fitness[idx] = get_fitness(subject, tests)
	return fitness

def rand_point_cross(subject1, subject2):
	pos = random.randint(0, len(subject1) - 1)
	print(f'Padre 1: ', end='|')
	show_subject(subject1)
	print(f'Padre 2: ', end='|')
	show_subject(subject2)
	print('Punto de cruzamiento:', pos)
	subject1[:pos], subject2[:pos] = subject2[:pos], subject1[:pos]
	if subject_is_valid(subject1) == None or subject_is_valid(subject2) == None:
		print('No valido, revirtiendo...')
		subject1[:pos], subject2[:pos] = subject2[:pos], subject1[:pos]
	print('Descendiente 1: ', end= '|')
	show_subject(subject1)
	print('Descendiente 2: ', end= '|')
	show_subject(subject2)


def simple_mut(subject):
	random_number = random.randint(0,len(subject) - 1)
	print('Sujeto a mutar: ', end= '|')
	show_subject(subject)
	print('Gen a mutar:', random_number)
	subject[random_number] = random.choice(_numbers_range if random_number % 2 == 0 else _operators)
	while subject_is_valid(subject) == None:
		# print(subject)
		print('Sujeto invalido: ', end='|')
		show_subject(subject)
		print('Generando nuevo')
		random_number = random.randint(0,len(subject) - 1)
		print('Gen a mutar:', random_number)
		subject[random_number] = random.choice(_numbers_range if random_number % 2 == 0 else _operators)
	print('Sujeto mutado valido: ', end= '|')	
	show_subject(subject)
