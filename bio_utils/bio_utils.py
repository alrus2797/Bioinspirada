import numpy as np

def blx_cross(c1,c2, alpha, verbose = False):
	beta = np.random.uniform(-alpha, 1 + alpha)
	if verbose: print(beta)
	return list(map(lambda x,y: x + beta * (y-x), c1,c2))

def uniform_mut(c1):
	pos = np.random.randint(0,len(c1))
	c1[pos] = np.random.uniform(-10,10)

def normalize(c1):
	n = (c1*100).astype(int)
	return n + 10

def show_map_table(title,m1, m2,cols=[0,1,2]):
	print(title)
	print('-'*49)
	print('|\t{}\t|\t{}\t |\t{}\t|'.format(*cols))
	print('-'*49)
	list(map(lambda x,y: print(f'|\t{x[0]}\t-\t{x[1]}\t=>\t{y}\t|') , m1, m2))
	print()
